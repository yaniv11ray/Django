import re
from django.db import connection
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import EmployeeData,DepartmentData
from .forms import EmployeeForm,DepartmentForm
from django.db.models import Q
from django.contrib.auth import authenticate ,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def loginpage(request):
    print(request)
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password) #remove this later
        user = authenticate(request,username=username,password=password)
        if user is None:
            context ={"error":"Invalid Username password combination , Login Failed !"}
            return render(request,'login.html',context)
        else:
            redirect('home.html')
        login(request,user)
        return redirect('/home')
    print("last call in login page")
    return render(request,'login.html',{})

def logoutpage(request):
    if request.method =="POST":
        logout(request)
        return redirect('/login')
        
    return render(request,'logout.html',{})

def registerpage(request):
    form = UserCreationForm
    print(request.POST)
    if request.method == 'POST':       
        form = UserCreationForm(request.POST)
        print("print form :\n ",form)
        if form.is_valid():
            form.save()
            print("----saved------")
            #context ={"msg":"User created succesfully !"}
            #return HttpResponse("User created succesfully !")
            return redirect('/login')
        else:
            print("----else of form ------")
            context ={
                'error' :form.errors.items
            }
            return render(request,'register.html',context)
        
    
    
    
    return render(request,'register.html',{'form':form})

# empdata =[
#     {'empno':234,'firstnme':'Vinay','midinit':'Ray'},
#     {'empno':324,'firstnme':'John','midinit':'Cena'},
#     {'empno':467,'firstnme':'Kevin','midinit':'Warner'}
# ]
def employee(request):
    print("employee----> in employee method \n")
    # ascending order sort on employeeid
    employees =EmployeeData.objects.all().order_by('employeeid')
    #emp=EmpData.objects.all().values()
    #print("print emp : ",employees)
    context ={
        'employees' : employees
    }
    #print(f'emp data : \n {context}')
    return render(request,'employee.html',context) #{'data' : empdata})

@login_required(login_url='login-page')
def home(request):
    print("----> in home method \n")
    employees =EmployeeData.objects.all() # this is similar to select * from table
    
    departments = DepartmentData.objects.all()
    for department in departments:
        print("department :",department)
    context ={
        'employees':employees,
        'departments':departments
    }
    #return HttpResponse("Home Page")
    return render(request,'home.html',context) # passing dict with key value pairs


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def about(request):
    users = User.objects.values()
    return render(request,'about.html',{'users':users})
  
def result(request):
    print("Form method : ",request.method)
    print("user: ",request.user)
    q = request.GET.get('q')
    q1 = request.POST.get('q')
    print("non stripped : ",q1)
    #q2 = q1.strip()
    #print("stripped : ",q2)
    if request.method == 'POST' :
        
        print("inside post if block :   ",q1)
        cursor = connection.cursor()
        sql =f"SELECT e.employeename,d.departmentname FROM yaniv.employee as e ,yaniv.department as d where e.departmentid=d.departmentid and e.employeeid={q1} ;"
        cursor.execute(sql)
        #data1 = cursor.fetchall()
        #print("--fetched data before \n",data1)
        data = dictfetchall(cursor)
        print("--fetched data after\n",data)
        print("length : ",len(data))
        if len(data) <= 0:
            data =None
    else:
        print("inside else if block : ",q1)
        return render(request,'result.html',{'data' :""})
    
    #print("employees : ",employees)
    print("connection queries: ",connection.queries)
    print("--context data \n",data)
    print("-----------------**********----------------")
   # a=list(data)
    #print(a[0][0])

    context ={
        "data":data
              }
    
    return render(request,'result.html',context)

# def result(request):
#     #print("from result method : ",request.GET.get('q'))
#     #print("from post result method : ",request.POST.get('q'))

#     q = request.GET.get('q')
#     q2 = request.POST.get('q2')
#     print("input : ",q,q2)
#     if request.method=='POST':
#         print("inside post if ")
#         employees =EmployeeData.objects.filter(Q(employeeid=q))
#         print("values :\n",employees.values('employeeid'))
#         departments = DepartmentData.objects.all()
#     else:
#         print("inside post else ")
           
