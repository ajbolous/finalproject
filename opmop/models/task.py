class Task():
    def __init__(self, tid, taskLocation, startTime, endTime, target, machineId, comments=""):
        self.id = tid
        self.location = taskLocation
        self.startTime = startTime
        self.endTime = endTime
        self.comments = comments
        self.machineId = machineId
        self.target = target
        self.actualTarget = None
        self.cost = None

    def __repr__(self):
        return "{}({},{},{})".format(self.__class__, self.target, self.startTime.time(), self.endTime.time())

    def toJSON(self):
        return {
            'id': self.id,
            'type': 'task',
            'startTime': self.startTime.isoformat(),
            'endTime': self.endTime.isoformat(),
            'location': self.location.toJSON(),
            'target': self.target,
            'actualTarget': self.actualTarget,
            'cost': self.cost,
            'comments': self.comments,
            'machineId': self.machineId
        }


class DigTask(Task):
    def __init__(self, tid,location, startTime, endTime, target, machineId,  comments=""):
        Task.__init__(self, tid, location, startTime, endTime, target, machineId,  comments=comments)

    def toJSON(self):
        t = Task.toJSON(self)
        t['type'] = 'dig'
        return t


class LoadTask(Task):
    def __init__(self,  tid,location, startTime, endTime, target, machineId, comments=""):
        Task.__init__(self, tid, location, startTime,
                      endTime, target, machineId, comments=comments)

    def toJSON(self):
        t = Task.toJSON(self)
        t['type'] = 'load'
        return t


class HaulageTask(Task):
    def __init__(self,  tid,location, dumpLocation, startTime, endTime, target, machineId,  comments=""):
        Task.__init__(self, tid, location, startTime,
                      endTime, target, machineId, comments=comments)
        self.dumpLocation = dumpLocation

    def toJSON(self):
        
        t = Task.toJSON(self)
        t['type'] = 'haulage'
        t['dumpLocation'] = self.dumpLocation.toJSON()
        return t
