import networkx as nx
import opmop.mapping.utils as utils


class MapGraph():
    def __init__(self):
        self.graph = nx.Graph()

    def addNode(self, p):
        self.graph.add_node(p.nid, point=p)

    def addEdge(self, p1, p2):
        w = utils.getCoordDistance(p1.lng, p1.lat, p2.lng, p2.lat)
        self.graph.add_edge(p1.nid, p2.nid, weight=w)

    def buildGraph(self, map):
        for road in map.roads:
            points = road.getPoints()
            points = sorted(points, key=lambda el: el.index)
            self.addNode(points[0])
            for i in range(1, len(points)):
                self.addNode(points[i])
                self.addEdge(points[i - 1], points[i])
                self.addEdge(points[i], points[i - 1])

        self.connectGraph()

    def connectGraph(self):
        threshold = 0.01
        for p1 in self.graph.nodes():
            for p2 in self.graph.nodes():
                if p1 != p2:
                    point1 = self.graph.node[p1]['point']
                    point2 = self.graph.node[p2]['point']
                    dist = utils.haversine(
                        point1.lng, point1.lat, point2.lng, point2.lat)
                    if dist <= threshold:
                        self.addEdge(point1, point2)

        dist = nx.all_pairs_dijkstra_path(self.graph)
        for k1 in dist:
            for k2 in dist:
                if k2 not in dist[k1]:
                    continue

    def drawMap(self):
        pos = {}
        for node in self.graph.nodes():
            pos[node] = (self.graph.node[node]['point'].lat,
                         self.graph.node[node]['point'].lng)
        nx.draw(self.graph, pos, node_size=20, with_labels=True)
        import matplotlib.pyplot as plt
        plt.show()

    def _calcShortestPath(self, source, dest):
        path = []
        w = 0
        try:
            shortestPath = nx.dijkstra_path(self.graph, source, dest)
        except Exception as e:
            print "Didnt find a path", e
            return None, -1

        for i in range(len(shortestPath) - 1):
            w += self.graph[shortestPath[i]][shortestPath[i + 1]]['weight']

        for node in shortestPath:
            path.append(self.graph.node[node]['point'])
        return path, w

    def calcShortestPath(self, source, dest):
        return self._calcShortestPath(source.nid, dest.nid)
