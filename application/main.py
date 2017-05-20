from database.database import Database
from models.map import Map, MapGraph


class Application():
    database = Database()
    map = Map()
    
    @staticmethod
    def initialize():
        Application.database.load()
        Application.map = Application.database.map
        graph = MapGraph()
        graph.buildGraph(Application.map)

    @staticmethod
    def getMachines():
        return Application.database.getMachines()
    
    @staticmethod
    def getRoads():
        return Application.map.getRoads()


Application.initialize()

Application.database.save()