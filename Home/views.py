from django.shortcuts import render,HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,'login.html')

def forget(request):
    return render(request,'Forget.html')

def profile(request):
    return render(request,'Profile.html')


def about(request):
    return HttpResponse("this is aboutpage")

