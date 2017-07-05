from opmop.models.task import HaulageTask, LoadTask, DigTask
from opmop.main import Application
from opmop.missions import utils as utils

def getScheduleCost(schedule):
    
    machinesCost = getScheduleCostPerMachine(schedule);
    totalCost = 0
    for machine in machinesCost:
        totalCost+= machinesCost[machine]['total'] 

    cost = {
        'machines': machinesCost,
        'total': totalCost
    }

    return cost

def getScheduleCostPerMachine(schedule):
    machines = {}
    for task in schedule.tasks:
        cost = 0
        machine = Application.database.getMachineById(task.machineId)
        loc = utils.getLocationAtTime(machine, task.startTime)
        path, distance = Application.mapping.calcShortestPath(loc, task.location.point)
        if distance < 0:
            distance = -1 * distance
        cost += distance * machine.fuelConsumption
        if isinstance(task, HaulageTask):
            path, distance = Application.mapping.calcShortestPath(
                task.location.point, task.dumpLocation.point)
            
            cost += distance * machine.fuelConsumption
            cost += 0.2 * machine.staticFuelConsumption

        else:
            time = (task.endTime - task.startTime).seconds // 3600
            if time < 0:
                time = -1 * time
            cost += time * machine.staticFuelConsumption

        t = task.toJSON()
        t['cost'] = cost
        if machine.id not in machines:
            machines[machine.id] = {
                'tasks': [t],
                'machine': machine.toJSON(),
                'total': cost
            }
        else:
            machines[machine.id]['tasks'].append(t)
            machines[machine.id]['total'] += cost

    return machines
