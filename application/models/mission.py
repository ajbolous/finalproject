from datetime import datetime, timedelta
from models.task import DigTask, LoadTask, HaulageTask


class Mission():
    def __init__(self, title, startDate, endDate, digLocation, dumpLocations, target):
        self.title = title
        self.startDate = startDate
        self.endDate = endDate
        self.target = target

        self.numDays = (endDate - startDate).days
        self.digLocation = digLocation
        self.dumpLocations = dumpLocations
        self.schedules = []

    def getSchedules(self):
        return self.schedules

    def createNextSchedule(self):
        if len(self.schedules) == 0:
            lastDate = self.startDate
        else:
            lastDate = self.schedules[len(self.schedules) - 1].date

        sched = Schedule(lastDate, lastDate, lastDate + timedelta(hours=9),
                         self.digLocation, self.dumpLocations, float(self.target) / self.numDays)
        self.schedules.append(sched)
        return sched

    def __repr__(self):
        return "Mission({},{},{},{},{})".format(self.title, self.startDate, self.digLocation, self.target, len(self.schedules))

    def toJSON(self):
        return {
            'type': 'mission',
            'startTime': self.startDate,
            'endTime': self.endDate,
            'digLocation': self.digLocation.toJSON(),
            'dumpLocations': [l.toJSON() for l in self.dumpLocations],
            'target': self.target,
            'schedules': [s.toJSON() for s in self.schedules]
        }


class Schedule():
    def __init__(self, date, startTime, endTime, digLocation, dumpLocations, target):
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.digLocation = digLocation
        self.dumpLocations = dumpLocations
        self.target = target
        self.tasks = []

        self.remainingDig = target
        self.remainingLoad = target
        self.remainingHaulage = target

    def getTasks(self):
        return self.tasks

    def addTask(self, task):
        self.tasks.append(task)

    def removeTask(self, task):
        self.tasks.remove(task)

    def updateRemaining(self):
        self.remainingDig = self.remainingHaulage = self.remainingLoad = self.target
        for task in self.tasks:
            delta = task.actualTarget if task.actualTarget else task.target
            if isinstance(task, HaulageTask):
                self.remainingHaulage -= delta
            elif isinstance(task, LoadTask):
                self.remainingLoad -= delta
            elif isinstance(task, DigTask):
                self.remainingDig -= delta

        self.remainingHaulage -= self.remainingDig

    def __repr__(self):
        return "Schedule({},{})".format(self.date, len(self.tasks))

    def toJSON(self):
        return {
            'type': 'schedule',
            'date': self.date,
            'startTime': self.startTime,
            'endTime': self.endTime,
            'digLocation': self.digLocation.toJSON(),
            'dumpLocations': [l.toJSON() for l in self.dumpLocations],
            'target': self.target,
            'remainingDig': self.remainingDig,
            'remainingLoad': self.remainingLoad,
            'remainingHaulage': self.remainingHaulage,
            'tasks': [t.toJSON() for t in self.tasks]
        }
