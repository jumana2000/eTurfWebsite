from django.shortcuts import render

# Create your views here.

def managerindex(request):
    return render(request,'managerindex.html')