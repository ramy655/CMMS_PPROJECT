from django.urls import path 
from . import views
urlpatterns = [
    path('',views.home,name="homep"),
    path('about/',views.about,name="aboutp"),
    path('signup/',views.signup,name="signup"),
    
]