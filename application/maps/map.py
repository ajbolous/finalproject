import networkx as nx
import os
from location import Location
from road import Road
import json
import utils


class Map():
    def __init__(self):
        self.roads = []
        self.locations = []
        self.graph = nx.Graph()

    def addEdge(self, l1, l2):
        w = utils.getLocationDistance(l1, l2)
        self.graph.add_edge(l1.nid, l2.nid, weight=w)

    def addLocation(self, lng, lat):
        id = self.graph.number_of_nodes() + 1
        l = Location(lat, lng, id)
        self.locations.append(l)
        self.graph.add_node(id)
        self.graph.node[id]['location'] = l
        return l

    def addRoad(self, road):
        r = Road(len(self.roads), 'R', [])
        prevL = self.addLocation(road[0]['lat'], road[0]['lng'] )
        r.addLocation(prevL)

        for point in road[1:]:
            location = self.addLocation(point['lat'], point['lng'])
            r.addLocation(location)
            self.addEdge(prevL, location)
            prevL = location

        self.roads.append(r)
        return r

    def loadFromJson(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + '/roads.json') as data:
            roads = json.load(data)
            roads = self.connectRoads(roads)
            for road in roads:
                self.addRoad(road)

    def connectRoads(self, roads):
        i, j = 0, 0
        mdist = 0.008
        count = 0
        for i in range(len(roads)):
            for j in range(i + 1, len(roads)):
                for n1 in roads[i]:
                    for n2 in roads[j]:
                        dist = utils.haversine(
                            n1['lat'], n1['lng'], n2['lat'], n2['lng'])
                        if dist < mdist:
                            n1['lat'], n1['lng'] = n2['lat'], n2['lng']
        return roads

    def drawRoads(self):
        pos = {}
        for node in self.graph.nodes():
            pos[node] = (self.graph.node[node]['location'].lat,
                         self.graph.node[node]['location'].lng)
        nx.draw(self.graph, pos, node_size=20)
        import matplotlib.pyplot as plt
        plt.show()

    def calcShortestPath(self, source, target):
        path = []
        for node in nx.dijkstra_path(self.graph, source, target):
            path.append(self.graph.node[node]['location'])
        return path


m = Map()
m.loadFromJson()
m.drawRoads()
