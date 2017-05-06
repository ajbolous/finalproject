import jsonpickle


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


    def __repr__(self):
        return "Machine({},{})".format(self.id, self.model)

    

def calcPerformance(self):
        pass
def setOffer(self):
        pass
def getOffer(self):
    pass

def save(data, filename):
    with open(filename, 'w') as fp:
        js = jsonpickle.encode(data)
        fp.write(js)


def load(filename):
    with open(filename) as fp:
        data = fp.read()
        return jsonpickle.decode(data)

machines = load('machines.json')
print machines