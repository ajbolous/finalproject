from models.task import HaulageTask, LoadTask, DigTask
from application.main import Application

def getScheduleCost(schedule):
    cost = {
        'machines': getScheduleCostPerMachine(schedule),
        'total': 0
    }

def getScheduleCostPerMachine(schedule):
    machines = {}
    for task in schedule.tasks:
        cost = 0
        loc = task.machine.getLocationAtTime(task.startTime)
        path, distance = Application.mapping.calcShortestPath(
            loc, task.location.location)
        cost += distance * task.machine.fuelConsumption
        if isinstance(task, HaulageTask):
            path, distance = Application.mapping.calcShortestPath(
                task.location.location, task.dumpLocation.location)
            cost += distance * task.machine.fuelConsumption
            cost += 0.2 * task.machine.staticFuelConsumption

        else:
            time = (task.endTime - task.startTime).seconds // 3600
            cost += time * task.machine.staticFuelConsumption

        t = task.toJSON()
        t['cost'] = cost
        if task.machine.id not in machines:
            machines[task.machine.id] = {
                'tasks': [t],
                'machine': task.machine.toJSON(),
                'total': cost
            }
        else:
            machines[task.machine.id]['tasks'].append(t)
            machines[task.machine.id]['total'] += cost

    return machines
