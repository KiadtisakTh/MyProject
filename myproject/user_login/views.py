from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib.auth import logout
from django.contrib import auth
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(req):
    if req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]
        if username == "" or password=="":
            return redirect("/login")
        else:
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(req,user)
                return redirect('/')
            else:
                messages.error(req,"username หรือ รหัสผ่าน ไม่ถูกต้อง!")
                return redirect('/login')
    return render(req,'login.html')


def user_register(req):
    form = Register()
    if req.method == "POST":
         form = Register(req.POST)
         if form.is_valid():
            form.save()
            messages.success(req,"สร้างบัญชีสำเร็จ")
            return redirect("/")
         else:
             messages.error(req,"สร้างบัญชีไม่สำเร็จ")
             form = Register()
             return redirect("register")
             
    return render(req, 'Register.html',{"form":form})


def user_logout(req):
        logout(req)
        # Redirect to a success page.
        return redirect("/")

@login_required
def edituser_profile(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = UserprofileForm(request.POST, instance=user_profile)
        if form.is_valid():
            user_profile.save()
            messages.success(request, 'บันทึกข้อมูลเรียบร้อยแล้ว')
            return redirect('/')
        else:
            messages.error(request, 'กรุณากรอกข้อมูลที่ถูกต้อง')
    else:
        form = UserprofileForm(instance=user_profile)
    return render(request, 'app/user_profile.html', {'form': form})

@login_required
def user_profile(req):
    return render(req, 'user_profile.html', {'user': req.user})
        