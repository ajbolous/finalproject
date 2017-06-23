from main import Application
from planner.planner import MissionPlanner
from datetime import datetime
planner = MissionPlanner()

print planner.getNewSchedule(Application.database.getMissions()[0], datetime(2017,5,1), 3000)
