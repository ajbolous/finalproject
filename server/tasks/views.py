# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
from application.main import Application


def getTasks(request):    
    missions = [Application.getMission().toJSON()]
    return JsonResponse(missions, safe=False)

def getMissionCosts(request):
    return JsonResponse(Application.getMissionCosts(), safe=False)
    