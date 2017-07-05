from opmop.models.point import Point
from opmop.models.road import Road
import json
import opmop.mapping.utils as utils


class Map():
    def __init__(self):
        self.roads = []

    def getRoads(self):
        return self.roads

    def getPointById(self, nid):
        for road in self.roads:
            for point in road.points:
                if point.nid == nid:
                    return point
        return None


    def addRoad(self, points):
        r = Road(len(self.roads), 'R', 'dirt')
        points = sorted(points, key=lambda el: el['index'])
        for p in points:
            r.addPoint(Point(p['index'], p['nid'], p['lat'], p['lng']))
        self.roads.append(r)

    def buildRoads(self, roads):
        threshold = 0.01
        for road in roads:
            for point in road:
                for road2 in roads:
                    for point2 in road2:
                        if point == point2:
                            continue
                        dist = utils.haversine(
                            point['lat'], point['lng'], point2['lat'], point2['lng'])
                        if dist < threshold:
                            point['lat'] = point2['lat']
                            point['lng'] = point2['lng']

            self.addRoad(road)

    def buildFromJson(self, jsonData):
        self.buildRoads(jsonData)

    def getClosestPoint(self, lat, lng):
        minDist = 999999
        minPoint = None
        for road in self.roads:
            for point in road.getPoints():
                dist = utils.getCoordDistance(point.lng, point.lat, lat, lng)
                if dist < minDist:
                    minDist = dist
                    minPoint = point
        return minPoint
