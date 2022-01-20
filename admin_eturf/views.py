from django.shortcuts import redirect, render
from admin_eturf.models import Categorydb

# Create your views here.

def adminindex(request):
    return render(request,'adminindex.html')

def addcategory(request):
    return render(request,'addcategory.html')

def catdata(request):
    if request.method == 'POST':
        name_c = request.POST.get('name')
        file_c = request.POST.get('file')
        data = Categorydb(name=name_c,file=file_c)
        data.save()
    return redirect('viewcategory')

def viewcategory(request):
    data = Categorydb.objects.all()
    return render(request,'viewcategory.html',{'data':data})

def addmanagers(request):
    return render(request,'addmanagers.html')