from tasks.mission import Mission
from tasks.task import Task
from maps.location import Location
import time
import database.database as db


m = Mission('dig2',time.time(),Location(123,123,1), 125000)

tasks = []

for i in range(1,100):
    t = Task('dig', Location(12+i, 12+i,i), time.time(), time.time()+100, "new task ")
    tasks.append(t)
    m.addTask(t)

db.saveTasks({'tasks': tasks, 'missions':m})

m = db.loadTasks()

print m