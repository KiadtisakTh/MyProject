from django.shortcuts import render , redirect
from form_service.models import ModelForm
from form_service.form import UserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def service_user(req):
    if req.method == "POST":
        #รับข้อมูล
        form = UserForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # Create an instance of your model with data from the form
            user_model = ModelForm(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                number=form.cleaned_data['number'],
                Laundry=form.cleaned_data['Laundry'],
                date_start=form.cleaned_data['date_start'],
                date_end=form.cleaned_data['date_end'],
                clothes=form.cleaned_data['clothes'],
                number_baskets=form.cleaned_data['number_baskets'],
                note=form.cleaned_data['note'],
            )
            # Save the instance to the database
            user_model.save()
            # Redirect to a success page or do something else
            return redirect('/')
    else:
        form = UserForm()
    return render(req,"service.html" ,{"form":form})

@login_required
def table_list(req):
    if req.user.is_superuser:
        model_form =  ModelForm.objects.all()
    else:
        model_form = ModelForm.objects.filter(first_name=req.user.first_name)
    return render(req, "table_list.html", {"model_form": model_form})