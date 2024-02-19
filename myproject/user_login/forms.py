from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user_login.models import User_Profile

class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',"first_name","last_name","email" ,"password1","password2"]

class UserprofileForm(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']

