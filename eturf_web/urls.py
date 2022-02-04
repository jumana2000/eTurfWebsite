from django.urls import path
from . import views

urlpatterns = [
    path('',views.eturf_index,name='eturf_index')
]