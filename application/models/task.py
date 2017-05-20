class Task():
    def __init__(self, taskLocation, startTime, endTime, comments=""):
        self.location = taskLocation
        self.startTime = startTime
        self.endTime = endTime
        self.comments = comments

    def __repr__(self):
        return "{}({},{},{})".format(self.__class__, self.location, self.startTime, self.endTime)


class DigTask(Task):
    def __init__(self, location, startTime, endTime, amount, power, comments=""):
        Task.__init__(self, location, startTime, endTime, comments=comments)
        self.amount = amount
        self.power = power


class LoadTask(Task):
    def __init__(self, location, startTime, endTime, amount, material, comments=""):
        Task.__init__(self, location, startTime, endTime, comments=comments)
        self.amount = amount
        self.material = material


class HaulageTask(Task):
    def __init__(self, location, dumpLocation, startTime, endTime, amount, material, comments=""):
        Task.__init__(self, location, startTime, endTime, comments=comments)
        self.amount = amount
        self.material = material
