from opmop.models.task import DigTask
from opmop.missions.utils import getLocationAtTime, getTimeWindows
from opmop.main import Application

def makeOffer(machine, date, digLocation, target):


    path, distance = Application.mapping.calcShortestPath(
        machine.point, digLocation.point)

    consumedFuel = distance * machine.fuelConsumption
    travelTime = distance / machine.speed

    if target <= 0:
        return False, []
    digs = target / float(machine.weightCapacity)

    digs = max(digs, 1)
    digTime = digs * 0.2
    digTime = min(digTime, 8)
    digs = (digTime / 0.2)

    totalTime = travelTime + digTime

    consumedFuel += (digTime * machine.staticFuelConsumption)
    tripCost = totalTime * 100 + consumedFuel * 10 + distance * 10

    windows = getTimeWindows(machine, date,  totalTime)

    if len(windows) <= 0:
        return False, []

    task = DigTask('TID', digLocation,windows[0][0], windows[0][1], digs * machine.weightCapacity, machine.id, "None")
    task.actualTarget = None
    return True,  [task], tripCost + 50
