from django.shortcuts import render
from algorithms.street_graph import getRoadsNodes, buildGraph, calcShortestPath
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def getRoads(request):
    return JsonResponse(getRoadsNodes(), safe=False)

def getShortestPath(request):
    return JsonResponse(calcShortestPath(0,20))

@csrf_exempt
def saveRoads(request):
    return HttpResponse("all ok")
