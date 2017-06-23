from opmop.models.task import DigTask, LoadTask, HaulageTask
from datetime import datetime, timedelta

def serialAllocation(schedule, shovels, loaders, trucks, map):
    startTime = schedule.startTime + timedelta(hours=9)
    for shovel in shovels:
        t = DigTask(schedule.digLocation, startTime, (startTime +
                                                      timedelta(hours=9)), shovel.weightCapacity * 9 * 5, 1)
        schedule.addTask(t)
        shovel.tasks.append(t)
        t.machine = shovel
        schedule.updateRemaining()
        if schedule.remainingDig <= 0:
            break

    for loader in loaders:
        t = LoadTask(schedule.digLocation, startTime,  (startTime +
                                                        timedelta(hours=9)), (loader.weightCapacity * 9 * 5))
        schedule.tasks.append(t)
        t.machine = loader
        loader.tasks.append(t)
        schedule.updateRemaining()
        if schedule.remainingLoad <= 0:
            break

    while True:
        noneSelected = True
        for truck in trucks:
            if len(truck.tasks) > 0:
                lastTask = truck.tasks[len(truck.tasks) - 1]
                startTime = lastTask.endTime + timedelta(minutes=15)
            else:
                startTime = schedule.startTime + timedelta(hours=9, minutes=15)

            if startTime.hour > 16:
                continue

            noneSelected = False
            path, distance = map.calcShortestPath(
                schedule.digLocation.location, schedule.dumpLocations[1].location)
            time = (2 * distance / float(truck.speed)) + 1

            t = HaulageTask(schedule.digLocation, schedule.dumpLocations[0], startTime, (
                startTime + timedelta(hours=time)), truck.weightCapacity)
            schedule.addTask(t)
            t.machine = truck
            truck.tasks.append(t)
            schedule.updateRemaining()

            if schedule.remainingHaulage <= 0:
                break

        if schedule.remainingHaulage <= 0:
            break

        if noneSelected:
            break
