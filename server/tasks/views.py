# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
from application.main import Application


def getTasks(request):    
    missions = [Application.getMission().toJSON()]
    return JsonResponse(missions, safe=False)


def getTasksRoute(request):
    
    machineId = request.GET.get('machineId')
    route = Application.getRoutes(int(machineId))
    return JsonResponse(route,safe = False)
