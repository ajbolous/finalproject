from datetime import datetime, timedelta
import json
from models.task import HaulageTask, LoadTask, DigTask, SubTask


class Machine():
    def __init__(self, id, model, weight, speed, fuelCapacity,  fuelConsumption, staticFeulConsupmtion, location, isAvailable):
        self.id = id
        self.model = model
        self.weight = weight
        self.speed = speed
        self.fuelCapacity = fuelCapacity
        self.fuelConsumption = fuelConsumption
        self.staticFeulConsupmtion = staticFeulConsupmtion
        self.location = location
        self.isAvailable = isAvailable
        self.tasks = []

    def getLocation(self):
        return self.location

    def getTasks(self):
        return self.tasks

    def getTimeWindows(self, date, size):
        ws = datetime(year=date.year, month=date.month, day=date.day, hour=9)
        we = ws + timedelta(hours=size)
        windows = []

        if len(self.tasks) == 0:
            for i in range( int(9/size)):
                windows.append((ws, ws + timedelta(hours=size) , size, self.location))
                ws += timedelta(hours=size)

        for task in self.tasks:
            while True:
                winSize = ((task.startTime - ws).seconds // 3600)
                if winSize >= size:
                    windows.append((ws, ws + timedelta(hours=size), size, task.location))
                    ws = ws + timedelta(hours=size)
                else:
                    break

        return windows

    def makeOffer(self, task, mapGraph):
        pass

    def __repr__(self):
        return "{}({},{})".format(self.__class__, self.id, self.model)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class Truck(Machine):

    def __init__(self, id, model, weight, speed, fuelCapacity, feulConsumption, staticFeulConsupmtion, location, isAvailable, weightCapacity,  loadCapacity):
        Machine.__init__(self, id, model, weight, speed,
                         fuelCapacity, feulConsumption, staticFeulConsupmtion, location, isAvailable)
        self.loadCapacity = loadCapacity
        self.weightCapacity = weightCapacity


    def makeOffer(self, task, mapGraph):
        if not isinstance(task, HaulageTask):
            return False, []

        path, distance = mapGraph.calcShortestPath(
            task.dumpLocation, task.location)

        consumedFuel = distance * self.fuelConsumption
        travelTime = distance / self.speed

        loadSize = task.amount
        loadWeight = task.amount
        averageFillTime = 1

        windows = Machine.getTimeWindows(
            self, task.startTime, travelTime + averageFillTime)

        numberOfTravels = loadWeight / self.weightCapacity
        numberOfTravels = max(numberOfTravels,1)
        numberOfTravels = max(numberOfTravels, loadSize / self.loadCapacity)
        numberOfRefeuls = (consumedFuel * numberOfTravels) / self.fuelCapacity

        tripTime = travelTime + averageFillTime + \
            (numberOfRefeuls * 1) / numberOfTravels

        tripCost = tripTime * 100 + consumedFuel * 10 + distance * 10

        subtasks = []

        avgAmount = loadSize / numberOfTravels


        for window in windows:
            stask = SubTask(window[0], window[1],
                            task.location, self, avgAmount, tripCost)
            subtasks.append(stask)
            numberOfTravels -= 1
            if numberOfTravels == 0:
                break

        if len(subtasks) > 0:
            return True, subtasks, tripCost*len(subtasks)

        return False, []


class Shovel(Machine):

    def __init__(self, id, model, weight, speed, fuelCapacity, fuelConsumption, staticFeulConsupmtion, location, isAvailable,  digRate, power):
        Machine.__init__(self, id, model, weight, speed, fuelCapacity,
                         fuelConsumption, staticFeulConsupmtion, location, isAvailable)

        self.digRate = digRate
        self.power = power

    def makeOffer(self, task, mapGraph):
        if not isinstance(task, DigTask):
            return False, []

        path, distance = mapGraph.calcShortestPath(
            self.location, task.location)

        consumedFuel = distance * self.fuelConsumption
        travelTime = distance / self.speed
        digTime = task.amount / self.digRate
        digTime = min(digTime,8)
        totalTime = travelTime + digTime

        consumedFuel += (digTime * self.staticFeulConsupmtion)
        tripCost = totalTime * 100 + consumedFuel * 10 + distance * 10

        windows = Machine.getTimeWindows(self, task.startTime,  totalTime)

        if len(windows) <= 0:
            return False, []

        return True,  [SubTask(windows[0][0], windows[0][1], task.location, self, digTime*self.digRate, tripCost)], tripCost


class Loader(Machine):
    def __init__(self, id, model, weight, speed, fuelCapacity, fulConsumption, staticFeulConsupmtion, location, isAvailable,  weightCapacity, loadCapacity):
        Machine.__init__(self, id, model, weight, speed,
                         fuelCapacity, fulConsumption, staticFeulConsupmtion, location, isAvailable)
        self.weightCapacity = weightCapacity
        self.loadCapacity = loadCapacity

    def makeOffer(self, task, mapGraph):
        if not isinstance(task, LoadTask):
            return False, []

        path, distance = mapGraph.calcShortestPath(
            self.location, task.location)

        consumedFuel = distance * self.fuelConsumption
        travelTime = distance / self.speed
        loadTime = (task.amount / self.loadCapacity) * 0.2
        loadTime = min(loadTime,8)
        totalTime = travelTime + loadTime

        consumedFuel += (loadTime * self.staticFeulConsupmtion)
        tripCost = totalTime * 100 + consumedFuel * 10 + distance * 10

        windows = Machine.getTimeWindows(self, task.startTime,  totalTime)

        if len(windows) <= 0:
            return False, []

        return True,  [SubTask(windows[0][0], windows[0][1], task.location, self, ( loadTime/ 0.2 ) * self.loadCapacity, tripCost)], tripCost
