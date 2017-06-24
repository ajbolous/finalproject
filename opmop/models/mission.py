from datetime import datetime, timedelta
from opmop.models.schedule import Schedule
from datetime import timedelta


class Mission():
    def __init__(self, mid, title, startDate, endDate, digLocation, dumpLocations, target):
        self.id = mid
        self.title = title
        self.startDate = startDate
        self.endDate = endDate
        self.target = target

        self.numDays = (endDate - startDate).days
        self.digLocation = digLocation
        self.dumpLocations = dumpLocations
        self.schedules = []

        for i in range(self.numDays):
            self.schedules.append(Schedule(i, self.startDate + timedelta(days=i), self, target / self.numDays))
        
    def getSchedules(self):
        return self.schedules

    def getScheduleById(self, id):
        print self.schedules
        for s in self.schedules:
            print s
            if s.id == id:
                return s
        return None

    def getScheduleByDate(self, date):
        for s in self.schedules:
            if s.date == date:
                return s
        return None

    def addSchedule(self, schedule):
        self.schedules.append(schedule)

    def __repr__(self):
        return "Mission({},{},{},{},{},{})".format(self.id, self.title, self.startDate, self.digLocation, self.target, len(self.schedules))

    def toJSON(self):
        return {
            'id': self.id,
            'type': 'mission',
            'startTime': self.startDate,
            'endTime': self.endDate,
            'digLocation': self.digLocation.toJSON(),
            'dumpLocations': [l.toJSON() for l in self.dumpLocations],
            'target': self.target,
            'schedules': [s.toJSON() for s in self.schedules]
        }

    def printMission(self):
        print self
        for sch in self.schedules:
            print "\t ", sch
            for task in sch.tasks:
                print "\t \t", task
