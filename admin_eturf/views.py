from django.shortcuts import redirect, render
from admin_eturf.models import Categorydb, Managerdb, Playgrounddb
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from eturf_web.models import *

# Create your views here.

def adminindex(request):
    return render(request,'adminindex.html')

def addcategory(request):
    return render(request,'addcategory.html')

def catdata(request):
    if request.method == 'POST':
        name_c = request.POST.get('name')
        file_c = request.FILES['file']
        data = Categorydb(name=name_c,file=file_c)
        data.save()
    return redirect('viewcategory')

def viewcategory(request):
    data = Categorydb.objects.all()
    return render(request,'viewcategory.html',{'data':data})

def addplaygrounds(request):
    data = Categorydb.objects.all()
    return render(request,'addplaygrounds.html',{'data':data})

def playground_data(request):
    if request.method == 'POST':
        ground_name = request.POST.get('name')
        location_p = request.POST.get('location')
        category_p = request.POST.get('category')
        price_p = request.POST.get('price')
        img_p = request.FILES['img']
        data = Playgrounddb(ground=ground_name,location=location_p,category=category_p,price=price_p,img=img_p)
        data.save()
    return redirect('addplaygrounds')

def viewplayground(request):
    data = Playgrounddb.objects.all()
    return render(request,'viewplayground.html',{'data':data})

def addmanagers(request):
    data = Playgrounddb.objects.all()
    return render(request,'addmanagers.html',{'data':data})

def managerdata(request):
    if request.method == 'POST':
        username_m = request.POST.get('username')
        password_m = request.POST.get('password')
        email_m = request.POST.get('email')
        ground = request.POST.get('ground')
        img_m = request.FILES['img']
        data = Managerdb(username=username_m,password=password_m,email=email_m,image=img_m,playground=ground)
        data.save()
    return redirect('viewmanager')

def viewmanager(request):
    data = Managerdb.objects.all()
    return render(request,'viewmanager.html',{'data':data})

def message(request):
    data = Contactdb.objects.all()
    return render(request,'message.html',{'data':data})

def ad_login(request):
    return render(request,'adminlogin.html')

def adminlogin(request):
    username_a = request.POST.get('username')
    password_a = request.POST.get('password')
    if User.objects.filter(username__contains=username_a).exists():
        user=authenticate(username=username_a,password=password_a)
        request.session['username']=username_a
        request.session['password']=password_a
        if user is not None:
            login(request,user)
            return redirect('adminindex')
        else:
            return render(request,'adminlogin.html',{'msg':'sorry....invalid user credentials'})
    else:
        return redirect('ad_login')
   
def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect('ad_login')