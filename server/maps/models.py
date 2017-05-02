from __future__ import unicode_literals
from django.forms.models import model_to_dict
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    lng = models.FloatField()
    lat = models.FloatField()
    material = models.CharField(max_length=50)
    capacity = models.FloatField()

    def toJSON(self):
        return model_to_dict(self)
