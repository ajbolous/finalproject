from opmop.models.task import HaulageTask
from opmop.missions.utils import getLocationAtTime, getTimeWindows
from opmop.main import Application

def makeOffer(machine, date, digLocation, dumpLocations,  target):

    bestDump = None
    minDistance = 10000

    for dumpLocation in dumpLocations:
        path, distance = Application.mapping.calcShortestPath(
            dumpLocation.point, digLocation.point)
        if (distance is not -1 and distance < minDistance):
            bestDump = dumpLocation
            minDistance = distance

    if bestDump == None:
        return False, []

    consumedFuel = minDistance * machine.fuelConsumption
    travelTime = minDistance / machine.speed
    averageFillTime = 0.2
    numberOfTravels = target / machine.weightCapacity
    numberOfTravels = max(numberOfTravels, 1)
    numberOfRefeuls = (consumedFuel * numberOfTravels) / machine.fuelCapacity

    tripTime = travelTime + averageFillTime + \
        (numberOfRefeuls * 1) / numberOfTravels

    windows = getTimeWindows(machine, date, tripTime)

    if len(windows) <= 0:
        return False, []

    tripCost = tripTime + consumedFuel * 10 + distance * 10 + \
        averageFillTime * numberOfTravels * machine.staticFuelConsumption

    subtasks = []

    totalTarget = 0
    totalCosts = 0


    for window in windows:
        currentLocation = getLocationAtTime(machine, window[0])

        path, distance = Application.mapping.calcShortestPath(
            currentLocation, digLocation.point)

        stask = HaulageTask('TID', digLocation, bestDump, window[0], window[1], machine.weightCapacity, machine.id, "None")

        totalCosts += distance * machine.fuelConsumption
        subtasks.append(stask)

        numberOfTravels -= 1
        if numberOfTravels == 0:
            break

        totalTarget += machine.weightCapacity
        if totalTarget > target:
            break

    if len(subtasks) > 0:
        return True, subtasks, tripCost * len(subtasks) + totalCosts

    return False, []
