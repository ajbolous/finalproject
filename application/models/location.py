class Location():
    def __init__(self, id, name, type, point):
        self.id = id
        self.name = name
        self.type = type
        self.point = point

    def __repr__(self):
        return "Location<{},{},{}>".format(self.id, self.name, self.type)

    def toJSON(self):
        return {
            'type': self.type,
            'name': self.name,
            'id': self.id,
            'point': self.point.toJSON()
        }
