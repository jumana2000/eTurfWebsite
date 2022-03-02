from django.urls import path
from . import views

urlpatterns = [
    path('adminindex',views.adminindex,name='adminindex'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('catdata',views.catdata,name='catdata'),
    path('viewcategory',views.viewcategory,name='viewcategory'),
    path('addplaygrounds',views.addplaygrounds,name='addplaygrounds'),
    path('playground_data',views.playground_data,name='playground_data'),
    path('viewplayground',views.viewplayground,name='viewplayground'),
    path('addmanagers',views.addmanagers,name='addmanagers'),
    path('managerdata',views.managerdata,name='managerdata'),
    path('viewmanager',views.viewmanager,name='viewmanager'),
    path('message',views.message,name='message'),
    path('',views.ad_login,name='ad_login'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adminlogout',views.adminlogout,name='adminlogout')
]