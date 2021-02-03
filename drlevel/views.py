from django.shortcuts import render
from .models import Medicaldevice
# Create your views here.

def drprofile(request):
    return render(request,'drlevel/profile.html')

def departments(request):
    context = {
        'medicaldevice' : Medicaldevice.objects.all(),
    }
    return render(request,'drlevel/departments.html',context)

def sendmail(request):
    return render(request,'drlevel/sendmail.html')

def qrcode(request):
    return render(request,'drlevel/qrcode.html')

def takevideo(request):
    
    return render(request,'drlevel/takevideo.html')