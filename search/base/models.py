from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

#from base.views import employee

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


# class EmpDetail(models.Model):
#     empno = models.CharField(db_column='EMPNO', unique=True, max_length=6)  # Field name made lowercase.
#     firstnme = models.CharField(db_column='FIRSTNME', max_length=12)  # Field name made lowercase.
#     midinit = models.CharField(db_column='MIDINIT', max_length=10)  # Field name made lowercase.
#     lastname = models.CharField(db_column='LASTNAME', max_length=15)  # Field name made lowercase.
#     workdept = models.CharField(db_column='WORKDEPT', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     phoneno = models.CharField(db_column='PHONENO', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     hiredate = models.DateField(db_column='HIREDATE', blank=True, null=True)  # Field name made lowercase.
#     job = models.CharField(db_column='JOB', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     edlevel = models.SmallIntegerField(db_column='EDLEVEL')  # Field name made lowercase.
#     sex = models.CharField(db_column='SEX', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     birthdate = models.DateField(db_column='BIRTHDATE', blank=True, null=True)  # Field name made lowercase.
#     salary = models.DecimalField(db_column='SALARY', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     bonus = models.DecimalField(db_column='BONUS', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     comm = models.DecimalField(db_column='COMM', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

#     # class Meta:
#     #     managed = False
#     #     db_table = 'EMPLOYEE_DETAIL'
    
#     def __str__(self):
#         return self.firstnme

class EmployeeData (models.Model):
    #host =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    #department =models.ForeignKey(DepartmentData,on_delete=models.CASCADE,null=True)
    employeeid = models.IntegerField(primary_key=True)
    employeename = models.CharField(max_length=20)  # Field name made lowercase.
    departmentid = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        managed = True
        #verbose_name_plural='Employees'# admin page will have table name Employees else django adds its own way
        #unique_together =('employee_name','employee_id')
        #-created descending order 
        ordering=['-updated','-created']
        
        db_table = 'employee'
        
    def __str__(self):
        return self.employeename

# class Dummy:
#     e= EmployeeData()
#     print(e.employee_id)
    
    

class DepartmentData (models.Model):
    # e= EmployeeData()
    # print(e.employee_id)
    # employee_id=e.employee_id
    #user =models.ForeignKey(User,on_delete=models.CASCADE)
    #employee =models.ForeignKey(EmployeeData,on_delete=models.CASCADE,default=1)
    #employee_id = models.CharField(max_length=10,null=True)
    departmentname = models.CharField(max_length=30)  # Field name made lowercase.
    departmentid = models.CharField(max_length=10)
    #departmentid = models.ForeignKey(EmployeeData,on_delete=models.DO_NOTHING)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        #verbose_name_plural='Departments' # admin page will have table name Departments else django adds its own way
        managed = True
        db_table = 'department'
        
    def __str__(self):
        return self.departmentname
    
