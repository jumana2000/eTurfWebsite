from django.db import models

# Create your models here.

class Categorydb(models.Model):
    name = models.CharField(max_length=100,null=True,blank=False)
    file = models.ImageField(upload_to='category',null=True,blank=False)