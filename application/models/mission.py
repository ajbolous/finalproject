class Mission():
    def __init__(self, title, startDate, endDate, location, target):
        self.title = title
        self.startDate = startDate
        self.endDate = endDate
        self.location = location
        self.target = target
        self.schedules = []

    def getSchedules(self):
        return self.schedules
        
    def addTask(self, task):
        self.schedules.append(task)

    def removeTask(self, task):
        self.schedules.remove(task)

    def __repr__(self):
        return "Mission({},{},{},{},{})".format(self.title, self.startDate, self.location, self.target, len(self.schedules))


