# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
from tasks.models import Task

def getTasks(request):
    tasks  = Task.objects.all()
    tasksJson = [t.toJSON() for t in tasks]
    return JsonResponse(tasksJson, safe=False)
