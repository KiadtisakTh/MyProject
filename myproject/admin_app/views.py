from django.shortcuts import render
from form_service.models import ModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import user_passes_test



# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
@login_required
def adnin_home(req):
    list_user = ModelForm.objects.all()
    return render(req, "admin_home.html", {"list_user": list_user})

