from opmop.models.task import LoadTask
from opmop.missions.utils import getLocationAtTime, getTimeWindows
from opmop.main import Application


def makeOffer(machine, schedule):

    path, distance = Application.mapping.calcShortestPath(
        machine.point, schedule.mission.digLocation.point)

    consumedFuel = distance * machine.fuelConsumption
    travelTime = distance / machine.speed

    loads = schedule.remainingLoad / machine.weightCapacity
    loadingTime = loads * 0.1
    loadingTime = max(loadingTime, 1)
    loadingTime = min(loadingTime, 8) - travelTime
    loads = loadingTime / 0.1

    totalTime = travelTime + loadingTime

    consumedFuel += (loadingTime * machine.staticFuelConsumption)
    tripCost = totalTime * 100 + consumedFuel * 10 + distance * 10

    windows, numOfTasks = getTimeWindows(machine, schedule.date,  totalTime)

    if len(windows) <= 0:
        return False, []

    task = LoadTask('{}-{}'.format(schedule.id, 0), schedule.mission.digLocation,
                    windows[0][0], windows[0][1], loads * machine.weightCapacity, machine.id, "None")

    return True,  [task], tripCost + 20 * numOfTasks
