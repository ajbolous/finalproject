import opmop.missions.costs as costs
import opmop.missions.routes as routes
import opmop.missions.negotiation as negotiation
import opmop.missions.utils as utils
from opmop.main import Application

def calculateScheduleCost(schedule):
    return costs.getScheduleCost(schedule)

def calculateMachineRoute(machine, date):
    tasks = utils.getMachineSchedule(machine, date)
    return routes.getTasksRoutes(tasks, machine.point)

def calculateSchedule(mission, schedule, customTarget=None):
    shovels, loaders, trucks = Application.database.getMachinesSorted()
    return negotiation.MASNegotiation(mission, schedule, shovels, loaders, trucks, customTarget)

