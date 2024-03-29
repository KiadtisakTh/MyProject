from django.urls import path

from member_app import views 

urlpatterns = [
    path("member_home",views.member_home , name="member_home"),
    path('membership/', views.membership, name='membership'),
    path('member_form' , views.member_form , name="member_form"),
    path('member_sucess' , views.member_sucess , name="member_sucess"),
     path('cancel_monthly_subscription/', views.cancel_monthly_subscription, name='cancel_monthly_subscription'),
    

]