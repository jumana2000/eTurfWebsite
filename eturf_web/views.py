from django.shortcuts import render

# Create your views here.

def eturf_index(request):
    return render(request,'eturf_index.html')