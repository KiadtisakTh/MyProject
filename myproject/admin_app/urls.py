from django.urls import path 
from .views import *
from admin_app import views

urlpatterns = [
    path("admin_home",views.admin_home , name="admin_home"),
    path("admin_member",views.admin_member , name="admin_member"),
    path("admin_order",views.admin_order , name="admin_order"),
    path("admin_home/admin_order/<int:id>",views.admin_order,name="admin_order"),
    path("admin_home/admin_detail/<int:id>",views.admin_detail,name="admin_detail"),
    path("admin_home/update/<int:id>",views.update_status,name="status_update"),
    path("admin_delete/<int:id>",views.admin_delete ,name='delete'),
    path("user_service/<int:id>",views.user_service ,name="user_service"),
]