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
        data = Managerdb.objects.filter(username=username_m,password=password_m).values('email','image','playground','id').first()
        request.session['username'] = username_m
        request.session['email'] = data['email']
        request.session['image'] = data['image']
        request.session['password'] = password_m
        request.session['playground'] = data['playground']
        request.session['managerid'] = data['id']
        return redirect('managerindex')
    else:
        return redirect('m_login')

def managerlogout(request):
    del request.session['username']
    del request.session['password']
    del request.session['image']
    del request.session['email']
    del request.session['playground']
    del request.session['managerid']
    return redirect('m_login')