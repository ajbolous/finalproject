from math import radians, cos, sin, asin, sqrt
from itertools import tee, izip


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon, dlat = lon2 - lon1, lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    km = 6367 * 2 * asin(sqrt(a))
    return km


def getCoordDistance(lng1, lat1, lng2, lat2):
    return haversine(lng1, lat2, lng2, lat2)


def getLocationDistance(l1, l2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    return haversine(l1.lng, l1.lat, l2.lng, l2.lat)


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

def printMission(mission):
    print mission
    for sch in mission.schedules:   
        print "\t ", sch
        for task in sch.tasks:
            print "\t \t", task