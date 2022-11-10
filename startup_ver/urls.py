"""startup_ver URL Configuration

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
from django.urls import path,re_path
from django.shortcuts import redirect,render
from django.views.generic import TemplateView
import requests
from .verify import verify_startup


def verifyview(request):
    if request.method=='POST':
        RCnumber=request.POST.get('biz_number')
        print('RCnumber: ',RCnumber)
        CompanyName=request.POST.get('name')
        print("Company Name: ",CompanyName)
        info={
        "rcNumber":RCnumber,
        "companyName":CompanyName,
        "verificationType":'RC-VERIFICATION'
        }

        verify=verify_startup(info)
        print('Verification Status: ',verify)

        if verify['verificationStatus']== 'NOT VERIFIED':
            # Return the failed page
            return redirect('failed_verification')
        else:
            # Return the successful page
            return render(request,'successfulverification.html',{"num":RCnumber,'name':CompanyName})
        
    else:
        return render(request,'startupverification.html')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('quickly_verify_page/',TemplateView.as_view(template_name="quick-verify-page.html"),name="quickly_verify_page"),
    re_path(r'verification-status-positive/?',TemplateView.as_view(template_name='verification-status-positive.html'),name='verification_status_positive'),
    re_path(r'failed_verification/?',TemplateView.as_view(template_name="failedverification.html"),name='failed_verification'),
    re_path(r'home/?',TemplateView.as_view(template_name="index.html"),name="home"),
    re_path(r'investor/registration/?',TemplateView.as_view(template_name="investor.html"),name="investor_registration"),
    re_path(r'signin/?',TemplateView.as_view(template_name="login.html"),name="signin"),
    re_path(r'logindetails/?',TemplateView.as_view(template_name="logindetails.html"),name="logindetails"),
    re_path(r'signup/?',TemplateView.as_view(template_name="registration.html"),name="signup"),
    re_path(r'startupregistration/?',TemplateView.as_view(template_name="startupregistration.html"),name="startupregistration"),
    re_path(r'startupverification/?',verifyview,name="startupverification"),
    re_path(r'successfulverification/?',TemplateView.as_view(template_name="successfulverification.html"),name="successfulverification"),
    re_path(r'welcome/?',TemplateView.as_view(template_name="homepage.html"),name="homepage"),
]
