from django.shortcuts import render


def engprofile(request):
    return render(request,'englevel/engprofile.html')

def notifications(request):
    return render(request,'englevel/notifications.html')

def engdepartments(request):
    return render(request,'englevel/engdepartments.html')

def equipments(request):
    return render(request,'englevel/equipments.html')

def workorder(request):
    return render(request,'englevel/workorder.html')

def connectwithcompany(request):
    return render(request,'englevel/connectwithcompany.html')

def esendmail(request):
    return render(request,'englevel/esendmail.html')

def eaddequipment(request):
    return render(request,'englevel/eaddequipment.html')

def assignedequipment(request):
    return render(request,'englevel/assigned-equipment.html')

