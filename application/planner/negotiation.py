from application.models.schedule import Schedule
from offers.offer import makeOffer


def getMaxOffer(machines, schedule, target):
    maxOffer, maxMachine = None, None
    for machine in machines:
        offer = makeOffer(machine, schedule, target)
        if offer[0] == False:
            continue
        if maxOffer == None:
            maxOffer = offer
            maxMachine = machine
        elif maxOffer[2] >= offer[2]:
            maxOffer = offer
            maxMachine = machine

    return maxOffer, maxMachine


def getNewSchedule(mission, date, target, shovels, loaders, trucks):

    schedule = Schedule(len(mission.schedules), date, mission, target)

    schedule.updateRemaining()

    while schedule.remainingDig > 0:
        schedule.updateRemaining()
        maxOffer, maxMachine = getMaxOffer(
            shovels, schedule, schedule.remainingDig)
        if maxOffer is None:
            break
        for task in maxOffer[1]:
            schedule.addTask(task)

        schedule.updateRemaining()


    while schedule.remainingLoad > 0:
        maxOffer, maxMachine = getMaxOffer(
            loaders, schedule, schedule.remainingLoad)
        if maxOffer is None:
            break
        for task in maxOffer[1]:
            schedule.addTask(task)

        schedule.updateRemaining()

    while schedule.remainingHaulage >= 0:
        maxOffer, maxMachine = getMaxOffer(
            trucks, schedule, schedule.remainingHaulage)

        if maxOffer is None:
            break

        for task in maxOffer[1]:
            schedule.addTask(task)
        schedule.updateRemaining()

    schedule.updateRemaining()

    return schedule
