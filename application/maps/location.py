class Location():
    def __init__(self, lat,lng, nid):
        self.lat = lat
        self.lng = lng 
        self.nid = nid

    def __repr__(self):
        return "Location({}, {}, {})".format(self.nid, self.lat, self.lng)

