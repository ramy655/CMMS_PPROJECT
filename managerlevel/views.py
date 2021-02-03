from django.shortcuts import render , redirect ,get_list_or_404
from .models import *
from .forms import DepartmentForm , EquipmentForm
# Create your views here.

def mprofile(request):
    return render(request,'managerlevel/mprofile.html')

def mnotifications(request):
    return render(request,'managerlevel/mnotifications.html')

def users(request):
    return render(request,'managerlevel/users.html')

def mdepartments(request):
    context = {
        'departments' : Departments.objects.all(),
    }
    return render(request,'managerlevel/mdepartments.html',context)

def mequipments(request):
    med = {
        'medical': Medicaldevice.objects.all(),
    }
    return render(request,'managerlevel/mequipments.html',med)

def mworkorder(request):
    context = {
        'workorder' : Workorder.objects.all(),
    }
    return render(request,'managerlevel/mworkorder.html',context)

def sendworkorder(request):
    return render(request,'managerlevel/sendworkorder.html')

def mconnectwithcompany(request):
    return render(request,'managerlevel/mconnectwithcompany.html')

def msendemail(request):
    return render(request,'managerlevel/msendemail.html')

def adduser(request):
    return render(request,'managerlevel/add-user.html')

def allworkorders(request):
    return render(request,'managerlevel/allworkorders.html')

def adddepartment(request):

    if request.method == 'POST':
        add_department =  DepartmentForm(request.POST , request.FILES)
        if add_department.is_valid():
            add_department.save()
            return redirect('mdepartments')


    x = {
        'form_department' : DepartmentForm(),
    }
    return render(request,'managerlevel/add-department.html',x)

def addequipment(request):

    if request.method == 'POST':
        add_equipment =  EquipmentForm(request.POST , request.FILES)
        if add_equipment.is_valid():
            add_equipment.save()
            return redirect('mequipments')
    y = {
        'form_equipment' : EquipmentForm(),
    }
    return render(request,'managerlevel/add-equipment.html',y)

def staffresponse(request):
    return render(request,'managerlevel/staff-response.html')

def update(request, id):
    equipment_id = Medicaldevice.objects.get(id = id)
    if request.method == 'POST':
        save_equipment =  EquipmentForm(request.POST , request.FILES, instance= equipment_id)
        if save_equipment.is_valid():
            save_equipment.save()
            return redirect('mequipments')
    else:
        save_equipment =  EquipmentForm(instance= equipment_id)
    context = {
        'form' : save_equipment
    }

    return render(request,'managerlevel/update.html',context)

def delete(request, id):
    equipment_delete = Medicaldevice.objects.get(id = id)
    if request.method == 'POST':
        equipment_delete.delete()
        return redirect('mequipments')
    
    return render(request,'managerlevel/delete.html')

