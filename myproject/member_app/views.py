from django.shortcuts import render

from member_app.models import MemberModel
from form_service.models import ModelForm

# Create your views here.
def member_home(request):
    member_models = MemberModel.objects.all()
    return render(request, "member_home.html", {'member_models': member_models})
