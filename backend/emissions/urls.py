from django.urls import path

from .views import (
    SAPUploadView,
    UtilityUploadView,
    TravelUploadView,
    EmissionRecordListView,
    approve_record,
    reject_record,
    dashboard_summary,
    AuditLogListView
)

urlpatterns = [
    path('upload/sap/', SAPUploadView.as_view()),
    path('upload/utility/', UtilityUploadView.as_view()),
    path('upload/travel/', TravelUploadView.as_view()),

    path('records/', EmissionRecordListView.as_view()),

    path('records/<int:pk>/approve/', approve_record),
    path('records/<int:pk>/reject/', reject_record),

    path('dashboard/summary/', dashboard_summary),

    path('audit-logs/', AuditLogListView.as_view()),
]