from django.urls import path

from form_service import views 



urlpatterns = [
    path("service",views.service_user , name="service"),
    
]