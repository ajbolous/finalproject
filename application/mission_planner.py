from models.mission import Mission
from models.task import Task, DigTask, HaulageTask, LoadTask
from models.map import Map
from models.schedule import Schedule
from database.database import Database
from datetime import datetime
from datetime import timedelta


def createMission(title, description, location, dumpLocation, startDate, endDate, target):
    mission = Mission(title, startDate, endDate, location, target)

    numDays = (endDate - startDate).days

    for i in range(numDays):
        date = startDate + timedelta(days=i)
        start = date + timedelta(hours=9)
        end = start + timedelta(hours=12)
        sch = Schedule(date, start, end, location)

        sch.tasks.append(DigTask(mission.location, sch.startTime,
                                 sch.endTime, target / numDays, 100, "Dig all day"))
        sch.tasks.append(LoadTask(mission.location, sch.startTime,
                                  sch.endTime, target / numDays, 100, 'Loader'))

        for i in range(6):
            sch.tasks.append(HaulageTask(mission.location, dumpLocation, sch.startTime + timedelta(
                hours=2 * i), sch.startTime + timedelta(hours=2 * (i + 1)), (target / numDays / 6), 100, "Haul all day"))

        mission.schedules.append(sch)
    return mission


import random


db = Database()
db.load()

map = Map()
map.loadFromJson()

l1 = map.getRoads()[random.randint(1, 20)].getPoints()[random.randint(1, 3)]
l2 = map.getRoads()[random.randint(1, 20)].getPoints()[random.randint(1, 3)]


mission = createMission("New mission", "dig", l1, l2, datetime(
    2017, 5, 1, hour=0, minute=0, second=0), datetime(2017, 5, 2, hour=0, minute=0, second=0), 10000)

db.missions = [mission]

db.save()
print mission
