class Task():
    def __init__(self, taskLocation, startTime, endTime, target, comments=""):
        self.location = taskLocation
        self.startTime = startTime
        self.endTime = endTime
        self.comments = comments
        self.machine = None
        self.target = target
        self.actualTarget = None
        self.cost = -1

    def __repr__(self):
        return "\n{}({},{},{})".format(self.__class__, self.target, self.startTime.time(), self.endTime.time())

    def toJSON(self):
        return {
            'type': 'task',
            'startTime': self.startTime.isoformat(),
            'endTime': self.endTime.isoformat(),
            'location': self.location.toJSON(),
            'target': self.target,
            'actualTarget': self.actualTarget,
            'cost': self.cost,
            'comments': self.comments,
            'machine': self.machine.toJSON()
        }


class DigTask(Task):
    def __init__(self, location, startTime, endTime, target, power, comments=""):
        Task.__init__(self, location, startTime,
                      endTime, target, comments=comments)
        self.power = power

    def toJSON(self):
        t = Task.toJSON(self)
        t['type'] = 'dig'
        return t


class LoadTask(Task):
    def __init__(self, location, startTime, endTime, target, comments=""):
        Task.__init__(self, location, startTime,
                      endTime, target, comments=comments)

    def toJSON(self):
        t = Task.toJSON(self)
        t['type'] = 'load'
        return t


class HaulageTask(Task):
    def __init__(self, location, dumpLocation, startTime, endTime, target, comments=""):
        Task.__init__(self, location, startTime,
                      endTime, target, comments=comments)
        self.dumpLocation = dumpLocation

    def toJSON(self):
        t = Task.toJSON(self)
        t['type'] = 'haulage'
        t['dumpLocation'] = self.dumpLocation.toJSON()
        return t
