import opmop.missions.costs as costs
import opmop.missions.routes as routes
import opmop.missions.negotiation as negotiation
import opmop.missions.utils as utils
from opmop.main import Application
import copy

def calculateScheduleCost(schedule):
    return costs.getScheduleCost(schedule)


def calculateMachineRoute(machine, date):
    tasks, count = utils.getMachineSchedule(machine, date.date())
    return {'route': routes.getTasksRoutes(tasks, machine.point)}


def calculateSchedule(mission, schedule, customTarget=None):
    shovels, loaders, trucks = Application.database.getMachinesSorted()

    schedCopy = copy.copy(schedule)
    masSchedule =  negotiation.MASNegotiation(mission, schedule, shovels, loaders, trucks, customTarget)
    randSchedule = negotiation.randomAllocation(schedCopy, shovels, loaders,trucks)

    masCost = calculateScheduleCost(masSchedule)
    randCost = calculateScheduleCost(randSchedule)

    schedule = masSchedule

    return masSchedule, masCost, randSchedule, randCost