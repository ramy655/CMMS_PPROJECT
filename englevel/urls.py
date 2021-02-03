from django.urls import path 
from . import views
urlpatterns = [
    path('engprofile/', views.engprofile ,name = "engprofile"),
    path('notifications/', views.notifications ,name = "notifications"),
    path('engdepartments/', views.engdepartments ,name = "engdepartments"),
    path('equipments/', views.equipments ,name = "equipments"),
    path('', views.workorder ,name = "workorder"),
    path('connectwithcompany/', views.connectwithcompany ,name = "connectwithcompany"),
    path('esendmail/', views.esendmail ,name = "esendmail"),
    path('eaddequipment/', views.eaddequipment ,name = "eaddequipment"),
    path('assignedequipment/', views.assignedequipment ,name = "assignedequipment"),

]