#     #employees =EmployeeData.objects.filter(Q(employeeid=q))
#     #print(employees)
#         employees =EmployeeData.objects.all()
#         departments = DepartmentData.objects.all()
#     #print("*******departments \n",dir(departments))
#     #print(departments.get('_values'))
#     info=zip(employees,departments)
#     # for employee in employees:
#     #     for department in departments:
#     #         if employee in departments:
#     #             print("nested for loop :",employee.employee_id,department.department_id)
#     #print("direct :",employees.employee_id)
#     #print("printning EmployeeData.employee_id: ",EmployeeData.employee_id)
#     # for employee in employees:
#     #     print("EEEID :",employee.employee_id)
    
#     #results=DepartmentData.objects.raw('select e.employee_name,d.department_name from department d,employee e where e.department_id=d.department_id ')
#     #if request.method=="POST":
#     # for department in departments:
#     #     print("department :",department.department_name,department.department_id)
#         #print("EID :",department.employee_id)
#         #print("insideloop")
#     #print("outside loop")
#     context={
#         'info':info,
#     }
#     return render(request,'result.html',context)


def department(request):
    print("----> in department method \n")
    #return HttpResponse("ROOM")
    departments = DepartmentData.objects.all()
    context ={
        "departments" :departments
    }
    #print(f'dept data : \n {context}')
    return render(request,'department.html',context)

def createEmp(request):
    print("createEmp----> in createEmp method")
    form = EmployeeForm()
    print(request.method)
    #print("createEmp****GET Request coming from user \n",request.POST)
    #form = EmployeeForm(request.POST)
    # if form.is_valid():
    #     form.save()
    #     return redirect('employee')
    #uncomment the below later
    if request.method =='POST':
        print("createEmp****POST Request coming from user \n",request.POST)
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/employee')
        
    context={
        'form':form
    }
    print("createEmp----> in createEmp method , just before reutrn \n")
    return render(request,'createEmp.html',context)

def createDept(request):
    form = DepartmentForm()
    if request.method=='POST':
        print("****Department Request coming from user \n",request.POST)
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/department')
        
    context={
        'form':form
    }
    return render(request,'createDept.html',context)

def updateEmp(request,pk):
    print("----> in updateEmp method \n")
    emp = EmployeeData.objects.get(id=pk)
    form = EmployeeForm(instance=emp) 
    if request.method=='POST':
        print("****Request to Update coming from user \n",request.POST)
        form = EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('employee')
    context ={
        'form':form
    }
    return render(request,'form.html',context)

# def updateDept(request,pk):
#     dept = Department.objects.get(id=pk)
#     form = DepartmentForm(instance=dept) 
#     if request.method=='POST':
#         print("****Request to Update coming from user \n",request.POST)
#         form = DepartmentForm(request.POST,instance=dept)
#         if form.is_valid():
#             form.save()
#             return redirect('department')
#     context ={
#         'form':form
#     }
#     return render(request,'form.html',context)

def deleteEmp(request,pk):
    print("----> in deleteEmp method \n")
    emp=EmployeeData.objects.get(id=pk)
    
    form = EmployeeForm(instance=emp)
    if request.method=='POST':
        emp.delete()
        # form=EmployeeForm(request.POST,instance=emp)
        # if form.is_valid():
        #     form.save()
        return redirect('employee')
    
    context={
        'form':form
    }
    return render(request,'delete.html',{'obj':emp})   

# def deleteDept(request,pk):
#     dept=Department.objects.get(id=pk)
    
#     form = DepartmentForm(instance=dept)
#     if request.method=='POST':
#         dept.delete()
#         # form=EmployeeForm(request.POST,instance=emp)
#         # if form.is_valid():
#         #     form.save()
#         return redirect('department')
    
#     context={
#         'form':form
#     }
#     return render(request,'delete.html',{'obj':dept}) 