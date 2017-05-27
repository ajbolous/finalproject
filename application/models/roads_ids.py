import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
roadsIds = []

with open(dir_path + '/roads.json','r') as data:
    roads = json.load(data)
    i=0
    for r in roads:
        road = []
        j=0
        for point in r:
            j+=1
            i+=1
            road.append({'nid':i, 'index': j, 'lat':point['lat'], 'lng':point['lng']})
        roadsIds.append(road)

print roadsIds
with open(dir_path + '/roads.json','w') as data:
    json.dump(roadsIds, data)
