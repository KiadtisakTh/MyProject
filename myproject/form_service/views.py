from django.shortcuts import render , redirect
from form_service.models import ModelForm
from form_service.form import UserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from web_app.models import User_Profile


# Create your views here.
@login_required
def service_user(req):
    if req.method == "POST":
        user_model = ModelForm.objects.create(
            first_name = req.POST.get('first_name'),
            last_name=req.POST.get('last_name'),
            email=req.POST.get('email'),
            phone_number=req.POST.get('phone_number'),
            Laundry=req.POST.get('Laundry'),
            date_start=req.POST.get('date_start'),
            date_end=req.POST.get('date_end'),
            clothes=req.POST.get('clothes'),
            number_clothes=req.POST.get('number_clothes'),
            number_baskets=req.POST.get('number_baskets'),
            note=req.POST.get('note'),
        )
        # Save the instance to the database
        user_model.save()
        # Redirect to a success page or do something else
        return redirect('table_list')
    else:
        form = UserForm()
    return render(req,"service.html" ,{"form":form})

@login_required
def edit_service(req,id):
    
    user = ModelForm.objects.get(pk = id)
    if req.method == "POST":
        form = UserForm(req.POST,instance=user)
        if form.is_valid():

            form.save()
            messages.success(req,"เเก้ไขข้อมูลสำเร็จ")
            return redirect("/")

    else:
        form = UserForm(instance=user)
    return render(req,"edit_service.html",{"form":form , "model_form":user})

@login_required
def table_list(req):
    model_form = ModelForm.objects.filter(first_name=req.user.first_name)
    return render(req, "table_list.html", {"model_form": model_form})

def delete(req,id):
    form = ModelForm.objects.get(pk = id)
    form.delete()
    messages.success(req,"ลบข้อมูลสำเร็จ")
    return redirect(table_list)