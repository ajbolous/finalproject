from __future__ import unicode_literals

from django.db import models
from django.forms.models import model_to_dict
<<<<<<< HEAD

=======
>>>>>>> 44184c3aacb3ad5bbe8594a0ef55bf50b9042bf4
# Create your models here.
class Machine(models.Model):
    mModel = models.CharField(max_length=50)
    mType = models.CharField(max_length=50)
    mSerial = models.CharField(max_length=50)   
    mWeight = models.IntegerField()
    mSpeed = models.IntegerField()
    mCapacity = models.IntegerField()
    mWeightCapacity = models.IntegerField()
    mFuelCapacity = models.IntegerField()
    mFuelConsumption = models.IntegerField()
    mLong = models.FloatField()
    mLat = models.FloatField()
    mIsAvailable = models.BooleanField()
    mFuelLevel = models.FloatField()
<<<<<<< HEAD

    def toJSON(self):
        return model_to_dict(self)
=======
    
    def toJSON(self):
        return model_to_dict(self)

>>>>>>> 44184c3aacb3ad5bbe8594a0ef55bf50b9042bf4
