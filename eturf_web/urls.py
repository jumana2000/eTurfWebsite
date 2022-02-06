from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.eturf_index,name='eturf_index'),
    path('eturf_list',views.eturf_list,name='eturf_list'),
    path('booknow/<int:turfid>/',views.booknow,name='booknow'),
    path('bookdata',views.bookdata,name='bookdata'),
    path('mybooking',views.mybooking,name='mybooking'),
    path('userregister',views.userregister,name='userregister'),
    path('u_register',views.u_register,name='u_register'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('userlogout',views.userlogout,name='userlogout'),
]