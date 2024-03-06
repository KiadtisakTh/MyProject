from django.db import models

# Create your models here.

    
ORDER_CHOICE = (
    ("1","เสร็จเเล้ว"),
    ("2","ยังไม่เสร็จ"),
    ("3","รอการส่งซัก"),
    ("4","ยกเลิก"),
 
)
class ModelForm(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(null = True)
    phone_number = models.CharField(max_length = 100,null=True, blank=True)
    Laundry = models.CharField(max_length = 100)
    date_start = models.DateField()
    date_end = models.DateField()
    clothes = models.CharField(max_length = 100)
    number_clothes = models.CharField(max_length = 100 , null = True)
    number_baskets = models.CharField(max_length = 100 , null = True)
    note = models.CharField(max_length = 100)
    status = models.CharField(max_length=255,choices=ORDER_CHOICE,default=3)
    

