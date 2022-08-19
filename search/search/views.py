# from django.db import connection
# from django.shortcuts import render,redirect
# from django.http import HttpResponse
#from base.models import EmployeeData,DepartmentData
#from base.forms import EmployeeForm,DepartmentForm
#from django.db.models import Q
# from django.contrib.auth import authenticate ,login,logout

# def loginPage(request):
#     if request.method =="POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         print(username,password) #remove this later
#         user = authenticate(request,username=username,password=password)
#         if user is None:
#             context ={"error":"Invalid Username password combination , Login Failed !"}
#             return render(request,'login.html',context)
#         else:
#             redirect('home.html')
#         login(request,user)
#         return redirect('/home')
    
#     return render(request,'login.html',{})

# def logoutPage(request):
#     if request.method =="POST":
#         logout(request)
#         return redirect('/login')
        
#     return render(request,'logout.html',{})

# def registerPage(request):
#     return render(request,'register.html',{})