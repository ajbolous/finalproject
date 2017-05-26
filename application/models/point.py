class Point():
    def __init__(self, nid, lat, lng):
        self.lat = lat
        self.lng = lng
        self.nid = nid

    def __repr__(self):
        return "Point({}, {}, {})".format(self.nid, self.lat, self.lng)
