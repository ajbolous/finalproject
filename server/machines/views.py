from django.shortcuts import render
from django.http import JsonResponse
from machines.models import Machine     

# Create your views here.

def getMachines(request):
    machines  = Machine.objects.all()
    machinesJson = [m.toJSON() for m in machines]
    return JsonResponse(machinesJson, safe=False)
