from opmop.models.task import DigTask
from opmop.missions.utils import getLocationAtTime, getTimeWindows
from opmop.main import Application


def makeOffer(machine, schedule):

    path, distance = Application.mapping.calcShortestPath(
        machine.point, schedule.mission.digLocation.point)

    consumedFuel = distance * machine.fuelConsumption
    travelTime = distance / machine.speed

    if schedule.remainingDig <= 0:
        return False, []

    digs = schedule.remainingDig / float(machine.weightCapacity)

    digs = max(digs, 1)
    digTime = digs * 0.2
    digTime = min(digTime, 8)
    digs = (digTime / 0.2)

    totalTime = travelTime + digTime

    consumedFuel += (digTime * machine.staticFuelConsumption)
    tripCost = totalTime * 100 + consumedFuel * 10 + distance * 10

    windows, numOfTasks = getTimeWindows(machine, schedule.date,  totalTime)

    if len(windows) <= 0:
        return False, []

    task = DigTask('{}-{}'.format(schedule.id, 0), schedule.mission.digLocation,
                   windows[0][0], windows[0][1], digs * machine.weightCapacity, machine.id, "None")
    task.actualTarget = None
    return True,  [task], tripCost + 50 * numOfTasks
