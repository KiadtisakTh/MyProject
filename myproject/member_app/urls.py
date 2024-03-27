from django.urls import path

from member_app import views 

urlpatterns = [
    path("member_home",views.member_home , name="member_home"),
    path('upgrade-membership/', views.upgrade_membership, name='upgrade_membership'),
    path('name' , views.name , name="name")
    

]