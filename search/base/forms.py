from django.forms import ModelForm
from .models import EmployeeData,DepartmentData

class EmployeeForm(ModelForm):
    class Meta:
        model=EmployeeData
        fields='__all__'

class DepartmentForm(ModelForm):
    class Meta:
        model=DepartmentData
        fields='__all__'