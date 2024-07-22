import logging
from django.shortcuts import render , redirect
from form_service.models import ModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import user_passes_test
from admin_app.form import UserService
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
@login_required
def admin_home(req):
    list_user = ModelForm.objects.all().order_by('date_start')
    return render(req, "admin_home.html", {"list_user": list_user})

def admin_member(req):
    list_user = ModelForm.objects.filter(membermodel__status_member=2)
    return render(req, "admin_member.html", {"list_user": list_user})




def admin_detail(req,id):
    order = ModelForm.objects.get(pk=id)
    return render(req,'admin_detail.html',{'order':order})

logger = logging.getLogger(__name__)

def update_status(req, id):
    order = ModelForm.objects.get(pk=id)
    if req.method == "POST":
        order.status = req.POST['status']
        order.save()
        logger.info(f"Order status updated to {order.status} for order ID {id}")

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "admin_orders",
            {
                "type": "order_update",
                "message": f"Order {id} status has been updated."
            }
        )

        async_to_sync(channel_layer.group_send)(
            "user_orders",
            {
                "type": "order_update",
                "message": f"Order {id} status has been updated."
            }
        )

        return redirect("/admin_home")
    
@login_required
def user_service(req,id):
    
    user = ModelForm.objects.get(pk = id)
    if req.method == "POST":
        form = UserService(req.POST,instance=user)
        if form.is_valid():

            form.save()
            
            return redirect("admin_home")

    else:
        form = UserService(instance=user)
    return render(req,"user_service.html",{"form":form , "model_form":user})

    
def admin_delete(req ,id):
    form = ModelForm.objects.get(pk = id)
    form.delete()
    return redirect(admin_home)
        