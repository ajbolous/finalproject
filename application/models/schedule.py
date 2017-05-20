class Schedule():
    def __init__(self, date, startTime, endTime, location):
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.location = location
        self.tasks = []

    def addTask(self, task):
        self.tasks.append(task)

    def removeTask(self, task):
        self.tasks.remove(task)

    def __repr__(self):
        return "Schedule({},{})".format(self.date, len(self.tasks))
