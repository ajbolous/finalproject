import json

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

    def calcPerformance(self):
        pass

    def setOffer(self):
        pass

    def makeOffer(self, task):
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
