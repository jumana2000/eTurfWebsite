import email
from django.http import HttpResponse
from django.shortcuts import redirect, render
from admin_eturf.models import *
from . models import *

# Create your views here.

def eturf_index(request):
    data = Playgrounddb.objects.all()
    return render(request,'eturf_index.html',{'data':data})

def eturf_list(request):
    data = Playgrounddb.objects.all()
    return render(request,'eturf_list.html',{'data':data})

def booknow(request):
    return render(request,'booknow.html')

def userregister(request):
    return render(request,'userregister.html')

def u_register(request):
    if request.method == 'POST':
        username_u = request.POST.get('username')
        password_u = request.POST.get('password')
        email_u = request.POST.get('email')
        if Userdb.objects.filter(email=email_u).exists():
            return HttpResponse('Email Already exists')
        mobile_u = request.POST.get('mobile')
        data = Userdb(username=username_u,password=password_u,email=email_u,mobile=mobile_u)
        data.save()
    return redirect('eturf_index')