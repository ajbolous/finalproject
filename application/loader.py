from machine import Machine

class Loader(Machine):
    def __init__(self,weightCapacity,loadCapacity,id,model,weight,speed,fuelCapacity,fulConsumption,location,isAvailable ):
        Machine.__init__(self,id,model,weight,speed,fuelCapacity,fulConsumption,location,isAvailable )
        self.weightCapacity=weightCapacity
        self.loadCapacity=loadCapacity


     