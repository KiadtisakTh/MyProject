from django.urls import path , include
from web_app import views
from .views import *

urlpatterns = [
    path("",views.index , name="home"),
    path("about",views.about , name="about"),
    path("contact",views.contact , name="contact"),
    path('user_profile/',views.user_profile, name='user_profile'),
    path('update_profile_image/', update_profile_image, name='update_profile_image'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]