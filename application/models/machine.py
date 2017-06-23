from datetime import datetime, timedelta
import json


class Machine():
    def __init__(self, mid, model, weight, speed, fuelCapacity,  fuelConsumption, staticFuelConsupmtion, point, isAvailable):
        self.id = mid
        self.model = model
        self.weight = weight
        self.speed = speed
        self.fuelCapacity = fuelCapacity
        self.fuelConsumption = fuelConsumption
        self.staticFuelConsumption = staticFuelConsupmtion
        self.point = point
        self.isAvailable = isAvailable

    def getLocation(self):
        return self.point

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
            'staticFuelConsumption': self.staticFuelConsumption,
            'point': self.point.toJSON(),
        }


class Truck(Machine):

    def __init__(self, mid, model, weight, speed, fuelCapacity, feulConsumption, staticFuelConsupmtion, location, isAvailable, weightCapacity):
        Machine.__init__(self, mid, model, weight, speed,
                         fuelCapacity, feulConsumption, staticFuelConsupmtion, location, isAvailable)

        self.weightCapacity = weightCapacity

    def toJSON(self):
        machine = Machine.toJSON(self)
        machine['type'] = 'truck'
        machine['weightCapacity'] = self.weightCapacity
        return machine


class Shovel(Machine):

    def __init__(self, mid, model, weight, speed, fuelCapacity, fuelConsumption, staticFuelConsupmtion, location, isAvailable,  weightCapacity):
        Machine.__init__(self, mid, model, weight, speed, fuelCapacity,
                         fuelConsumption, staticFuelConsupmtion, location, isAvailable)

        self.weightCapacity = weightCapacity

    def toJSON(self):
        machine = Machine.toJSON(self)
        machine['type'] = 'shovel'
        machine['weightCapacity'] = self.weightCapacity
        return machine


class Loader(Machine):
    def __init__(self, mid, model, weight, speed, fuelCapacity, fulConsumption, staticFuelConsupmtion, location, isAvailable,  weightCapacity):
        Machine.__init__(self, mid, model, weight, speed,
                         fuelCapacity, fulConsumption, staticFuelConsupmtion, location, isAvailable)
        self.weightCapacity = weightCapacity

    def toJSON(self):
        machine = Machine.toJSON(self)
        machine['type'] = 'loader'
        machine['weightCapacity'] = self.weightCapacity
        return machine
