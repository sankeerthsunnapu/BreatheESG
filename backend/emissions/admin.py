from django.contrib import admin
from .models import *

admin.site.register(Company)
admin.site.register(DataSource)
admin.site.register(RawUpload)
admin.site.register(EmissionRecord)
admin.site.register(AuditLog)