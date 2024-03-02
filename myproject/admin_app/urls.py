from django.urls import path 
from .views import *
from admin_app import views

urlpatterns = [
    path("admin_home",views.adnin_home , name="admin_home"),
]