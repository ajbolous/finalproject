import pickle
import os
import json

from opmop.mapping.map import Map
from opmop.models.machine import Truck, Shovel, Loader

PATH = os.path.dirname(os.path.realpath(__file__))


def save(data, filePath):
    with open(os.path.join(PATH, filePath), 'w') as f:
        pickle.dump(data, f)


def load(filePath):
    with open(os.path.join(PATH, filePath), 'r') as f:
        return pickle.load(f)


class Database():
    def __init__(self):
        self.machines = []
        self.missions = None
        self.locations = []
        
    def load(self):

        data = load('data.pkl')

        self.machines = data['machines']
        self.locations = data['locations']
        if 'missions' in data:
            self.missions = data['missions']
        else:
            self.missions = []

    def save(self):
        data = {
            'machines': self.machines,
            'missions': self.missions,
            'locations': self.locations
        }
        save(data, 'data.pkl')

    def getMachines(self):
        return self.machines

    def getMachineById(self, mid):
        for m in self.machines:
            if m.id == mid:
                return m
        return None

    def getMachinesSorted(self):
        trucks = []
        shovels = []
        loaders = []
        for machine in self.machines:
            if isinstance(machine, Truck):
                trucks.append(machine)
            if isinstance(machine, Loader):
                loaders.append(machine)
            if isinstance(machine, Shovel):
                shovels.append(machine)

        return shovels, loaders, trucks

    def getMissions(self):
        return self.missions

    def getMissionById(self, mid):
        for m in self.missions:
            if m.id == mid:
                return m
        return None

    def getSchedulesByDate(self, date):
        schedules = []
        for m in self.getMissions():
            for schedule in m.getSchedules():
                if schedule.date.date == date.date():
                    schedules.append(schedule)
        return schedules

    def getScheduleById(self, sid):
        pass

    def getLocations(self):
        return self.locations

    def getRoadsJson(self):
        with open(os.path.join(PATH, 'roads.json'), 'r') as f:
            return json.load(f)
