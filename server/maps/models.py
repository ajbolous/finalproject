from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Location(models.Model):
    lName=models.CharField(max_length=50)
    lType=models.CharField(max_length=50)
    lLong=models.FloatField()
    lLate=models.FloatField()
    lMaterial=models.CharField(max_length=50)
    lCapacity=models.CharField(max_length=50)
