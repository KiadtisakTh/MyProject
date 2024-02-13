from django.shortcuts import render

# Create your views here.
def service_user(req):
    return render(req,"service.html")