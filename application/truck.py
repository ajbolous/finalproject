from machine import Machine
class Truck(Machine):
    def __init__(self,loadCapacity,weightCapacity,id,model,weight,speed,fuelCapacity,fulConsumption,location,isAvailable):
        Machine.__init__(self,id,model,weight,speed,fuelCapacity,fulConsumption,location,isAvailable)
        self.loadCapacity =loadCapacity
        self.weightCapacity=weightCapacity


    def __repr__(self):
        return "Truck({},{},{},{},{},{},{},{},{},{})".format(self.id, self.model, self.weight, self.speed,self.fuelCapacity,self.fulConsumption ,self.location, self.isAvailable,self.loadCapacity ,self.weightCapacity)

        
    
        
        
        
       

