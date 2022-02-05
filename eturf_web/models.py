from datetime import date
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Userdb(models.Model):
    username = models.CharField(max_length=100,null=True,blank=False)
    password = models.CharField(max_length=100,null=True,blank=False)
    mobile = models.IntegerField(null=True,blank=False)
    email = models.EmailField(null=True,blank=False)

class Bookdb(models.Model):
    userid = models.ForeignKey(Userdb,on_delete=CASCADE,null=True,blank=False)
    start_time = models.TimeField(null=True,blank=False)
    end_time = models.TimeField(null=True,blank=False)
    date = models.DateField(null=True,blank=False)