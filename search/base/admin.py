from django.contrib import admin

# Register your models here.
from .models import DepartmentData, EmployeeData
admin.site.register(EmployeeData)
admin.site.register(DepartmentData)

