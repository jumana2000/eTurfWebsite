from django.urls import path
from . import views

urlpatterns = [
    path('',views.eturf_index,name='eturf_index'),
    path('eturf_list',views.eturf_list,name='eturf_list'),
    path('booknow',views.booknow,name='booknow'),
    path('userregister',views.userregister,name='userregister'),
    path('u_register',views.u_register,name='u_register')
]