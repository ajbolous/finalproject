import pickle
import jsonpickle
import os
from models.map import Map
from models.machine import Truck, Shovel, Loader

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

    def load(self):

        data = load('data.pkl')

        self.machines = data['machines']
        if 'missions' in data:
            self.missions = data['missions']
        else:
            self.missions = []

    def save(self):
        data = {
            'machines': self.machines,
            'missions': self.missions
        }
        save(data, 'data.pkl')
        with open(os.path.join(PATH, 'data.json'), 'w') as f:
            f.write(jsonpickle.encode(data))

    def getMachines(self):
        return self.machines

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
        return shovels,loaders,trucks

    def getMissions(self):
        return self.missions