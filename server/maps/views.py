from django.shortcuts import render
from algorithms.street_graph import getRoadsNodes, buildGraph, calcShortestPath
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from maps.models import Location


def getRoads(request):
    return JsonResponse(getRoadsNodes(), safe=False)


def getShortestPath(request):
    dest = int(request.GET['dest'])
    src = int(request.GET['source'])
    return JsonResponse(calcShortestPath(src, dest), safe=False)


@csrf_exempt
def saveRoads(request):
    return HttpResponse("all ok")


def getLocations(request):
    locations = [location.toJSON() for location in Location.objects.all()]
    return JsonResponse(locations, safe=False)


def addLocation(request):
    location = Location()
    location.lat = float(request.GET.get('lat'))
    location.lng = float(request.GET.get('lng'))
    location.name = request.GET.get('name')
    location.site = request.GET.get('site')
    location.capacity = request.GET.get('capacity')
    location.material = request.GET.get('material')

    location.save()
    return HttpResponse("Location saved successfuly.", 200)
