# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
from opmop.main import Application
from opmop.missions import planner
from datetime import datetime

def getMissions(request):
    missions = [m.toJSON() for m in Application.database.getMissions()]
    return JsonResponse(missions, safe=False)

def allocateSchedule(request):
    missionId = int(request.GET.get('id'))
    date = datetime(request.GET.get('date'))
    target = int(request.GET.get('date'))
    mission = Application.database.getMissionById(missionId)
    planner.calculateSchedule(mission, date, target)

def getMissionCosts(request):
    return JsonResponse(planner.calculateScheduleCost(), safe=False)