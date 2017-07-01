# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
from opmop.main import Application
from opmop.missions import planner
from datetime import datetime


def getScheduleCost(request):
    missionId = int(request.GET.get('mid'))
    scheduldeId = int(request.GET.get('sid'))
    mission = Application.database.getMissionById(missionId)
    schedule = mission.getScheduleById(scheduldeId)
    cost = planner.calculateScheduleCost(schedule)
    return JsonResponse(cost, safe=False)


def getMachineTasks(request):
    machineId = int(request.GET.get('mid'))
    scheddate =  datetime.strptime(request.GET.get('date'), '%d/%m/%Y')
    machine = Application.database.getMachineById(machineId)

    machineTasks = planner.calculateMachineRoute(machine, scheddate)
    return JsonResponse(machineTasks, safe=False)


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
