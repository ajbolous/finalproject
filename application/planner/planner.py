import costs
import routes
import negotiation
import utils
from application.main import Application


class MissionPlanner():
    def __init__(self):
        pass

    def newMission(self):
        pass

    def getSchedulesByDate(self, date):
        schedules = []
        for m in Application.database.getMissions():
            for schedule in m.getSchedules():
                if schedule.date.date == date.date():
                    schedules.append(schedule)
        return schedules

    def getScheduleById(self, sid):
        pass

    def getScheduleCost(self, schedule):
        return costs.getScheduleCost(schedule)

    def getMachineRoute(self, machine, date):
        tasks = utils.getMachineSchedule(machine, date)
        return routes.getTasksRoutes(tasks, machine.point)

    def getNewSchedule(self, mission, date, target):
        shovels, loaders, trucks = Application.database.getMachinesSorted()
        return negotiation.getNewSchedule(mission, date, target, shovels, loaders, trucks)
