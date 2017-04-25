from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Location(models.Model):
    Name=models.CharField(max_length=50)
    site=models.CharField(max_length=50)
    lng=models.FloatField()
    lat=models.FloatField()
    material=models.CharField(max_length=50)
    capacity=models.CharField(max_length=50)
