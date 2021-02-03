from django.db import models
from managerlevel.models import Departments , User
#from django.utils import timezone
#from django.contrib.auth.models import User
# Create your models here.

class Medicaldevice(models.Model):
    
    
    name = models.CharField(max_length=250)
    serial_number =models.CharField(max_length=250)
    location = models.CharField(max_length=250,null= True , blank= True)
    manufacture = models.CharField(max_length=250,null= True , blank= True)
    country = models.CharField(max_length=250,null= True , blank= True)
    model_device = models.CharField(max_length=250,null= True , blank= True)
    #time = models.TimeField(default=timezone.now) 
    #doctor = models.ForeignKey(User , on_delete=models.PROTECT)

    def __str__(self):
        return self.name

#class Workorder(models.Model):
    
    #Equipment = models.ForeignKey(Medicaldevice , on_delete=models.PROTECT ,null= True , blank= True)
    #Department = models.ForeignKey(Departments , on_delete=models.PROTECT ,null= True , blank= True)
    #Case = models.BooleanField(max_length=250,null= True , blank= True)
    #Assigned_to = models.ForeignKey(User , on_delete=models.PROTECT ,null= True , blank= True)
    #Time_Response = models.TimeField(null= True , blank= True)
    #time = models.TimeField(default=timezone.now) 
    #doctor = models.ForeignKey(User , on_delete=models.PROTECT)
    #Department_of_device = models.ForeignKey(Departments , on_delete=models.PROTECT ,null= True , blank= True)
    