from django.http import HttpResponse
from django.shortcuts import redirect, render
from admin_eturf.models import *
from . models import *
from django.contrib import messages

# Create your views here.

def eturf_index(request):
    data = Playgrounddb.objects.all()
    return render(request,'eturf_index.html',{'data':data})

def eturf_list(request):
    data = Playgrounddb.objects.all()
    return render(request,'eturf_list.html',{'data':data})

def booknow(request,turfid):
    data = Playgrounddb.objects.filter(id=turfid)
    return render(request,'booknow.html',{'data':data})

def bookdata(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        date = request.POST.get('date')
        ground = request.POST.get('ground')
        price = request.POST.get('price')
        if Bookdb.objects.filter(start_time=start_time,end_time=end_time,date=date,ground=ground,price=price).exists():
            messages.error(request,'Already booked!!!')
        else:
            data = Bookdb(userid=Userdb.objects.get(id=userid),start_time=start_time,end_time=end_time,date=date,ground=ground,price=price)
            data.save()
    return redirect('eturf_index')

def userregister(request):
    return render(request,'userregister.html')

def u_register(request):
    if request.method == 'POST':
        username_u = request.POST.get('username')
        password_u = request.POST.get('password')
        email_u = request.POST.get('email')
        if Userdb.objects.filter(email=email_u):
            return HttpResponse('Email Already exists')
        mobile_u = request.POST.get('mobile')
        data = Userdb(username=username_u,password=password_u,email=email_u,mobile=mobile_u)
        data.save()
    return redirect('eturf_index')

def userlogin(request):
    username_u = request.POST.get('username')
    password_u = request.POST.get('password')
    if Userdb.objects.filter(username=username_u,password=password_u).exists():
        data = Userdb.objects.filter(username=username_u,password=password_u).values('email','mobile','id').first()
        request.session['username_u'] = username_u
        request.session['email'] = data['email']
        request.session['mobile'] = data['mobile']
        request.session['password_u'] = password_u
        request.session['userid'] = data['id']
        return redirect('eturf_index')
    else:
        messages.error(request,'Sorry invalid user credentials!!!')
        return redirect('eturf_index')

def userlogout(request):
    del request.session['username_u']
    del request.session['password_u']
    del request.session['email']
    del request.session['mobile']
    del request.session['userid']
    return redirect('eturf_index')