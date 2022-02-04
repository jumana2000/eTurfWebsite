from django.db import models

# Create your models here.

class Categorydb(models.Model):
    name = models.CharField(max_length=100,null=True,blank=False)
    file = models.ImageField(upload_to='category',null=True,blank=False)

class Playgrounddb(models.Model):
    img = models.ImageField(upload_to='playground',null=True,blank=False)
    ground = models.CharField(max_length=100,null=True,blank=False)
    location = models.CharField(max_length=100,null=True,blank=False)
    price = models.IntegerField(null=True,blank=False)
    category = models.CharField(max_length=100,null=True,blank=False)

class Managerdb(models.Model):
    username = models.CharField(max_length=100,null=True,blank=False)
    password = models.CharField(max_length=100,null=True,blank=False)
    email = models.CharField(max_length=100,null=True,blank=False)
    image = models.ImageField(upload_to='manager',null=True,blank=False)
    playground = models.CharField(max_length=100,null=True,blank=False)