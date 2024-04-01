from django.urls import path

from member_app import views 

urlpatterns = [
    path("member_home",views.member_home , name="member_home"),
    path('membership/', views.membership, name='membership'),
    path('member_form' , views.member_form , name="member_form"),
    path('member_success' , views.member_success , name="member_success"),
     path('cancel_monthly_subscription/', views.cancel_monthly_subscription, name='cancel_monthly_subscription'),
    

]