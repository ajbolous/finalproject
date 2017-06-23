from models.task import Task, HaulageTask, LoadTask, DigTask


def getRoute(p1, p2, ltype):
    path, length = Application.mapping.calcShortestPath(p1, p2)
    return {
        'from': p1.toJSON(),
        'to': p2.toJSON(),
        'path': [p.toJSON() for p in path],
        'type': ltype,
        'length': length
    }


def getTasksRoutes(tasks, origin):
    routes = []

    if len(tasks) < 1:
        return []

    lastLocation = origin
    for i in range(0, len(tasks)):
        routes.append(
            getRoute(lastLocation, tasks[i].location.point, tasks[i].point.type))
        lastLocation = tasks[i].location.location

        if isinstance(tasks[i], HaulageTask):
            routes.append(getRoute(
                lastLocation, tasks[i].dumpLocation.point, tasks[i].dumpLocation.type))
            lastLocation = tasks[i].dumpLocation.location

    return routes
