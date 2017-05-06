class Road():
    def __init__(self, rid, name, locations):
        self.id = rid
        self.name = name
        self.locations = locations

    def addLocation(self, location):
        self.locations.append(location)

    def __repr__(self):
        return "Road({}, {}, {})".format(self.id, self.name, len(self.locations))
