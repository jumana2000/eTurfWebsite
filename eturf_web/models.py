from datetime import date
from django.db import models
from django.db.models.deletion import CASCADE

from admin_eturf.models import Managerdb

# Create your models here.

class Userdb(models.Model):
    username = models.CharField(max_length=100,null=True,blank=False)
    password = models.CharField(max_length=100,null=True,blank=False)
    mobile = models.IntegerField(null=True,blank=False)
    email = models.EmailField(null=True,blank=False)

    class Meta:
        unique_together = ["username", "email"]

class Bookdb(models.Model):
    userid = models.ForeignKey(Userdb,on_delete=CASCADE,null=True,blank=False)
    managerid = models.ForeignKey(Managerdb,on_delete=CASCADE,null=True,blank=False)
    start_time = models.TimeField(null=True,blank=False)
    end_time = models.TimeField(null=True,blank=False)
    date = models.DateField(null=True,blank=False)
    price = models.IntegerField(null=True,blank=False)
    ground = models.CharField(max_length=100,null=True,blank=False)