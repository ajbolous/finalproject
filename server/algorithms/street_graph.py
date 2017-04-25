import networkx as nx
import matplotlib.pyplot as plt
from math import radians, cos, sin, asin, sqrt
import json
import os 

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


def addNode(g, nid, lat, lng):
    g.add_node(nid)
    g.node[nid]["lat"] = lat
    g.node[nid]["lng"] = lng


def addEdge(g, vid, uid):
    v = g.node[vid]
    u = g.node[uid]
    w = haversine(v['lng'], v['lat'], u['lng'], u['lat'])
    g.add_edge(vid, uid, weight=w)


def readJson():
    global roads
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '/roads.json') as data_file:
        roads = json.load(data_file)
        return roads


def connectRoadsMap():
    i, j = 0, 0
    mdist = 0.008
    count = 0
    for i in range(len(roads)):
        for j in range(i + 1, len(roads)):
            for n1 in roads[i]:
                for n2 in roads[j]:
                    dist = haversine(n1['lat'], n1['lng'],
                                     n2['lat'], n2['lng'])
                    if dist < mdist:
                        n1['lat'], n1['lng'] = n2['lat'], n2['lng']


def connectRoads():
    i = 0
    nodes = g.nodes()
    mdist = 0.008
    count = 0
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            n1 = g.node[nodes[i]]
            n2 = g.node[nodes[j]]
            dist = haversine(n1['lat'], n1['lng'], n2['lat'], n2['lng'])
            if dist < mdist:
                addEdge(g, nodes[i], nodes[j])
                n1['lat'], n1['lng'] = n2['lat'], n2['lng']


def buildGraph():
    roads = readJson()
    g = nx.Graph()
    for road in roads:
        buildRoad(road)
    connectRoads()
    connectRoadsMap()


def buildRoad(points):
    i = g.number_of_nodes()
    addNode(g, i,  points[0]['lat'], points[0]['lng'])
    for point in points[1:]:
        i += 1
        addNode(g, i, point['lat'], point['lng'])
        addEdge(g, i - 1, i)


def getNode(id):
    return g.node[id]


def getRoadsNodes():
    return roads


def drawRoads():
    pos = {}
    for node in g.nodes():
        pos[node] = (g.node[node]['lat'],  g.node[node]['lng'])
    nx.draw(g, pos, node_size=20)
    plt.show()


def calcShortestPath(source, target):
    path = []
    for node in nx.dijkstra_path(g, source, target):
        path.append({'lat': g.node[node]['lat'], 'lng': g.node[node]['lng']});
    return path


roads = []
g = nx.Graph()
buildGraph()
