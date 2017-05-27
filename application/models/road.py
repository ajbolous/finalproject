import json


class Road():
    def __init__(self, rid, name, rType):
        self.id = rid
        self.name = name
        self.type = rType
        self.points = []

    def addPoint(self, point):
        self.points.append(point)

    def getPoints(self):
        return self.points

    def setPoints(self, points):
        self.points = points

    def __repr__(self):
        return "Road({}, {}, {})".format(self.id, self.name, len(self.points))

    def toJSON(self):
        return {'id': self.id, 'name': self.name, 'type': self.type, 'points': [p.toJSON() for p in self.points]}
