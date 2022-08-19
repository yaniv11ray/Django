"""search URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
#from .views import loginPage ,registerPage,logoutPage
from base import views
#from base.views import home,department,result,about,employee,updateEmp,deleteEmp


admin.AdminSite.site_header="Login to Yaniv Admin Page"
admin.AdminSite.site_title="Welcome to Admin Page of Yaniv"
admin.AdminSite.index_title="Welcome to Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls'))
    # path('login/',loginPage,name='login-page'),
    # path('logout/',logoutPage,name='logout-page'),
    # path('register/',registerPage,name='resgister-page')
    # path('home', home),
    # path('department/', department,name="department"),
    # path('employee/', views.employee,name="employee"),
    # path('result/', views.result,name="result"),
    # path('about/', views.about,name="about"),
    # path('createEmployee/', views.createEmp,name="create-employee"),
    # path('updateEmployee/<str:pk>/', views.updateEmp,name="update-employee"),
    # path('deleteEmployee/<str:pk>/', views.deleteEmp,name="delete-employee")   

]
