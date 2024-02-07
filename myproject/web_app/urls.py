from django.urls import path , include
from web_app import views

urlpatterns = [
    path("",views.index , name="home"),
]