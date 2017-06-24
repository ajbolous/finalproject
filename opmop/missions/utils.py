from datetime import datetime, timedelta
from opmop.models.task import HaulageTask, DigTask, LoadTask
from opmop.models.machine import Loader

from opmop.main import Application


def isTimeConflict(window1, window2):
    if window1[0] >= window2[0] and window1[0] <= window2[1]:
        return True
    if window1[0] <= window2[0] and window1[1] >= window2[0]:
        return True
    if window1[0] <= window2[0] and window1[1] >= window2[0]:
        return True
    return False


def getMachineSchedule(machine, date):
    tasks = []
    numberOfTasks = 0
    for mission in Application.database.getMissions():
        if mission.startDate.month == date.month:
            for schedule in mission.getSchedules():
                for task in schedule.getTasks():
                    if task.machineId == machine.id:
                        numberOfTasks += 1
                        if task.startTime.date() == date:
                            tasks.append(task)
    return tasks, numberOfTasks


def getNumberOfHaulers(schedule, window):
    numOfHaulers = 0
    for task in schedule.tasks:
        if isinstance(task, HaulageTask):
            if isTimeConflict((task.startTime, task.endTime), window):
                numOfHaulers += 1
    return numOfHaulers


def getWasteAtTime(schedule, time):
    waste = 0
    for task in schedule.tasks:
        if isinstance(task, LoadTask) and time>task.startTime:
            print task
            ratio = float((time - task.startTime).seconds) / \
                (task.endTime - task.startTime).seconds
            waste += int(ratio * task.target)
        if isinstance(task, HaulageTask) and task.endTime < time:
            waste -= task.target
    return waste


def getLocationAtTime(machine, time):
    machineTasks, numberOfTasks = getMachineSchedule(machine, time.date())
    location = machine.point
    for task in machineTasks:
        if task.startTime > time and task.endTime < time:
            location = task.digLocation
            if isinstance(task, HaulageTask):
                location = task.dumpLocation
            break
    return location


def getTimeWindows(machine, date, size):

    if size <= 0:
        return [], 0

    windows = []
    machineTasks, totalTasks = getMachineSchedule(machine, date.date())

    windowStart = datetime(date.year, date.month, date.day, 9)
    windowEnd = windowStart + timedelta(hours=size)

    maxNumOfWindows = int(9 / size)

    for i in range(maxNumOfWindows):
        conflict = False
        for task in machineTasks:
            if isTimeConflict((task.startTime, task.endTime), (windowStart, windowEnd)):
                conflict = True
        if not conflict:
            windows.append((windowStart, windowEnd))

        windowStart = windowEnd
        windowEnd = windowStart + timedelta(hours=size)

    return windows, totalTasks
