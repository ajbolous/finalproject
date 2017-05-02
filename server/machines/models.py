from __future__ import unicode_literals

from django.db import models
from django.forms.models import model_to_dict

# Create your models here.
class Machine(models.Model):
    model = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)   
    weight = models.IntegerField(null = True)
    speed = models.IntegerField(null = True)
    capacity = models.IntegerField(null = True)
    weightCapacity = models.IntegerField(null = True)
    fuelCapacity = models.IntegerField(null = True)
    fuelConsumption = models.IntegerField(null = True)
    lng = models.FloatField(null = True)
    lat = models.FloatField(null = True)
    isAvailable = models.BooleanField()
    fuelLevel = models.FloatField(null = True)
    modalYear=models.IntegerField(null = True)
    def toJSON(self):
        return model_to_dict(self)

