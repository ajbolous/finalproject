from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from machines.models import Machine     

# Create your views here.

def getMachines(request):
    machines  = Machine.objects.all()
    machinesJson = [m.toJSON() for m in machines]
    return JsonResponse(machinesJson, safe=False)


def addMachine(request):
    m=Machine()
    m.type= request.GET.get('type')
    m.model= request.GET.get('model')
    m.capacity= request.GET.get('capacity')
    m.weight=int(request.GET.get('weight'))
    m.modalYear=int(request.GET.get('modalYear'))
    m.speed=int(request.GET.get('speed'))
    m.fuelCapacity=int(request.GET.get('fuelCapacity'))
    m.weightCapacity=int(request.GET.get('weightCapacity'))
    m.fuelConsumption=int(request.GET.get('fuelConsumption'))
    m.lng=float(request.GET.get('lng'))
    m.lat=float(request.GET.get('lat'))
    m.isAvailable=bool(request.GET.get('isAvailable'))
    m.fuelLevel=float(request.GET.get('fuelLevel'))
    
    m.save()
    return HttpResponse("Called add machine", 200)
