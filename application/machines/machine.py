class Machine():
    def __init__(self,id,model,weight,speed,fuelCapacity,fulConsumption,location,isAvailable):
        self.id =id
        self.model =model
        self.weight=weight
        self.speed=speed
        self.fuelCapacity=fuelCapacity
        self.fulConsumption=fulConsumption
        self.location=location
        self.isAvailable=isAvailable


    def calcPerformance(self):
        pass
    def setOffer(self):
        pass
    def getOffer(self):
        pass


    def __repr__(self):
        return "Machine({},{})".format(self.id, self.model)
