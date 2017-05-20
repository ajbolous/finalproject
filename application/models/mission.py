class Mission():
    def __init__(self, title, startDate, location, target):
        self.title = title
        self.startDate = startDate
        self.location = location
        self.target = target
        self.tasks = []

    def addTask(self, task):
        self.tasks.append(task)

    def removeTask(self, task):
        self.tasks.remove(task)

    def __repr__(self):
        return "Mission({},{},{},{},{})".format(self.title, self.startDate, self.location, self.target, len(self.tasks))
