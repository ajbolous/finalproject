import opmop.missions.costs as costs
import opmop.missions.routes as routes
import opmop.missions.negotiation as negotiation
import opmop.missions.utils as utils
from opmop.main import Application


def calculateScheduleCost(schedule):
    return costs.getScheduleCost(schedule)


def calculateMachineRoute(machine, date):
    print date
    tasks, count = utils.getMachineSchedule(machine, date.date())
    print tasks
    return {'tasks': [t.toJSON() for t in tasks], 'route': routes.getTasksRoutes(tasks, machine.point)}


def calculateSchedule(mission, schedule, customTarget=None):
    shovels, loaders, trucks = Application.database.getMachinesSorted()
    return negotiation.MASNegotiation(mission, schedule, shovels, loaders, trucks, customTarget)