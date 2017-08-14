from opmop.models.schedule import Schedule
from opmop.missions.offers.offer import makeOffer
from datetime import datetime, timedelta
from opmop.models.task import LoadTask, DigTask, HaulageTask
from opmop.main import Application
import opmop.missions.utils as utils


def getMaxOffer(machines, schedule):
    maxOffer, maxMachine = None, None
    for machine in machines:
        offer = makeOffer(machine, schedule)
        if offer[0] == False:
            continue
        if maxOffer == None:
            maxOffer = offer
            maxMachine = machine
        elif maxOffer[2] >= offer[2]:
            maxOffer = offer
            maxMachine = machine

    return maxOffer, maxMachine


def MASNegotiation(mission, schedule, shovels, loaders, trucks, custromTarget=None):

    schedule.tasks = []
    schedule.updateRemaining()

    while schedule.remainingDig > 0:
        maxOffer, maxMachine = getMaxOffer(shovels, schedule)
        if maxOffer is None:
            break
        for task in maxOffer[1]:
            schedule.addTask(task)
        schedule.updateRemaining()

    schedule.updateRemaining()
    while schedule.remainingLoad > 0:
        maxOffer, maxMachine = getMaxOffer(loaders, schedule)
        if maxOffer is None:
            break
        for task in maxOffer[1]:
            schedule.addTask(task)

        schedule.updateRemaining()
    schedule.updateRemaining()

    while schedule.remainingHaulage > 0:
        maxOffer, maxMachine = getMaxOffer(trucks, schedule)
        if maxOffer is None:
            break

        for task in maxOffer[1]:
            schedule.addTask(task)
        schedule.updateRemaining()

    schedule.updateRemaining()

    return schedule


def getBestMachine(machines, usedMachines):
    bestMachine = None
    for machine in machines:
        if machine not in usedMachines and bestMachine == None:
            bestMachine = machine
        elif machine not in usedMachines and machine.fuelConsumption < bestMachine.fuelConsumption:
            bestMachine = machine

    return bestMachine

def greedyAllocation(schedule, shovels, loaders, trucks):
    import random
    startTime = datetime(schedule.date.year, schedule.date.month,
                         schedule.date.day, hour=9, minute=0, second=0)
    schedule.tasks = []
    schedule.updateRemaining()

    maxDigTime = 0

    usedShovels = {}
    while True:
        shovel = getBestMachine(shovels,usedShovels)
        
        if shovel is None:
            break   

        usedShovels[shovel] = True


        digTime = (schedule.remainingDig / shovel.weightCapacity) * 0.2
        digTime = min(digTime, 9)

        if digTime < 1:
            continue

        maxDigTime = max(digTime,maxDigTime)

        t = DigTask('{}-{}'.format(schedule.id, shovel.id), schedule.mission.digLocation, startTime, (startTime +
                                                                                                      timedelta(hours=digTime)), shovel.weightCapacity * digTime * 5, shovel.id)
        schedule.addTask(t)
        schedule.updateRemaining()

        if schedule.remainingDig <= 0:
            break


    usedLoaders = {}
    while True:
        loader = getBestMachine(loaders, usedLoaders)

        if loader is None:
            break

        usedLoaders[loader] = True

        loadTime = (schedule.remainingLoad / loader.weightCapacity) * 0.2
        loadTime = min(loadTime, 9)
        loadTime = min(loadTime,maxDigTime)

        if loadTime < 1:
            continue

        t = LoadTask('{}-{}'.format(schedule.id, loader.id), schedule.mission.digLocation, startTime,  (startTime +
                                                                                                        timedelta(hours=loadTime)), (loader.weightCapacity * loadTime * 5), loader.id)
        schedule.addTask(t)
        schedule.updateRemaining()
        if schedule.remainingLoad <= 0:
            break

    usedTrucks = {}
    taskStartTime = startTime
    while True:

        truck = getBestMachine(trucks, usedTrucks)

        if truck is None:
            break

        usedTrucks[truck] = True

        path, distance = Application.mapping.calcShortestPath(
            schedule.mission.digLocation.point, schedule.mission.dumpLocations[0].point)

        path, distance2 = Application.mapping.calcShortestPath(truck.point, schedule.mission.digLocation.point)

        time = ( (distance + distance2) / float(truck.speed)) + 0.2

        t = HaulageTask('{}-{}'.format(schedule.id, truck.id), schedule.mission.digLocation, schedule.mission.dumpLocations[0], taskStartTime, (
            taskStartTime + timedelta(hours=time)), truck.weightCapacity, truck.id)

        taskStartTime += timedelta(hours=time + (maxDigTime/8),)

        if taskStartTime.hour > (maxDigTime + 9):
            break

        schedule.addTask(t)
        schedule.updateRemaining()
        if schedule.remainingHaulage <= 0:
            break

        if schedule.remainingHaulage <= 0:
            break

    return schedule




def randomAllocation(schedule, shovels, loaders, trucks):
    import random
    startTime = datetime(schedule.date.year, schedule.date.month,
                         schedule.date.day, hour=9, minute=0, second=0)
    schedule.tasks = []
    schedule.updateRemaining()

    maxDigTime = 0
    for _ in shovels:
        shovel = shovels[random.randint(0, len(shovels) - 1)]

        digTime = (schedule.remainingDig / shovel.weightCapacity) * 0.2
        digTime = min(digTime, 9)

        if digTime < 1:
            continue
        maxDigTime = max(digTime,maxDigTime)

        t = DigTask('{}-{}'.format(schedule.id, shovel.id), schedule.mission.digLocation, startTime, (startTime +
                                                                                                      timedelta(hours=digTime)), shovel.weightCapacity * digTime * 5, shovel.id)
        schedule.addTask(t)
        schedule.updateRemaining()
        if schedule.remainingDig <= 0:
            break

    for loader in loaders:

        loadTime = (schedule.remainingLoad / loader.weightCapacity) * 0.2
        loadTime = min(loadTime, 9)
        loadTime = min(loadTime,maxDigTime)
        if loadTime < 1:
            continue

        t = LoadTask('{}-{}'.format(schedule.id, loader.id), schedule.mission.digLocation, startTime,  (startTime +
                                                                                                        timedelta(hours=loadTime)), (loader.weightCapacity * loadTime * 5), loader.id)
        schedule.addTask(t)
        schedule.updateRemaining()
        if schedule.remainingLoad <= 0:
            break

    while True:
        noneSelected = True
        taskStartTime = startTime

        for truck in trucks:
            path, distance = Application.mapping.calcShortestPath(
                schedule.mission.digLocation.point, schedule.mission.dumpLocations[0].point)

            path, distance2 = Application.mapping.calcShortestPath(truck.point, schedule.mission.digLocation.point)

            time = ( (distance + distance2) / float(truck.speed)) + 0.2

            t = HaulageTask('{}-{}'.format(schedule.id, truck.id), schedule.mission.digLocation, schedule.mission.dumpLocations[0], taskStartTime, (
                taskStartTime + timedelta(hours=time)), truck.weightCapacity, truck.id)

            taskStartTime += timedelta(hours=time + (maxDigTime/8),)

            if taskStartTime.hour > (maxDigTime + 9):
                break

            schedule.addTask(t)
            schedule.updateRemaining()
            if schedule.remainingHaulage <= 0:
                break

        if schedule.remainingHaulage <= 0:
            break

        if noneSelected:
            break

    return schedule
