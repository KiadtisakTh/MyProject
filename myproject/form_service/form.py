from django import forms

from form_service.models import ModelForm



class UserForm(forms.ModelForm):
    class Meta:
        model = ModelForm
        fields = ['first_name', 'last_name','email','number','Laundry','date_start','date_end','clothes','number_baskets','note']