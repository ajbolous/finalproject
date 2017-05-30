from database.database import Database
from models.map import Map, MapGraph


class Application():
    # static properties
    database = Database()
    map = Map()
    graph = MapGraph()

    @staticmethod
    def initialize():
        Application.database.load()
        Application.map.loadFromJson()
        Application.graph.buildGraph(Application.map)

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
        machines = Application.database.getMachines()

        mission = Application.database.getMissions()[0]

        sched = mission.getSchedules()[0]
        offers = []
        for task in sched.getTasks():
            remaining = task.amount
            while remaining>0:
                maxOffer = None
                for machine in machines:
                    offer = machine.makeOffer(task, Application.graph)
                    if offer[0] == False:
                        continue
                    if maxOffer == None:
                        maxOffer = offer
                    elif maxOffer[2] > offer[2]:
                        maxOffer = offer

                if maxOffer == None:
                    print "Didnt allocate all, remaining {}".format(remaining)
                    break

                for stask in maxOffer[1]:
                    stask.machine.tasks.append(stask)
                    remaining-= stask.amount

Application.initialize()

Application.negotiation()

for machine in Application.database.getMachines():
    print machine, machine.getTasks()
Application.database.save()