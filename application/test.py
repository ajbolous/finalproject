from models.task import Task
from models.map import Map
import time
from database.database import Database
from models.machine import Loader, Shovel, Truck, Machine
import random


db = Database()


map = Map()
map.loadFromJson()

machines = []

p  = map.getRoads()[0].getPoints()[0]

print p
for i in range(0, 20):
    machines.append(Loader(i, 'TRX', 10000, 40, 800, 10,
                           map.getRoads()[1].getPoints()[0], True, 20, 10))

for i in range(20, 40):
    machines.append(Shovel(i, 'ZXF', 10000, 40, 800, 10,
                           p, True, 20, 50))

for i in range(40, 50):
    machines.append(Truck(i, 'TRK1', 10000, 40, 800, 10,
                          map.getRoads()[2].getPoints()[0], True, 400, 500))


db.machines = machines
db.map = map


db.save()
