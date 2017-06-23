from datetime import datetime, timedelta
from opmop.models.task import HaulageTask, DigTask, LoadTask
from opmop.main import Application


def getMachineSchedule(machine, date):
    tasks = []
    for mission in Application.database.getMissions():
        if mission.startDate.date() <= date and date <= mission.endDate.date():
            for schedule in mission.getSchedules():
                if schedule.date.date() == date.date():
                    for task in schedule.getTasks():
                        if task.machineId == machine.id:
                            tasks.append(task)
    return tasks


def getLocationAtTime(machine, time):
    machineTasks = getMachineSchedule(machine, time.date())
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
        return []

    windows = []
    machineTasks = getMachineSchedule(machine, date.date())

    windowStart = datetime(date.year, date.month, date.day, 9)
    windowEnd = windowStart + timedelta(hours=size)

    maxNumOfWindows = int(9 / size)

    for i in range(maxNumOfWindows):
        conflict = False
        for task in machineTasks:
            if windowStart > task.startTime and windowStart < task.endTime:
                conflict = True
            if windowStart < task.startTime and windowEnd > task.startTime:
                conflict = True
            if windowStart < task.endTime and windowEnd > task.endTime:
                conflict = True
        if not conflict:
            windows.append((windowStart, windowEnd))

        windowStart = windowEnd
        windowEnd = windowStart + timedelta(hours=size)

    return windows
