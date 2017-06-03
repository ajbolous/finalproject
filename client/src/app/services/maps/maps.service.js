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

            var i = 0;
            road.getPath().forEach(function(v) {
                v.id = path[i].id;
                i++;

            })

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

        methods.addLocationsToMap = function(locations) {
            locations.forEach(function(location) {
                var icon = undefined;
                switch (location.machine.type) {
                    case 'shovel':
                        icon = 'http://icons.iconarchive.com/icons/bartkowalski/1960-matchbox-cars/48/Hatra-Tractor-Shovel-icon.png';
                        break;
                    case 'truck':
                        icon = "http://icons.iconarchive.com/icons/custom-icon-design/flatastic-2/48/truck-icon.png";
                        break;
                    case 'loader':
                        icon = "https://cdn4.iconfinder.com/data/icons/BRILLIANT/construction/png/48/front_loader.png";
                        break;
                    default:
                        icon = undefined
                }

                var marker = new google.maps.Marker({
                    position: { lat: location.location.lat, lng: location.location.lng },
                    map: map,
                    animation: google.maps.Animation.DROP,
                    icon: icon,
                    label: location.machine.id.toString(),
                    title: location.machine.id + " - " + location.machine.model
                });

                var contentString = '<div id="content">' +
                    '<div id="bodyContent">' +
                    '<br><b style="text-transform:capitalize">' + location.machine.type + "</b><br>" + location.machine.id + " - " + location.machine.model + '<br> ( ' + location.location.lat + " , " + location.location.lng + ' )</b>' +
                    '</div>' +
                    '</div>';

                var infowindow = new google.maps.InfoWindow({
                    content: contentString
                });

                marker.addListener('click', function() {
                    infowindow.open(map, marker);
                });
            });
            return true;
        }

        methods.getNodes = function() {
            return $http.get(DJANGOURL + '/maps/get-roads');
        }

        methods.buildRoads = function() {
            return methods.getNodes().then(function(response) {
                roads = [];

                response.data.forEach(function(road) {
                    roads.push(methods.addRoad(road.points, '#0000aa', 0.4, false, 4));
                });
            });
        }

        return methods;
    }
})();