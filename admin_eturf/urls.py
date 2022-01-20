from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminindex,name='adminindex'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('catdata',views.catdata,name='catdata'),
    path('viewcategory',views.viewcategory,name='viewcategory'),
    path('addmanagers',views.addmanagers,name='addmanagers')
]