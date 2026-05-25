from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DataSource(models.Model):
    SOURCE_TYPES = [
        ('SAP', 'SAP'),
        ('UTILITY', 'Utility'),
        ('TRAVEL', 'Travel'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    source_type = models.CharField(max_length=20, choices=SOURCE_TYPES)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.company.name} - {self.source_type}"


class RawUpload(models.Model):
    source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    original_filename = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_filename


class EmissionRecord(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    SCOPE_CHOICES = [
        ('SCOPE_1', 'Scope 1'),
        ('SCOPE_2', 'Scope 2'),
        ('SCOPE_3', 'Scope 3'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    source = models.ForeignKey(DataSource, on_delete=models.CASCADE)

    activity_type = models.CharField(max_length=255)
    scope = models.CharField(max_length=20, choices=SCOPE_CHOICES)

    quantity = models.FloatField()
    unit = models.CharField(max_length=50)

    normalized_quantity = models.FloatField(null=True, blank=True)
    normalized_unit = models.CharField(max_length=50, default='kgCO2e')

    emission_factor = models.FloatField(null=True, blank=True)
    emission_value = models.FloatField(null=True, blank=True)

    record_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    suspicious_flag = models.BooleanField(default=False)
    validation_message = models.TextField(blank=True, null=True)

    source_row_id = models.CharField(max_length=255, blank=True, null=True)

    locked = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity_type} - {self.emission_value}"


class AuditLog(models.Model):
    emission_record = models.ForeignKey(
        EmissionRecord,
        on_delete=models.CASCADE
    )

    field_name = models.CharField(max_length=255)

    old_value = models.TextField(null=True, blank=True)
    new_value = models.TextField(null=True, blank=True)

    edited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    edited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.field_name} changed"