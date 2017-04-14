from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from machines.models import Machine     

def getMachines(request):
    machines  = Machine.objects.all()
    machinesJson = [m.toJSON() for m in machines]
    return JsonResponse(machinesJson, safe=False)
