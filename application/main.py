from database.database import Database
from models.map import Map, MapGraph


class Application():
    # static properties
    database = Database()
    map = Map()
    graph = None

    @staticmethod
    def initialize():
        Application.database.load()
        Application.map = Application.database.map
        Application.graph = MapGraph()
        Application.graph.buildGraph(Application.map)
        Application.graph.drawMap()
    @staticmethod
    def getMachines():
        return Application.database.getMachines()

    @staticmethod
    def getRoads():
        return Application.map.getRoads()

    @staticmethod
    def calc():
        return Application.graph._calcShortestPath(1, 57)

    @staticmethod
    def negotiation():
        machine = Application.database.getMachines()[47]

        mission = Application.database.getMissions()[0]

        sched = mission.getSchedules()[0]
        print machine
        for task in sched.getTasks():
            machine.makeOffer(task, Application.graph)


Application.initialize()

Application.negotiation()

Application.database.save()
