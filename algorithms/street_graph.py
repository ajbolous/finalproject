import networkx as nx
import matplotlib.pyplot as plt
from math import radians, cos, sin, asin, sqrt

#hehehe
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon, dlat = lon2 - lon1, lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    km = 6367 * 2 * asin(sqrt(a))
    return kmz


def addNode(g, nid, lat, lng):
    g.add_node(nid)
    g.node[nid]["lat"] = lat
    g.node[nid]["lng"] = lng


def addEdge(g, vid, uid):
    v = g.node[vid]
    u = g.node[uid]
    w = haversine(v['lng'], v['lat'], u['lng'], u['lat'])
    g.add_edge(vid, uid, weight=w)


def readTxt():
    f = open('points.txt')
    points = []
    for line in f.readlines():
        l = line.split(' ')
        points.append([l[0], float(l[1]), float(l[2])])
    f.close()
    return points


def buildGraph(points):
    i = 0
    addNode(g, i,  points[0][1], points[0][2])
    for point in points[1:]:
        i += 1
        addNode(g, i, point[1], point[2])
        addEdge(g, i - 1, i)


g = nx.Graph()
buildGraph(readTxt())
nx.draw_circular(g)
plt.show()
print nx.astar_path(g, 1, 4)
