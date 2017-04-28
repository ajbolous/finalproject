from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from machines.models import Machine

# Create your views here.


def getMachines(request):
    machines = Machine.objects.all()
    machinesJson = [m.toJSON() for m in machines]
    return JsonResponse(machinesJson, safe=False)


def addMachine(request):
    m = Machine()
    m.mType = 'bolous'
    m.mCapacity = 12
    m.mWeight = 20
    m.mYear = 2017
    m.mSpeed = 200
    m.mFuelCapacity = 25
    m.mWeightCapacity = 26
    m.mFuelConsumption = 255
    m.mLong = 2
    m.mLat = 1
    m.mIsAvailable = True
    m.mFuelLevel = 45
    m.save()
    return HttpResponse("Called add machine", 200)
