from models.task import DigTask, LoadTask, HaulageTask


class Schedule():
    def __init__(self, sid, date, mission, target):
        self.id = sid
        self.date = date
        self.mission = mission
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
        return "Schedule({},{},{})".format(self.id, self.date, len(self.tasks))

    def toJSON(self):
        return {
            'id': self.id,
            'type': 'schedule',
            'date': self.date,
            'target': self.target,
            'remainingDig': self.remainingDig,
            'remainingLoad': self.remainingLoad,
            'remainingHaulage': self.remainingHaulage,
            'tasks': [t.toJSON() for t in self.tasks]
        }
