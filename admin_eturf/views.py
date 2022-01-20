from unicodedata import category, name
from django.shortcuts import redirect, render
from admin_eturf.models import Categorydb, Playgrounddb

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

def addmanagers(request):
    return render(request,'addmanagers.html')

def addplaygrounds(request):
    data = Categorydb.objects.all()
    return render(request,'addplaygrounds.html',{'data':data})

def playground_data(request):
    if request.method == 'POST':
        ground_name = request.POST.get('name')
        location_p = request.POST.get('location')
        category_p = request.POST.get('category')
        img_p = request.FILES['img']
        data = Playgrounddb(ground=ground_name,location=location_p,category=category_p,img=img_p)
        data.save()
    return redirect('addplaygrounds')

def viewplayground(request):
    data = Playgrounddb.objects.all()
    return render(request,'viewplayground.html',{'data':data})