from models.task import Task, HaulageTask, LoadTask, DigTask


def getRoute(l1, l2, map, ltype):
    points = []
    path, length = map.calcShortestPath(l1, l2)

    for p in path:
        points.append(p.toJSON())
    return {
        'from': l1.toJSON(),
        'to': l2.toJSON(),
        'path': points,
        'type': ltype
    }


def getTasksRoutes(tasks, origin, map):
    routes = []

    if len(tasks) < 1:
        return []

    lastLocation = origin
    for i in range(0, len(tasks)):
        routes.append(getRoute(
            lastLocation, tasks[i].location.location, map, tasks[i].location.type))
        lastLocation = tasks[i].location.location
        if isinstance(tasks[i], HaulageTask):
            routes.append(getRoute(
                lastLocation, tasks[i].dumpLocation.location, map, tasks[i].dumpLocation.type))
            lastLocation = tasks[i].dumpLocation.location

    return routes
