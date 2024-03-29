from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from member_app.models import MemberModel
from form_service.models import ModelForm
from member_app.form import MemberForm
from web_app.models import User_Profile

# Create your views here.
def member_home(req):
    members = MemberModel.objects.filter(user=req.user)
    for member in members:
        if member.status_member == 2:
            return redirect('member_sucess')  
    members = MemberModel.objects.filter(user=req.user)
    return render(req, 'member_home.html', {'members': members})


def member_sucess(req):
     return render(req, 'member_sucess.html')



def membership(request):
    try:
        member = MemberModel.objects.get(user=request.user)
    except MemberModel.DoesNotExist:
        member = MemberModel.objects.create(user=request.user, status_member="2")

    if request.method == "POST":
        member.status_member = "2"
        member.save()
        return redirect('member_form') 
        
    else:
        
        return render(request, 'member_home.html', {'member': member})
    
def member_form(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            # ดึงข้อมูลผู้ใช้ที่ลงทะเบียนอยู่
            user = request.user
            # สร้าง MemberModel object โดยใช้ข้อมูลจากแบบฟอร์ม
            member = form.save(commit=False)  # ไม่บันทึกลงในฐานข้อมูลก่อน
            member.user = user  # เชื่อมโยงกับผู้ใช้
            member.save()  # บันทึกลงในฐานข้อมูล
            return redirect('member_success')  # แล้ว redirect ไปยังหน้าที่ต้องการหลังจากการส่งแบบฟอร์มสำเร็จ
    else:
        form = MemberForm()
    
    return render(request, 'member_form.html', {'form': form})


def cancel_monthly_subscription(request):
    if request.method == 'POST':
        member = MemberModel.objects.get(user=request.user)
        member.status_member = 1
        member.save()
        return redirect('user_profile')  