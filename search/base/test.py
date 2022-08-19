from base.models import EmpData

a=EmpData.objects.all()
print(a)
print(EmpData.objects.first())