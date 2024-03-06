from django.urls import path 
from .views import *
from admin_app import views

urlpatterns = [
    path("admin_home",views.adnin_home , name="admin_home"),
    path("admin_order",views.admin_order , name="admin_order"),
    path("admin_home/admin_order/<int:id>",views.admin_order,name="admin_order"),
    path("admin_home/admin_detail/<int:id>",views.admin_detail,name="admin_detail"),
    path("admin_home/update/<int:id>",views.update_status,name="status_update"),
]