from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(req):
    
    return render(req,"index.html")


@login_required
def about(req):
    return render(req,"about.html")