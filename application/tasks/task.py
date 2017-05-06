class Task():
    def __init__(self, taskType, taskLocation, startTime, endTime, comments=""):
        self.taskType = taskType
        self.location = taskLocation
        self.startTime = startTime
        self.endTime = endTime
        self.comments = comments

    def __repr__(self):
        return "Task({},{},{},{}".format(self.taskType, self.location, self.startTime, self.endTime)

    