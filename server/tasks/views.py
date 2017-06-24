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
    missionId = int(request.GET.get('mid'))
    scheduldeId = int(request.GET.get('sid'))
    mission = Application.database.getMissionById(missionId)
    schedule = mission.getScheduleById(scheduldeId)
    planner.calculateSchedule(mission, schedule)
    schedule.allocated = True
    Application.database.save()
    return JsonResponse(schedule.toJSON(), safe=False)

def getMissionCosts(request):
    return JsonResponse([], safe=False)