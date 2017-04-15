from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
<<<<<<< HEAD
def getAllMachines(request):
    pass

def getMachine(request):
    pass

def addMachine(request):
    pass

def deleteMachine(request):
    pass

def editMachine(request):
    pass
=======
from machines.models import Machine     

def getMachines(request):
    machines  = Machine.objects.all()
    machinesJson = [m.toJSON() for m in machines]
    return JsonResponse(machinesJson, safe=False)
>>>>>>> 44184c3aacb3ad5bbe8594a0ef55bf50b9042bf4
