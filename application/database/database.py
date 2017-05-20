import pickle
import jsonpickle
import os
from models.map import Map

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
        self.map = None

    def load(self):

        data = load('data.pkl')

        self.map = data['map']
        if self.map == None:
            self.map = Map()
            self.map.loadFromJson()

        self.machines = data['machines']

    def save(self):
        data = {
            'map': self.map,
            'machines': self.machines
        }
        save(data, 'data.pkl')
        with open(os.path.join(PATH, 'data.json'), 'w') as f:
            f.write(jsonpickle.encode(data))

    def getMachines(self):
        return self.machines

    def getRoads(self):
        return self.map['roads']

    def getLocations(self):
        return self.map['locations']
