from django.shortcuts import render , redirect
from form_service.models import ModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import user_passes_test



# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
@login_required
def adnin_home(req):
    list_user = ModelForm.objects.all()
    return render(req, "admin_home.html", {"list_user": list_user})


def admin_order(req):
    order = ModelForm.objects.all()
    return render(req,'admin_order.html',{'list_order':order})

def admin_detail(req,id):
    order = ModelForm.objects.get(pk=id)
    return render(req,'admin_detail.html',{'order':order})

def update_status(req,id):
    order = ModelForm.objects.get(pk=id)
    if req.method == "POST":
        order.status = req.POST['status']
        order.save()
        return redirect("/admin_home/admin_order")
        