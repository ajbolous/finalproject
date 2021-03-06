
import time
from database import Database
import random
from datetime import datetime

from opmop.models.location import Location
from opmop.models.machine import Loader, Shovel, Truck, Machine
from opmop.models.task import Task
from opmop.models.mission import Mission
from opmop.models.schedule import Schedule
from opmop.mapping.map import Map
from opmop.mapping.map_graph import MapGraph


db = Database()
map = Map()
map.buildFromJson(db.getRoadsJson())


def randomPoint():
    roads = map.getRoads()
    road = roads[random.randint(0, len(roads) - 1)]
    points = road.getPoints()
    return points[random.randint(0, len(points) - 1)]


def createMachines():
    machines = []
    for i in range(0, 4):
        machines.append(Shovel(i, 'SHV' + str(i), random.randint(1500, 2000), random.randint(12, 20), random.randint(
            8000, 12000), random.randint(150, 200), random.randint(80, 120), randomPoint(), True, random.randint(50, 80)))

    for i in range(4, 8):
        machines.append(Loader(i, 'LOD' + str(i), random.randint(300000, 400000), random.randint(40, 50), random.randint(
            8000, 12000), random.randint(150, 200), random.randint(80, 120), randomPoint(), True, random.randint(25, 60)))

    for i in range(8, 20):
        machines.append(Truck(i,  'TRK' + str(i), random.randint(250, 400), random.randint(40, 50), random.randint(
            8000, 12000), random.randint(150, 200), random.randint(80, 120), randomPoint(), True, random.randint(350, 500)))
    return machines


def createMission(mid, title, location, dumpLocations, startDate, endDate, target):
    mission = Mission(mid, title, startDate, endDate,
                      location, dumpLocations, target)
    return mission


def createLocations():
    locations = []
    for i in range(0, 3):
        l = Location(i, 'Site{}'.format(i), 'dig', randomPoint())
        locations.append(l)

    for i in range(3, 6):
        l = Location(i, 'Dump{}'.format(i), 'dump', randomPoint())
        locations.append(l)

    for i in range(6, 8):
        l = Location(i, 'Fuel{}'.format(i), 'fuel', randomPoint())
        locations.append(l)

    return locations


db.map = map
db.locations = createLocations()

db.machines = createMachines()

mission1 = createMission(1, "Iron min", db.locations[1], db.locations[5:10], datetime(
    2017, 7, 1, hour=0, minute=0, second=0), datetime(2017, 7, 30, hour=0, minute=0, second=0), 80000)

mission2 = createMission(2, "Coal june", db.locations[2], db.locations[5:10], datetime(
    2017, 7, 1, hour=0, minute=0, second=0), datetime(2017, 7, 20, hour=0, minute=0, second=0), 100000)



db.missions = [mission1, mission2]

db.save()
