from django.urls import path 
from . import views
urlpatterns = [
    path('drprofile/', views.drprofile ,name = "drprofile"),
    path('departments/', views.departments ,name = "departments"),
    path('sendmail/', views.sendmail ,name = "sendmail"),
    path('qrcode/', views.qrcode ,name = "qrcode"),
    path('takevideo/', views.takevideo ,name = "takevideo"),
]
