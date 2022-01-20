from distutils.command.upload import upload
from statistics import mode
from tkinter.tix import Tree
from django.db import models

# Create your models here.

class Categorydb(models.Model):
    name = models.CharField(max_length=100,null=True,blank=False)
    file = models.ImageField(upload_to='category',null=True,blank=False)

class Playgrounddb(models.Model):
    img = models.ImageField(upload_to='playground',null=True,blank=False)
    ground = models.CharField(max_length=100,null=True,blank=False)
    location = models.CharField(max_length=100,null=Tree,blank=False)
    category = models.CharField(max_length=100,null=True,blank=False)
