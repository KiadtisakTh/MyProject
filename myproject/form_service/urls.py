from django.urls import path

from form_service import views 



urlpatterns = [
    path("service",views.service_user , name="service"),
    path("table_list",views.table_list , name="table_list"),
    
]