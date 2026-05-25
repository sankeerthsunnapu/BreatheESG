import pandas as pd
from .utils import validate_record
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import EmissionRecordSerializer

from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view

from .serializers import AuditLogSerializer

class UtilityUploadView(APIView):

    def post(self, request):

        file = request.FILES.get('file')

        try:
            df = pd.read_csv(file)

            company, _ = Company.objects.get_or_create(
                name="Demo Enterprise"
            )

            source = DataSource.objects.create(
                company=company,
                source_type='UTILITY'
            )

            records = []

            for _, row in df.iterrows():

                quantity = float(
                row.get('kWh_Consumed', 0)
                )

                validation = validate_record(quantity, 'kwh')

                record = EmissionRecord.objects.create(
                    company=company,
                    source=source,
                    activity_type='Electricity Consumption',
                    scope='SCOPE_2',
                    quantity=quantity,
                    unit='kwh',
                    normalized_quantity=quantity,
                    emission_factor=0.45,
                    emission_value=quantity * 0.45,
                    record_date=row.get('Billing_End'),
                    suspicious_flag=validation['suspicious'],
                    validation_message=validation['message']
                )

                records.append(record)

            serializer = EmissionRecordSerializer(
                records,
                many=True
            )

            return Response(serializer.data)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=500
            )

class SAPUploadView(APIView):

    def post(self, request):

        file = request.FILES.get('file')

        if not file:
            return Response(
                {"error": "No file uploaded"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            df = pd.read_csv(file)

            company, _ = Company.objects.get_or_create(
                name="Demo Enterprise"
            )

            source = DataSource.objects.create(
                company=company,
                source_type='SAP',
                uploaded_by=request.user
                if request.user.is_authenticated
                else None
            )

            RawUpload.objects.create(
                source=source,
                file=file,
                original_filename=file.name
            )

            created_records = []

            for _, row in df.iterrows():

                quantity = float(row.get('Menge', 0))

                validation = validate_record(quantity,row.get('unit', '')
                )

                record = EmissionRecord.objects.create(
                    company=company,
                    source=source,
                    activity_type=row.get(
                        'Brennstofftyp',
                        'Unknown Fuel'
),
                    scope='SCOPE_1',
                    quantity=quantity,
                    unit=row.get('Einheit', 'Liters'),
                    normalized_quantity=quantity,
                    emission_factor=2.68,
                    emission_value=quantity * 2.68,
                    record_date=row.get('Buchungsdatum'),
                    suspicious_flag=validation['suspicious'],
                    validation_message=validation['message']
                )

                created_records.append(record)

            serializer = EmissionRecordSerializer(
                created_records,
                many=True
            )

            return Response(serializer.data)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class TravelUploadView(APIView):

    def post(self, request):

        file = request.FILES.get('file')

        try:
            df = pd.read_csv(file)

            company, _ = Company.objects.get_or_create(
                name="Demo Enterprise"
            )

            source = DataSource.objects.create(
                company=company,
                source_type='TRAVEL'
            )

            records = []

            for _, row in df.iterrows():

                distance = float(
                row.get('Distance_KM', 0)
                )

                validation = validate_record(distance, 'km')

                category = row.get(
                'Travel_Category',
                'Flight'
                )

                factor = 0.12

                if category == 'Hotel':
                    factor = 15

                emission = distance * factor

                record = EmissionRecord.objects.create(
                    company=company,
                    source=source,
                    activity_type=category,
                    scope='SCOPE_3',
                    quantity=distance,
                    unit='km',
                    normalized_quantity=distance,
                    emission_factor=factor,
                    emission_value=emission,
                    record_date=row.get('Travel_Date'),
                    suspicious_flag=validation['suspicious'],
                    validation_message=validation['message']
                )

                records.append(record)

            serializer = EmissionRecordSerializer(
                records,
                many=True
            )

            return Response(serializer.data)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=500
            )

class EmissionRecordListView(ListAPIView):

    queryset = EmissionRecord.objects.all().order_by('-created_at')

    serializer_class = EmissionRecordSerializer


@api_view(['POST'])
def approve_record(request, pk):

    try:
        record = EmissionRecord.objects.get(id=pk)

        old_status = record.status

        record.status = 'APPROVED'
        record.locked = True
        record.save()

        AuditLog.objects.create(
            emission_record=record,
            field_name='status',
            old_value=old_status,
            new_value='APPROVED',
            edited_by=request.user if request.user.is_authenticated else None
        )

        return Response({
            "message": "Record approved"
        })

    except EmissionRecord.DoesNotExist:
        return Response(
            {"error": "Record not found"},
            status=404
        )

@api_view(['POST'])
def reject_record(request, pk):

    try:
        record = EmissionRecord.objects.get(id=pk)

        old_status = record.status

        record.status = 'REJECTED'
        record.save()

        AuditLog.objects.create(
            emission_record=record,
            field_name='status',
            old_value=old_status,
            new_value='REJECTED',
            edited_by=request.user if request.user.is_authenticated else None
        )

        return Response({
            "message": "Record rejected"
        })

    except EmissionRecord.DoesNotExist:
        return Response(
            {"error": "Record not found"},
            status=404
        )

@api_view(['GET'])
def dashboard_summary(request):

    total = EmissionRecord.objects.count()

    approved = EmissionRecord.objects.filter(
        status='APPROVED'
    ).count()

    rejected = EmissionRecord.objects.filter(
        status='REJECTED'
    ).count()

    suspicious = EmissionRecord.objects.filter(
        suspicious_flag=True
    ).count()

    pending = EmissionRecord.objects.filter(
        status='PENDING'
    ).count()

    return Response({
        "total_records": total,
        "approved_records": approved,
        "rejected_records": rejected,
        "suspicious_records": suspicious,
        "pending_records": pending
    })

class AuditLogListView(ListAPIView):

    queryset = AuditLog.objects.all().order_by('-edited_at')

    serializer_class = AuditLogSerializer