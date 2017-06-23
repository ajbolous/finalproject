from opmop.models.task import LoadTask
from opmop.missions.utils import getLocationAtTime, getTimeWindows
from opmop.main import Application

def makeOffer(machine, date, digLocation, target):

    path, distance = Application.mapping.calcShortestPath(
        machine.point, digLocation.point)

    consumedFuel = distance * machine.fuelConsumption
    travelTime = distance / machine.speed

    loads = target / machine.weightCapacity
    loadingTime = loads * 0.2 + 1
    loadingTime = min(loadingTime, 1)
    loads = loadingTime / 0.2

    totalTime = travelTime + loadingTime

    consumedFuel += (loadingTime * machine.staticFuelConsumption)
    tripCost = totalTime * 100 + consumedFuel * 10 + distance * 10

    windows = getTimeWindows(machine, date,  totalTime)

    if len(windows) <= 0:
        return False, []

    task = LoadTask('TID', digLocation, windows[0][0], windows[0][1], loads * machine.weightCapacity, machine.id, "None")
    task.machine = machine
    task.actualTarget = None
    return True,  [task], tripCost
