(function() {
    'use strict';

    angular
        .module('opmopApp')
        .service('MapsService', MapsService);

    function MapsService($q, $http, $log, MapMenuService) {
        var methods = {}
        var roads = [];
        var map = undefined;
        var mapCoords = { lat: 40.519897, lng: -112.148473 }
        var mapMenu = undefined;

        methods.initMap = function(el) {

            map = new google.maps.Map(document.getElementById('map'), {
                zoom: 15,
                center: mapCoords,
                mapTypeId: 'satellite'
            });
            mapMenu = MapMenuService;

            return map
        }

        methods.addMapMenuOption = function(option, callback) {
            return mapMenu.addOption(option, callback);
        }

        methods.addLocation = function(location) {
            return $http.get(DJANGOURL + '/maps/add-location', { params: location });
        }

        methods.addNewRoad = function() {
            var road = methods.addRoad([mapCoords, mapCoords], '#ffffff', 0.5, true, 4);
            roads.push(road)
            return road;
        }

        methods.setEditRoads = function(isEditable) {
            roads.forEach(function(road) {
                road.setEditable(isEditable);
            });
        }

        methods.addRoad = function(path, color, opacity, editable, width) {
            var road = new google.maps.Polyline({
                editable: editable,
                path: path,
                geodesic: true,
                strokeColor: color,
                strokeOpacity: opacity,
                strokeWeight: width
            });
            road.setMap(map);

            google.maps.event.addListener(road, 'rightclick', function(e) {
                // Check if click was on a vertex control point
                if (e.vertex == undefined) {
                    return;
                }
                mapMenu.open(map, road.getPath(), e.vertex);
            });
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
            $log.debug(JSON.stringify(paths));
        }

        methods.getShortestPath = function(source, destination) {
            $http.get(DJANGOURL + '/maps/get-shortest', { params: { source: source, dest: destination } }).then(function(response) {
                methods.addRoad(response.data, '#ff0000', 0.2, false, 8);
            });

        }

        methods.getLocations = function() {

            return $http.get(DJANGOURL + '/maps/get-locations').then(function(response) {
                return response.data;
            });
        }

        methods.buildLocations = function() {
            return methods.getLocations().then(function(locations) {
                locations.forEach(function(location) {
                    $log.debug(location);
                    var marker = new google.maps.Marker({
                        position: { lat: location.lat, lng: location.lng },
                        map: map,
                        label: location.site,
                        title: location.name + " - " + location.site
                    });

                    var contentString = '<div id="content">' +
                        '<div id="bodyContent">' +
                        '<p><b>' + location.site + '</b>' +
                        '</div>' +
                        '</div>';

                    var infowindow = new google.maps.InfoWindow({
                        content: contentString
                    });

                    marker.addListener('click', function() {
                        infowindow.open(map, marker);
                    });
                })
            });
        }
        methods.getNodes = function() {
            return $http.get(DJANGOURL + '/maps/get-roads');
        }

        methods.buildRoads = function() {
            return methods.getNodes().then(function(response) {
                roads = [];
                response.data.forEach(function(road) {
                    roads.push(methods.addRoad(road, '#0000aa', 0.4, false, 4));
                });
            });
        }

        return methods;
    }
})();