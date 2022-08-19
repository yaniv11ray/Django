from django.urls import path
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse

from . import views
#from search.views import loginPage,logoutPage,registerPage


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.loginpage),
    path('department/',views.department,name='department'),
    path('home/', views.home, name="home"),
    path('login/',views.loginpage,name='login-page'),
    path('logout/',views.logoutpage,name='logout-page'),
    path('register/',views.registerpage,name='resgister-page'),
    #path('department/',views.department,name="department"),
    path('employee/', views.employee,name="employee"),
    #path('createEmployee/', views.createEmp,name="create-employee"),
    path('result/', views.result,name="result"),
    path('about/', views.about,name="about"),
    path('createEmployee/', views.createEmp,name="create-employee"),
    path('updateEmployee/<str:pk>/', views.updateEmp,name="update-employee"),
    path('deleteEmployee/<str:pk>/', views.deleteEmp,name="delete-employee"),
    
    path('createDepartment/', views.createDept,name="create-Department")
    # path('updateDepartment/<str:pk>/', views.updateDept,name="update-Department"),
    # path('deleteDepartment/<str:pk>/', views.deleteDept,name="delete-Department"),


]