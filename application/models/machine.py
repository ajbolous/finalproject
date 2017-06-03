from datetime import datetime, timedelta
import json
from models.task import HaulageTask, LoadTask, DigTask


class Machine():
    def __init__(self, id, model, weight, speed, fuelCapacity,  fuelConsumption, staticFuelConsupmtion, location, isAvailable):
        self.id = id
        self.model = model
        self.weight = weight
        self.speed = speed
        self.fuelCapacity = fuelCapacity
        self.fuelConsumption = fuelConsumption
        self.staticFuelConsupmtion = staticFuelConsupmtion
        self.location = location
        self.isAvailable = isAvailable
        self.tasks = []

    def getLocation(self):
        return self.location

    def getTasks(self):
        return self.tasks

    def getTimeWindows(self, date, size):
        if size <= 0:
            return []

        ws = datetime(year=date.year, month=date.month, day=date.day, hour=9)
        we = ws + timedelta(hours=9)
        windows = []

        if len(self.tasks) == 0:
            for i in range(int(9 / size)):
                windows.append(
                    (ws, ws + timedelta(hours=size), size, self.location))
                ws += timedelta(hours=size)

        tasks = sorted(self.tasks, key=lambda o: o.startTime)

        for task in tasks:
            while True:
                winSize = ((task.startTime - ws).seconds / 3600.0)
                if winSize > size:
                    windows.append(
                        (ws, ws + timedelta(hours=size), size, task.location))
                    ws = ws + timedelta(hours=size)
                else:
                    ws = max(ws, task.endTime)
                    break

        while True:
            winSize = ((we - ws).seconds / 3600.0)
            if winSize > size:
                windows.append(
                    (ws, ws + timedelta(hours=size), size, task.location))
                ws = ws + timedelta(hours=size)
            else:
                break

        return windows

    def makeOffer(self, task, mapGraph):
        pass

    def __repr__(self):
        return "{}({},{})".format(self.__class__, self.id, self.model)

    def toJSON(self):
        return {
            'id': self.id,
            'model': self.model,
            'weight': self.weight,
            'speed': self.speed,
            'fuelCapacity': self.fuelCapacity,
            'fuelConsumption': self.fuelConsumption,
            'staticFuelConsumption': self.staticFuelConsupmtion,
            'location': self.location.toJSON(),
            'tasks': len(self.tasks)
        }


class Truck(Machine):

    def __init__(self, id, model, weight, speed, fuelCapacity, feulConsumption, staticFuelConsupmtion, location, isAvailable, weightCapacity):
        Machine.__init__(self, id, model, weight, speed,
                         fuelCapacity, feulConsumption, staticFuelConsupmtion, location, isAvailable)

        self.weightCapacity = weightCapacity

    def toJSON(self):
        machine = Machine.toJSON(self)
        machine['type'] = 'truck'
        machine['weightCapacity'] = self.weightCapacity
        return machine

    def makeOffer(self, schedule, mapGraph):

        bestDump = None
        minDistance = 1000

        for dumpLocation in schedule.dumpLocations:
            path, distance = mapGraph.calcShortestPath(
                dumpLocation, schedule.digLocation)
            if (distance < minDistance):
                bestDump = dumpLocation
                minDistance = distance

        if bestDump == None:
            return False, []

        consumedFuel = minDistance * self.fuelConsumption
        travelTime = minDistance / self.speed
        averageFillTime = 1
        numberOfTravels = schedule.remainingHaulage / self.weightCapacity
        numberOfTravels = min(numberOfTravels, 1)
        numberOfRefeuls = (consumedFuel * numberOfTravels) / self.fuelCapacity

        tripTime = travelTime + averageFillTime + \
            (numberOfRefeuls * 1) / numberOfTravels

        windows = Machine.getTimeWindows(
            self, schedule.startTime, tripTime)

        if len(windows) <= 0:
            return False, []

        tripCost = tripTime * 100 + consumedFuel * 10 + distance * 10

        subtasks = []

        avgTarget = schedule.target / numberOfTravels

        totalTarget = 0

        for window in windows:

            stask = HaulageTask(schedule.digLocation, bestDump,
                                window[0], window[1], self.weightCapacity, "None")

            subtasks.append(stask)

            numberOfTravels -= 1
            if numberOfTravels == 0:
                break

            totalTarget += avgTarget
            if totalTarget > schedule.remainingHaulage:
                break

        if len(subtasks) > 0:
            return True, subtasks, tripCost * len(subtasks) + 5 * len(self.tasks)

        return False, []


class Shovel(Machine):

    def __init__(self, id, model, weight, speed, fuelCapacity, fuelConsumption, staticFuelConsupmtion, location, isAvailable,  weightCapacity):
        Machine.__init__(self, id, model, weight, speed, fuelCapacity,
                         fuelConsumption, staticFuelConsupmtion, location, isAvailable)

        self.weightCapacity = weightCapacity

    def toJSON(self):
        machine = Machine.toJSON(self)
        machine['type'] = 'shovel'
        machine['weightCapacity'] = self.weightCapacity
        return machine

    def makeOffer(self, schedule, mapGraph):

        path, distance = mapGraph.calcShortestPath(
            self.location, schedule.digLocation)

        consumedFuel = distance * self.fuelConsumption
        travelTime = distance / self.speed

        if schedule.remainingDig <= 0:
            return False, []
        digs = schedule.remainingDig / float(self.weightCapacity)
    
        digs = max(digs, 1)
        digTime = digs * 0.2
        digTime = min(digTime, 8)
        digs = (digTime/0.2)

        totalTime = travelTime + digTime

        consumedFuel += (digTime * self.staticFuelConsupmtion)
        tripCost = totalTime * 100 + consumedFuel * 10 + distance * 10

        windows = Machine.getTimeWindows(self, schedule.startTime,  totalTime)

        if len(windows) <= 0:
            return False, []

        task = DigTask(schedule.digLocation,
                       windows[0][0], windows[0][1], digs * self.weightCapacity, 100)
        task.machine = self
        task.actualTarget = None
        return True,  [task], tripCost + 50 * len(self.tasks)


class Loader(Machine):
    def __init__(self, id, model, weight, speed, fuelCapacity, fulConsumption, staticFuelConsupmtion, location, isAvailable,  weightCapacity):
        Machine.__init__(self, id, model, weight, speed,
                         fuelCapacity, fulConsumption, staticFuelConsupmtion, location, isAvailable)
        self.weightCapacity = weightCapacity

    def toJSON(self):
        machine = Machine.toJSON(self)
        machine['type'] = 'loader'
        machine['weightCapacity'] = self.weightCapacity
        return machine

    def makeOffer(self, schedule, mapGraph):
        path, distance = mapGraph.calcShortestPath(
            self.location, schedule.digLocation)

        consumedFuel = distance * self.fuelConsumption
        travelTime = distance / self.speed

        loads = schedule.remainingLoad / self.weightCapacity
        loadingTime = loads * 0.2 + 1
        loadingTime = min(loadingTime, 1)
        loads = loadingTime / 0.2

        totalTime = travelTime + loadingTime

        consumedFuel += (loadingTime * self.staticFuelConsupmtion)
        tripCost = totalTime * 100 + consumedFuel * 10 + distance * 10

        windows = Machine.getTimeWindows(self, schedule.startTime,  totalTime)

        if len(windows) <= 0:
            return False, []

        task = LoadTask(schedule.digLocation,
                        windows[0][0], windows[0][1], loads * self.weightCapacity, 100)
        task.machine = self
        task.actualTarget = None
        return True,  [task], tripCost - 50 * len(self.tasks)
