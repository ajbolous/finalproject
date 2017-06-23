from main import Application
from datetime import datetime
from main import Application
from missions import planner

mission = Application.database.getMissions()[0]

sched = planner.calculateSchedule(mission, datetime(2017,5,1), 3000)
mission.addSchedule(sched)

mission.printMission()