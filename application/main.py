from database.database import Database
from models.map import Map, MapGraph
from models.mission import Mission
from models.schedule import Schedule
from datetime import datetime


class Application():
    # static properties
    database = Database()
    roadsMap = Map()
    mapping = MapGraph()

    @staticmethod
    def initialize():
        Application.database.load()
        Application.roadsMap.buildFromJson(Application.database.getRoadsJson())
        Application.mapping.buildGraph(Application.roadsMap)


Application.initialize()
