from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib.auth import logout
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate

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
                return redirect('/login')
    return render(req,'login.html')


def user_register(req):
    email = "email"  # กำหนดค่า email เริ่มต้น
    if req.method == "POST":
        username = req.POST.get("username", "")
        email = req.POST.get("email", email)  # ใช้ค่า email เริ่มต้นในกรณีไม่มีค่าใน req.POST
        password = req.POST.get("password", "")
        password2 = req.POST.get("password2", "")
        if username == '' or email == '' or password == '' or password2 == '':
            return redirect("/register")
        elif password != password2:
            return redirect("/register")
        else:
            if User.objects.filter(username=username).exists():
                return redirect("/register")
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                )
                user.save()
                messages.success(req,"สร้างบันชีสำเร็จ")
                return redirect("/")
    return render(req, 'Register.html')


    



def user_logout(req):
        logout(req)
        # Redirect to a success page.
        return redirect("/")