# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms.models import model_to_dict
from django.db import models


class Person(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

    def toJSON(self):
        return model_to_dict(self)
# Create your models here.
