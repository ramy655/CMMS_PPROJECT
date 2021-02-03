from django.contrib import admin
from .models import Medicaldevice , Departments , Workorder

# Register your models here.

admin.site.register(Medicaldevice)
admin.site.register(Departments)
admin.site.register(Workorder)