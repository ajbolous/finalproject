from opmop.models.task import HaulageTask
import opmop.missions.utils as utils
from opmop.main import Application


def makeOffer(machine, schedule):

    bestDump = None
    minDistance = 10000

    for dumpLocation in schedule.mission.dumpLocations:
        path, distance = Application.mapping.calcShortestPath(
            dumpLocation.point, schedule.mission.digLocation.point)
        if (distance is not -1 and distance < minDistance):
            bestDump = dumpLocation
            minDistance = distance

    if bestDump == None:
        return False, []

    consumedFuel = minDistance * machine.fuelConsumption
    travelTime = minDistance / (machine.speed/4)
    averageFillTime = 0.2
    numberOfTravels = 1
    numberOfRefeuls = (consumedFuel * numberOfTravels) / machine.fuelCapacity

    tripTime = 2*travelTime + averageFillTime + (numberOfRefeuls * 1)

    windows, numOfTasks = utils.getTimeWindows(
        machine, schedule.date, tripTime)

    if len(windows) <= 0:
        return False, []

    tripCost = tripTime + consumedFuel * 10 + distance * 10 + \
        averageFillTime * numberOfTravels * machine.staticFuelConsumption


    totalTarget = 0
    totalCosts = 0

    minWindowCost = 9999999
    bestWindow = None

    for window in windows:

        currentLocation = utils.getLocationAtTime(machine, window[0])

        numOfHaulers = utils.getNumberOfHaulers(schedule, window)
        wasteAtTime = utils.getWasteAtTime(schedule, window[0])

        if(numOfHaulers < 1 and wasteAtTime > machine.weightCapacity):
            path, distance = Application.mapping.calcShortestPath(
                currentLocation, schedule.mission.digLocation.point)

            windowCost = distance * machine.fuelConsumption + 20 * numOfHaulers

            if windowCost < minWindowCost:
                bestWindow = window
                minWindowCost = windowCost

    if bestWindow == None:
        return False, []

    task = HaulageTask('{}-{}'.format(schedule.id, numberOfTravels), schedule.mission.digLocation,
                       bestDump, bestWindow[0], bestWindow[1], machine.weightCapacity, machine.id, "None")

    return True, [task], windowCost + totalCosts + numOfTasks * 50
