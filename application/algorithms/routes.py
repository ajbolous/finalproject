from models.task import Task, HaulageTask, LoadTask, DigTask


def getRoute(l1, l2, map):

    path, length = map.calcShortestPath(l1, l2)
    return {
        'from': l1.toJSON(),
        'to': l2.toJSON(),
        'path': path
    }


def getTasksRoutes(tasks, origin, map):
    routes = []

    if len(tasks) < 1:
        return []

    if len(tasks) < 2:
        return routes

    lastLocation = origin
    for i in range(0, len(tasks)):
        routes.append(getRoute(lastLocation, tasks[i].location, map))
        lastLocation= tasks[i].location
        if isinstance(tasks[i], HaulageTask):
            routes.append(getRoute(lastLocation, tasks[i].dumpLocation,map))
            lastLocation = tasks[i].dumpLocation

    print routes