from __future__ import unicode_literals

from django.db import models
from datetime import datetime

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.

class Recent_events(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True)
    
    heading=models.CharField(max_length=50)
    image=models.ImageField(upload_to='eventimages/pictures')
    content=models.CharField(max_length=5000)
   

class Teacher(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True)
    Name=models.CharField(max_length=50)
    Image=models.ImageField()


