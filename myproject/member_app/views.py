from django.shortcuts import render

# Create your views here.
def member_home(req):
    return render (req,"member_home.html")