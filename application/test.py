from models.task import Task
from models.map import Map,MapGraph
import time
from database.database import Database
from models.machine import Loader, Shovel, Truck, Machine
import random


db = Database()


map = Map()
map.loadFromJson()
g = MapGraph()
g.buildGraph(map)


machines = []


def randomPoint():
    roads = map.getRoads()
    road  = roads[random.randint(0, len(roads)-1)]
    points = road.getPoints()
    return points[random.randint(0,len(points)-1)]

for i in range(0, 5):
    machines.append(Loader(i, 'TRX', 10000, random.randint(25,30), random.randint(800,1200), random.randint(8,12),random.randint(4,6),randomPoint(), True, random.randint(20,40), 10))

for i in range(5, 10):
    p  = map.getRoads()[0].getPoints()[0]
    machines.append(Shovel(i, 'ZXF', 10000, random.randint(15,22), random.randint(1000,1500), random.randint(16,20),random.randint(8,12),randomPoint(), True, random.randint(40,80), 50))

for i in range(10, 50):
    p  = map.getRoads()[0].getPoints()[0]
    machines.append(Truck(i, 'TRK1', 10000, random.randint(40,60), random.randint(600,800), random.randint(6,10),1,randomPoint(), True, random.randint(400,800), 500))


db.machines = machines
db.map = map


db.save()
