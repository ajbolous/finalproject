from database.database import Database
from models.map import Map, MapGraph
from models.mission import Mission, Schedule
from datetime import datetime
from algorithms.routes import getTasksRoutes


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
    def getMission():
        return Application.database.getMissions()[0]

    @staticmethod
    def getLocations():
        return Application.database.getLocations()

    @staticmethod
    def calc():
        return Application.graph._calcShortestPath(1, 57)

    @staticmethod
    def getMaxOffer(machines, schedule):
        maxOffer, maxMachine = None, None
        for machine in machines:
            offer = machine.makeOffer(schedule, Application.graph)
            if offer[0] == False:
                continue
            if maxOffer == None:
                maxOffer = offer
                maxMachine = machine
            elif maxOffer[2] >= offer[2]:
                maxOffer = offer
                maxMachine = machine

        return maxOffer, maxMachine

    @staticmethod
    def getRoutes():
        machine = Application.getMachines()[13]
        return getTasksRoutes(machine.tasks, machine.location, Application.graph)

    @staticmethod
    def negotiation():
        shovels, loaders, trucks = Application.database.getMachinesSorted()
        mission = Application.database.getMissions()[0]

        schedule = mission.createNextSchedule()
        schedule.updateRemaining()

        print schedule.remainingDig, schedule.remainingLoad, schedule.remainingHaulage

        while schedule.remainingDig > 0:
            schedule.updateRemaining()
            maxOffer, maxMachine = Application.getMaxOffer(shovels, schedule)
            if maxOffer is None:
                break
            for task in maxOffer[1]:
                schedule.addTask(task)
                maxMachine.tasks.append(task)
            print maxOffer, maxMachine

        print schedule.remainingDig, schedule.remainingLoad, schedule.remainingHaulage

        while schedule.remainingLoad > 0:
            schedule.updateRemaining()
            maxOffer, maxMachine = Application.getMaxOffer(loaders, schedule)
            if maxOffer is None:
                break
            for task in maxOffer[1]:
                schedule.addTask(task)
                maxMachine.tasks.append(task)
            print maxOffer, maxMachine

        print schedule.remainingDig, schedule.remainingLoad, schedule.remainingHaulage

        while schedule.remainingHaulage >= 0:
            maxOffer, maxMachine = Application.getMaxOffer(trucks, schedule)

            if maxOffer is None:
                break
            for task in maxOffer[1]:
                schedule.addTask(task)
                maxMachine.tasks.append(task)
                task.machine = maxMachine
            schedule.updateRemaining()

        schedule.updateRemaining()
        print schedule.remainingDig, schedule.remainingLoad, schedule.remainingHaulage

        for machine in trucks:
            print machine.id, len(machine.tasks)


Application.initialize()
Application.negotiation()
