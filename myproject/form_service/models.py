from django.db import models

# Create your models here.
class ModelForm(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(null = True)
    phone_number = models.CharField(max_length = 100,null=True, blank=True)
    Laundry = models.CharField(max_length = 100)
    date_start = models.DateField()
    date_end = models.DateField()
    clothes = models.CharField(max_length = 100)
    number_baskets = models.IntegerField(default = 0)
    note = models.CharField(max_length = 100)
