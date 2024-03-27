from django.db import models
from django.contrib.auth.models import User
from form_service.models import ModelForm


# Create your models here.
ORDER_CHOICE = (
    ("1","สมาชิกรายวัน"),
    ("2","สมาชิกรายเดือน"),
 
)

class MemberModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , null = True)
    status_member = models.CharField(max_length=255,choices=ORDER_CHOICE,default=1)
    price = models.CharField(max_length=20)


       
