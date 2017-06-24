from opmop.models.schedule import Schedule
from opmop.missions.offers.offer import makeOffer


def getMaxOffer(machines, schedule):
    maxOffer, maxMachine = None, None
    for machine in machines:
        offer = makeOffer(machine, schedule)
        if offer[0] == False:
            continue
        if maxOffer == None:
            maxOffer = offer
            maxMachine = machine
        elif maxOffer[2] >= offer[2]:
            maxOffer = offer
            maxMachine = machine

    return maxOffer, maxMachine


def MASNegotiation(mission, schedule, shovels, loaders, trucks, custromTarget=None):

    schedule.tasks = []
    schedule.updateRemaining()

    while schedule.remainingDig > 0:
        maxOffer, maxMachine = getMaxOffer(shovels, schedule)
        if maxOffer is None:
            break
        for task in maxOffer[1]:
            schedule.addTask(task)
        schedule.updateRemaining()

    schedule.updateRemaining()
    while schedule.remainingLoad > 0:
        maxOffer, maxMachine = getMaxOffer(loaders, schedule)
        if maxOffer is None:
            break
        for task in maxOffer[1]:
            schedule.addTask(task)

        schedule.updateRemaining()
    schedule.updateRemaining()

    while schedule.remainingHaulage > 0:
        maxOffer, maxMachine = getMaxOffer(trucks, schedule)
        if maxOffer is None:
            break

        for task in maxOffer[1]:
            schedule.addTask(task)
        schedule.updateRemaining()

    schedule.updateRemaining()

    return schedule
