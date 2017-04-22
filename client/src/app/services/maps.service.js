(function() {
    'use strict';

    angular
        .module('opmopApp')
        .service('MapsService', MapsService);

    function MapsService($q, $http, $log) {
        var methods = {}
        var roads = [];
        var map = undefined;
        var mapCoords = { lat: 40.519897, lng: -112.148473 }

        methods.initMap = function(el) {

            map = new google.maps.Map(document.getElementById('map'), {
                zoom: 15,
                center: mapCoords,
                mapTypeId: 'satellite'
            });
            return map
        }

        methods.addNewRoad = function() {
            var road = methods.addRoad([mapCoords, mapCoords]);
            road.setEditable(true);
            return road;
        }

        methods.setEditRoads = function(isEditable) {
            roads.forEach(function(road) {
                road.setEditable(isEditable);
            });
        }

        methods.addRoad = function(path) {
            var road = new google.maps.Polyline({
                editable: false,
                path: path,
                geodesic: true,
                strokeColor: '#000077',
                strokeOpacity: 0.4,
                strokeWeight: 6
            });
            road.setMap(map);
            roads.push(road)
            return road;
        }

        methods.exportRoads = function() {

            var paths = [];

            roads.forEach(function(road) {
                var path = [];
                road.getPath().forEach(function(coord) {
                    path.push({ lat: coord.lat(), lng: coord.lng() });
                });
                paths.push(path);
            });

            var jsonStr = JSON.stringify(paths);
            $log.debug(jsonStr);
        }

        methods.getShortestPath = function(source, destination) {
            $http.get(DJANGOURL + '/maps/get-shortest', { params: { source: source, dest: destination } }).then(function(response) {
                var road = new google.maps.Polyline({
                    editable: false,
                    path: response.data,
                    geodesic: true,
                    strokeColor: '#ff0000',
                    strokeOpacity: 0.2,
                    strokeWeight: 8
                });
                road.setMap(map);
                roads.push(road)
                return road;
            });

        }


        methods.getNodes = function() {
            return $http.get(DJANGOURL + '/maps/get-roads');
        }

        methods.buildRoads = function() {
            return methods.getNodes().then(function(response) {
                self.roads = response.data;
                self.roads.forEach(function(road) {
                    return methods.addRoad(road);
                });
            });
        }

        return methods;
    }
})();