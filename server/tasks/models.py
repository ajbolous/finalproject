# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms.models import model_to_dict

# Create your models here.


class Task(models.Model):
    tName = models.CharField(max_length=50)
    tDescription = models.CharField(max_length=200)
    tSite = models.CharField(max_length=50)
    tPriority = models.IntegerField()
    tDeadline=models.DateField()
    tStartDate=models.DateField()

    def toJSON(self):
        return model_to_dict(self)


class SubTask(models.Model):
    sDescription = models.CharField(max_length=200)
    sType=models.CharField(max_length=50)
    sStartDate=models.DateField()
    sFinishDate=models.DateField()
    sCapacity=models.IntegerField()
    sTask=models.ForeignKey(Task, on_delete=models.CASCADE)

    def toJSON(self):
        return model_to_dict(self)

class Location(models.Model):
    lName=models.CharField(max_length=50)
    lType=models.CharField(max_length=50)
    lLong=models.FloatField()
    lLate=models.FloatField()
    lMaterial=models.CharField(max_length=50)
    lCapacity=models.CharField(max_length=50)

    def toJSON(self):
        return model_to_dict(self)