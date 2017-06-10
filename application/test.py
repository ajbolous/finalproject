from models.task import Task
from models.mission import Mission, Schedule
from models.map import Map, MapGraph
import time
from database.database import Database
from models.machine import Loader, Shovel, Truck, Machine
import random
from datetime import datetime
from models.locations import Location

db = Database()
map = Map()
map.loadFromJson()


def randomPoint():
    roads = map.getRoads()
    road = roads[random.randint(0, len(roads) - 1)]
    points = road.getPoints()
    return points[random.randint(0, len(points) - 1)]


def createMachines():
    machines = []
    for i in range(0, 5):
        machines.append(Shovel(i, 'SHV' + str(i), random.randint(1000, 2000), random.randint(12, 20), random.randint(
            8000, 12000), random.randint(150, 200), random.randint(80, 120), randomPoint(), True, random.randint(20, 120)))

    for i in range(5, 10):
        p = map.getRoads()[0].getPoints()[0]
        machines.append(Loader(i, 'LOD' + str(i), random.randint(250000, 400000), random.randint(40, 50), random.randint(
            8000, 12000), random.randint(150, 200), random.randint(80, 120), randomPoint(), True, random.randint(20, 60)))

    for i in range(10, 20):
        p = map.getRoads()[0].getPoints()[0]
        machines.append(Truck(i, 'TRK' + str(i), random.randint(250, 400), random.randint(40, 50), random.randint(
            8000, 12000), random.randint(150, 200), random.randint(80, 120), randomPoint(), True, random.randint(300, 400)))
    return machines


def createMission(title, description, location, dumpLocations, startDate, endDate, target):
    mission = Mission(title, startDate, endDate,
                      location, dumpLocations, target)
    numDays = (endDate - startDate).days
    mission.schedules = []
    return mission


def createLocations():
    locations = []
    for i in range(0, 5):
        l = Location(i, 'Site{}'.format(i), 'dig', randomPoint())
        locations.append(l)

    for i in range(5, 10):
        l = Location(i, 'Dump{}'.format(i), 'dump', randomPoint())
        locations.append(l)

    for i in range(10, 12):
        l = Location(i, 'Fuel{}'.format(i), 'fuel', randomPoint())
        locations.append(l)

    return locations


db.map = map
db.machines = createMachines()
db.locations = createLocations()

mission = createMission("New mission", "dig", db.locations[2], db.locations[5:10], datetime(
    2017, 5, 1, hour=0, minute=0, second=0), datetime(2017, 5, 11, hour=0, minute=0, second=0), 500000)

db.missions = [mission]

db.save()
