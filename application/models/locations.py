class Location():
    def __init__(self, id, name, type, location):
        self.id = id
        self.name = name
        self.type = type
        self.location = location

    def __repr__(self):
        return "Location<{}{}{}{}>".format(self.id, self.name, self.type, self.location)

    def toJSON(self):
        return {
            'type': self.type,
            'name': self.name,
            'id': self.id,
            'location': self.location.toJSON()
        }
