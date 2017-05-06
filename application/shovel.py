from machine import Machine


class Shovel(Machine):


    def __init__(self,digRate,power,id,model,weight,speed,fuelCapacity,fulConsumption,location,isAvailable):
        Machine.__init__(self,id,model,weight,speed,fuelCapacity,fulConsumption,location,isAvailable)
        self.digRate =digRate
        self.power=power
        

    def __repr__(self):
        return "Shovel({},{},{},{},{},{},{},{},{},{})".format(self.id, self.model,self.weight,self.speed,self.fuelCapacity, self.fulConsumption,self.location,self.isAvailable,self.digRate ,self.power)

        
        
        
       
        
        
