from django.urls import path 
from . import views
urlpatterns = [

    path('mprofile/', views.mprofile ,name = "mprofile"),
    path('mnotifications/', views.mnotifications ,name = "mnotifications"),
    path('users/', views.users ,name = "users"),
    path('mdepartments/', views.mdepartments ,name = "mdepartments"),
    path('mequipments/', views.mequipments ,name = "mequipments"),
    path('mworkorder/', views.mworkorder ,name = "mworkorder"),
    path('sendworkorder/', views.sendworkorder ,name = "sendworkorder"),
    path('mconnectwithcompany/', views.mconnectwithcompany ,name = "mconnectwithcompany"),
    path('msendemail/', views.msendemail ,name = "msendemail"),
    path('adduser/', views.adduser ,name = "adduser"),
    path('allworkorders/', views.allworkorders ,name = "allworkorders"),
    path('add-department/', views.adddepartment ,name = "adddepartment"),
    path('add-equipment/', views.addequipment ,name = "addequipment"),
    path('staff-response/', views.staffresponse ,name = "staffresponse"),
    path('update/<int:id>', views.update ,name = "update"),
    path('delete/<int:id>', views.delete ,name = "delete"),

]
