import pickle


def save(data, filePath):
    with open(filePath, 'w') as f:
        pickle.dump(data, f)


def load(filePath):
    with open(filePath, 'r') as f:
        return pickle.load(f)


def saveTasks(data):
    save(data, 'tasks.pkl')


def loadTasks():
    return load('tasks.pkl')
