from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('managerindex',views.managerindex,name='managerindex'),
    path('booking_history',views.booking_history,name='booking_history'),
    path('',views.m_login,name='m_login'),
    path('managerlogin',views.managerlogin,name='managerlogin'),
    path('managerlogout',views.managerlogout,name='managerlogout')
]