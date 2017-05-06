import json
import jsonpickle


class Machine():
    def __init__(self):
        self.id = 1
        self.model = ""

    def __repr__(self):
        return "Machine({},{})".format(self.id, self.model)


class Shovel(Machine):
    def __init__(self):
        Machine.__init__(self)
        self.digRate = 10
        self.height = 1

    def __repr__(self):
        return "Shovel({},{})".format(self.id, self.model)

class Truck(Machine):
    def __init__(self):
        Machine.__init__(self)
        self.loadCapacity = 10
        self.fuel = 10

    def __repr__(self):
        return "Truck({},{})".format(self.id, self.model)




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