from datetime import datetime, timedelta
import json
from models.task import HaulageTask, LoadTask, DigTask, SubTask


class Machine():
    def __init__(self, id, model, weight, speed, fuelCapacity, fuelConsumption, point, isAvailable):
        self.id = id
        self.model = model
        self.weight = weight
        self.speed = speed
        self.fuelCapacity = fuelCapacity
        self.fuelConsumption = fuelConsumption
        self.point = point
        self.isAvailable = isAvailable
        self.tasks = []

    def getPosition(self):
        return self.point

    def getTasks(self):
        return self.tasks

    def getTimeWindows(self, date, size):
        ws = datetime(year=date.year, month=date.month, day=date.day, hour=9)
        we = ws + timedelta(hours=10)
        windows = []

        if len(self.tasks) == 0:
            return [(ws, we, (we-ws), self.point)]

        for task in self.tasks:
            winSize = (task.starTime - ws).hours
            if winSize >= size:
                windows.append((ws, task.starTime, winSize, task.location))
                ws = task.endTime

        return windows

    def makeOffer(self, task, mapGraph):
        pass

    def __repr__(self):
        return "{}({},{})".format(self.__class__, self.id, self.model)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class Truck(Machine):

    def __init__(self, id, model, weight, speed, fuelCapacity, feulConsumption, point, isAvailable, weightCapacity,  loadCapacity):
        Machine.__init__(self, id, model, weight, speed,
                         fuelCapacity, feulConsumption, point, isAvailable)
        self.loadCapacity = loadCapacity
        self.weightCapacity = weightCapacity

    def makeOffer(self, task, mapGraph):
        t = type(task)
        print t
        if not isinstance(task,HaulageTask):
            print False
            return False, -1

        path, distance = mapGraph.calcShortestPath(
            task.dumpLocation, task.location)

        consumedFuel = distance * self.fuelConsumption
        travelTime = distance / self.speed

        loadSize = task.amount
        loadWeight = task.amount * task.material
        averageFillTime = 1

        windows = Machine.getTimeWindows(self, task.startTime, travelTime + averageFillTime)

        print path, distance
        print windows
        print travelTime, distance
        numberOfTravels = loadWeight / self.weightCapacity
        numberOfTravels = max(numberOfTravels, loadSize / self.loadCapacity)

        numberOfRefeuls = (consumedFuel * numberOfTravels) / self.fuelCapacity

        time = numberOfTravels * travelTime + numberOfTravels * \
            averageFillTime + numberOfRefeuls * 1


class Shovel(Machine):

    def __init__(self, id, model, weight, speed, fuelCapacity, fuelConsumption, point, isAvailable,  digRate, power):
        Machine.__init__(self, id, model, weight, speed,
                         fuelCapacity, fuelConsumption, point, isAvailable)

        self.digRate = digRate
        self.power = power


class Loader(Machine):
    def __init__(self, id, model, weight, speed, fuelCapacity, fulConsumption, point, isAvailable,  weightCapacity, loadCapacity):
        Machine.__init__(self, id, model, weight, speed,
                         fuelCapacity, fulConsumption, point, isAvailable)
        self.weightCapacity = weightCapacity
        self.loadCapacity = loadCapacity
