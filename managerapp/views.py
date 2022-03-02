from django.shortcuts import render,redirect
from admin_eturf.models import *
from eturf_web.models import *

# Create your views here.

def managerindex(request):
    ground = request.session.get('playground')
    bcount = Bookdb.objects.filter(ground=ground).count()
    return render(request,'managerindex.html',{'bcount':bcount})

def booking_history(request):
    ground = request.session.get('playground')
    bcount = Bookdb.objects.filter(ground=ground).count()
    ground = request.session.get('playground')
    data = Bookdb.objects.filter(ground=ground)
    return render(request,'booking_history.html',{'data':data,'bcount':bcount})

def m_login(request):
    return render(request,'managerlogin.html')

def managerlogin(request):
    username_m = request.POST.get('username')
    password_m = request.POST.get('password')
    if Managerdb.objects.filter(username=username_m,password=password_m).exists():
        data = Managerdb.objects.filter(username=username_m,password=password_m).values('email','image','playground','id').first()
        request.session['username_m'] = username_m
        request.session['email_m'] = data['email']
        request.session['image'] = data['image']
        request.session['password_m'] = password_m
        request.session['playground'] = data['playground']
        request.session['managerid'] = data['id']
        return redirect('managerindex')
    else:
        return redirect('m_login')

def managerlogout(request):
    del request.session['username_m']
    del request.session['password_m']
    del request.session['image']
    del request.session['email_m']
    del request.session['playground']
    del request.session['managerid']
    return redirect('m_login')