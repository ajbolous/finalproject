import json


class Point():
    def __init__(self, idx, nid, lat, lng):
        self.lat = lat
        self.lng = lng
        self.nid = nid
        self.index = idx

    def __repr__(self):
        return "Point({}, {}, {})".format(self.nid, self.lat, self.lng)

    def toJSON(self):
        return {'index': self.index, 'nid': self.nid, 'lat': self.lat, 'lng': self.lng}
