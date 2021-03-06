from django.shortcuts import render

from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from opmop.main import Application


def getRoads(request):
    return JsonResponse([road.toJSON() for road in Application.roadsMap.getRoads()], safe=False)


def getLocations(request):
    return JsonResponse([location.toJSON() for location in Application.database.getLocations()], safe=False)


def addLocation(request):
    location = {}
    location.lat = float(request.GET.get('lat'))
    location.lng = float(request.GET.get('lng'))
    location.name = request.GET.get('name')
    location.site = request.GET.get('site')
    location.capacity = request.GET.get('capacity')
    location.material = request.GET.get('material')
    return HttpResponse("Location saved successfuly.", 200)
