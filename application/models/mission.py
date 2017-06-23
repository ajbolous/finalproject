from datetime import datetime, timedelta


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

    def getSchedules(self):
        return self.schedules

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
