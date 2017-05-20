from database.database import Database
from models.map import Map, MapGraph


class Application():
    #static properties
    database = Database()
    map = Map()
    graph = None

    @staticmethod
    def initialize():
        Application.database.load()
        Application.map = Application.database.map
        Application.graph = MapGraph()
        Application.graph.buildGraph(Application.map)

    @staticmethod
    def getMachines():
        return Application.database.getMachines()

    @staticmethod
    def getRoads():
        return Application.map.getRoads()


    @staticmethod
    def calc():
        return Application.graph._calcShortestPath(1,57)



Application.initialize()

Application.database.save()
print Application.calc()