import dig
import load
import haulage
from models.machine import Truck, Shovel, Loader


def makeOffer(machine, schedule, target):
    if isinstance(machine, Truck):
        return haulage.makeOffer(machine, schedule.date, schedule.mission.digLocation, schedule.mission.dumpLocations, target)
    if isinstance(machine, Loader):
        return load.makeOffer(machine, schedule.date, schedule.mission.digLocation, target)
    if isinstance(machine, Shovel):
        return dig.makeOffer(machine, schedule.date, schedule.mission.digLocation, target)

    return False, None
