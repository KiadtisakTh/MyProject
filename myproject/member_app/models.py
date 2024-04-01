from django.db import models
from django.contrib.auth.models import User
from form_service.models import ModelForm


# Create your models here.
ORDER_CHOICE = (
    (1, "สมาชิกรายวัน"),
    (2, "สมาชิกรายเดือน"),
)

class MemberModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    modelform = models.ForeignKey(ModelForm, on_delete=models.CASCADE, null=True)
    status_member = models.IntegerField(choices=ORDER_CHOICE, default=1)
    address_member = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.user)
  
