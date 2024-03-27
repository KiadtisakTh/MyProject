from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from member_app.models import MemberModel
from form_service.models import ModelForm
from web_app.models import User_Profile

# Create your views here.
def member_home(req):
     members = MemberModel.objects.filter(user = req.user)
     return render(req, 'member_home.html', {'members': members})



def upgrade_membership(request):
    try:
        member = MemberModel.objects.get(user=request.user)
    except MemberModel.DoesNotExist:
        # สร้างอินสแตนซ์ MemberModel ใหม่สำหรับผู้ใช้ปัจจุบัน
        member = MemberModel.objects.create(user=request.user, status_member="2")
    
    if request.method == "POST":
        # อัปเดตสถานะเป็น "สมาชิกรายเดือน"
        member.status_member = "2"
        member.save()
        return redirect('user_profile')  # เปลี่ยนเส้นทางไปยังหน้าสำเร็จ
        
    else:
        # จัดการคำขอ GET ตามที่จำเป็น
        return render(request, 'member_home.html', {'member': member})
    
def name(req):
    return render(req ,'name.html')