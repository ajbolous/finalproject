from main import Application
from datetime import datetime
from main import Application
from missions import planner

for mission in Application.database.getMissions():
    for schedule in mission.getSchedules():
        planner.calculateSchedule(mission, schedule)
        break
    break

Application.database.save()


