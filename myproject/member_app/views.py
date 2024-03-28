from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from member_app.models import MemberModel
from form_service.models import ModelForm
from member_app.form import MemberForm
from web_app.models import User_Profile

# Create your views here.
def member_home(req):
    members = MemberModel.objects.filter(user=req.user)
    for member in members:
        if member.status_member == 2:
            return redirect('member_sucess')  # เปลี่ยน 'member_success' เป็นชื่อ URL ของหน้าที่ต้องการ redirect ไป
    # หากไม่มีสมาชิกที่มีสถานะเป็น 2 ให้ดึงข้อมูลใหม่จากฐานข้อมูล
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
    
def member_form(req):
    if req.method == 'POST':
        form = MemberForm(req.POST)
        if form.is_valid():
            form.save()  # บันทึกข้อมูลลงในฐานข้อมูล
            return redirect('member_sucess')  # แล้ว redirect ไปยังหน้าที่ต้องการหลังจากการส่งแบบฟอร์มสำเร็จ
    else:
        form = MemberForm()
    
    return render(req, 'member_form.html', {'form': form})