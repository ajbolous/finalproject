import opmop.missions.offers.dig as dig
import opmop.missions.offers.load as load
import opmop.missions.offers.haulage as haulage
from opmop.models.machine import Truck, Shovel, Loader


def makeOffer(machine, schedule):
    if isinstance(machine, Truck):
        return haulage.makeOffer(machine, schedule)
    if isinstance(machine, Loader):
        return load.makeOffer(machine, schedule)
    if isinstance(machine, Shovel):
        return dig.makeOffer(machine, schedule)

    return False, None
