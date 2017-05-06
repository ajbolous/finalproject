import pickle


def save(data, filePath):
    with open(filePath, 'w') as f:
        pickle.dump(data, f)


def load(filePath):
    with open(filePath, 'r') as f:
        return pickle.load(f)


class Database():
    def __init__(self, filePath):
        try:
            self.loadData(filePath)
        except:
            self.machines = []
            self.tasks = []
            self.missions = []

    def loadData(self,filePath):
        data = load(filePath)
        self.machines = data['machines']
        self.tasks = data['tasks']
        self.missions = data['missions']

    def saveData(self, filePath):
        save({
            'machines': self.machines,
            'tasks': self.tasks,
            'missions': self.missions
        }, filePath)

    def getMachines(self):
        return self.machines

    def getTasks(self):
        return self.tasks

    def getMissions(self):
        return self.missions