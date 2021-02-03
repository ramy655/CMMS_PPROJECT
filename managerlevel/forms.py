from django import forms
from .models import Departments, Medicaldevice

class DepartmentForm(forms.ModelForm):
    class Meta:
        model =  Departments

        fields = ['name']

        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'})
               }

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Medicaldevice

        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'serial_number' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'location' : forms.TextInput(attrs={'class' : 'form-control'}),
            'manufacture' : forms.TextInput(attrs={'class' : 'form-control'}),
            'country' : forms.TextInput(attrs={'class' : 'form-control'}),
            'model_device' : forms.TextInput(attrs={'class' : 'form-control'}),
            'Department_of_device' : forms.Select(attrs={'class' : 'form-control'}),
            # photo = forms.FileInput(attrs={'class' : 'form-control'})
               }




