from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from models import Person
from django.core import serializers


def getPerson(request):
    name = request.GET['name']
    p = Person.objects.get(firstName=name)
    return JsonResponse(p.toJSON(), safe=False)


def addPerson(request):
    fname = request.GET['fname']
    lname = request.GET['lname']
    p = Person(firstName=fname, lastName=lname)
    p.save()
    return HttpResponse('Person added', 200)


def getAll(request):
    persons = Person.objects.all()
    personsJson = [p.toJSON() for p in persons]
    return JsonResponse(personsJson, safe=False)
