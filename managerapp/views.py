from django.shortcuts import render,redirect
from admin_eturf.models import *

# Create your views here.

def managerindex(request):
    return render(request,'managerindex.html')

def m_login(request):
    return render(request,'managerlogin.html')

def managerlogin(request):
    username_m = request.POST.get('username')
    password_m = request.POST.get('password')
    if Managerdb.objects.filter(username=username_m,password=password_m).exists():
        return redirect('managerindex')
    else:
        return redirect('m_login')

def managerlogout(request):
    return redirect('m_login')