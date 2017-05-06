from tasks.mission import Mission
from tasks.task import Task
from maps.location import Location
import time
from database.database import Database
from machines.machine import Machine

db = Database('data.pkl')

print db.getMachines()
print db.getTasks()

db.saveData('data.pkl')
