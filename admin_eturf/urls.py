from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminindex,name='adminindex'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('catdata',views.catdata,name='catdata'),
    path('viewcategory',views.viewcategory,name='viewcategory'),
    path('addmanagers',views.addmanagers,name='addmanagers'),
    path('addplaygrounds',views.addplaygrounds,name='addplaygrounds'),
    path('playground_data',views.playground_data,name='playground_data'),
    path('viewplayground',views.viewplayground,name='viewplayground')
]