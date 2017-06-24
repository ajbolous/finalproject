from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from opmop.main import Application
from opmop.models.machine import Machine
from opmop.missions import planner


def getMachineId(request):
    machineId = request.GET.get('id')
    machine = Application.database.getMachineById(machineId)
    return JsonResponse(machine, safe=False)


def getMachines(request):
    machinesJson = [machine.toJSON()
                    for machine in Application.database.getMachines()]
    return JsonResponse(machinesJson, safe=False)


def getMachineRoute(request):
    machineId = request.GET.get('id')
    route = planner.calculateMachineRoute(int(machineId))
    return JsonResponse(route, safe=False)


def addMachine(request):
    m = Machine()
    m.type = request.GET.get('type')
    m.model = request.GET.get('model')
    m.capacity = request.GET.get('capacity')
    m.weight = int(request.GET.get('weight'))
    m.modalYear = int(request.GET.get('modalYear'))
    m.speed = int(request.GET.get('speed'))
    m.fuelCapacity = int(request.GET.get('fuelCapacity'))
    m.weightCapacity = int(request.GET.get('weightCapacity'))
    m.fuelConsumption = float(request.GET.get('fuelConsumption'))
    m.lng = float(request.GET.get('lng'))
    m.lat = float(request.GET.get('lat'))
    m.isAvailable = bool(request.GET.get('isAvailable'))
    m.fuelLevel = float(request.GET.get('fuelLevel'))

    return HttpResponse("Called add machine", 200)


def editMachine(request):
    m = Machine.objects.get(id=int(request.GET.get('id')))
    m.type = request.GET.get('type')
    m.model = request.GET.get('model')
    m.capacity = request.GET.get('capacity')
    m.weight = int(request.GET.get('weight'))
    m.modalYear = int(request.GET.get('modalYear'))
    m.speed = int(request.GET.get('speed'))
    m.fuelCapacity = int(request.GET.get('fuelCapacity'))
    m.weightCapacity = int(request.GET.get('weightCapacity'))
    m.fuelConsumption = float(request.GET.get('fuelConsumption'))
    m.lng = float(request.GET.get('lng'))
    m.lat = float(request.GET.get('lat'))
    m.isAvailable = bool(request.GET.get('isAvailable'))
    m.fuelLevel = float(request.GET.get('fuelLevel'))

    return HttpResponse("Called edit machine", 200)


def deleteMachine(request):
    return HttpResponse("Succesfuly Deleted the machine ", 200)
