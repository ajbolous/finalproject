(function() {
    'use strict';

    angular
        .module('opmopApp')
        .service('MapsService', MapsService);

    function MapsService($q, $http, $log, MapMenuService, MissionsService, MachinesService) {
        var methods = {}
        var map = undefined;
        var mapCoords = { lat: 40.519897, lng: -112.148473 }
        var mapMenu = undefined;
        var alreadyHooked = false;

        var routes = [];
        var roads = [];
        var markers = {
            trucks: [],
            shovels: [],
            loaders: [],
            locations: []
        };

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
            if (alreadyHooked)
                return;
            alreadyHooked = true;
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


        methods.addRoad = function(path, color, opacity, editable, width) {
            var road = new google.maps.Polyline({
                editable: editable,
                path: path,
                geodesic: true,
                strokeColor: color,
                strokeOpacity: opacity,
                strokeWeight: width,
                map: map
            });

            var i = 0;
            road.getPath().forEach(function(v) {
                v.id = path[i].id;
                i++;
            });

            google.maps.event.addListener(road, 'rightclick', function(e) {
                if (e.vertex == undefined)
                    return;
                mapMenu.open(map, road.getPath(), e.vertex);
            });

            return road;
        }


        methods.getLocations = function() {
            return $http.get(DJANGOURL + '/maps/get-locations').then(function(response) {
                return response.data;
            });
        }

        methods.addMarker = function(position, icon, label, title) {
            var marker = new google.maps.Marker({
                position: { lat: position.lat, lng: position.lng },
                map: map,
                icon: icon,
                label: label,
                title: title
            });
            var contentString = '<div id="content">' +
                '<div id="bodyContent">' +
                '<br><b style="text-transform:capitalize">' + title + "</b><br>" + label + '<br> ( ' + position.lat + " , " + position.lng + ' )</b>' +
                '</div>' +
                '</div>';

            var infowindow = new google.maps.InfoWindow({
                content: contentString
            });
            marker.addListener('click', function() {
                infowindow.open(map, marker);
            });
            return marker;
        }


        methods.addMachineMarker = function(machine) {
            var icon = undefined;
            var marker = methods.addMarker(machine.point, icon, " " + machine.id, machine.type + " - " + machine.model);

            switch (machine.type) {
                case 'shovel':
                    icon = 'http://icons.iconarchive.com/icons/bartkowalski/1960-matchbox-cars/48/Hatra-Tractor-Shovel-icon.png';
                    marker.setIcon(icon);
                    markers.shovels.push(marker);
                    break;
                case 'truck':
                    icon = "http://icons.iconarchive.com/icons/custom-icon-design/flatastic-2/48/truck-icon.png";
                    marker.setIcon(icon);
                    markers.trucks.push(marker);
                    break;
                case 'loader':
                    icon = "https://cdn4.iconfinder.com/data/icons/BRILLIANT/construction/png/48/front_loader.png";
                    marker.setIcon(icon);
                    markers.loaders.push(marker);
                    break;
            }

        }

        methods.addLocationMarker = function(mapLocation) {

            var marker = methods.addMarker(mapLocation.point, undefined, "", mapLocation.type);
            markers.locations.push(marker);
            switch (mapLocation.type) {
                case 'fuel':
                    marker.setIcon("https://cdn2.iconfinder.com/data/icons/circle-icons-1/64/gas-32.png");
                    break;
                case 'dump':
                    marker.setIcon("https://cdn2.iconfinder.com/data/icons/thesquid-ink-40-free-flat-icon-pack/64/power-plant-32.png");
                    break;
                case 'dig':
                    marker.setIcon("https://cdn3.iconfinder.com/data/icons/snowish/32x32/apps/inkscape.png");
                    break;
            }

        }



        methods.clearRoutes = function() {
            for (var key in routes)
                methods.removeRoute({ id: key });
            routes = {};
        }
        methods.removeRoute = function(machine) {

            var machineRoutes = routes[machine.id];
            machineRoutes.forEach(function(route) {
                route.road.setMap(null);
                route.marker.setMap(null);
            });

            delete routes[machine.id];
        }
        methods.addRoute = function(machine, routesToAdd) {
            var colors = ['orangered', 'orange', 'dodgerblue', 'violet', 'aliceblue', 'yellowgreen']
            var i = 0;

            if (machine.id in routes) {
                methods.removeRoute(machine);
            }
            routes[machine.id] = [];

            routesToAdd.forEach(function(route) {
                var mapRoute = {};
                mapRoute.road = methods.addRoad(route.path, colors[machine.id % 6], 0.4, false, 8);
                var icon = "https://cdn1.iconfinder.com/data/icons/hawcons/32/698879-icon-14-flag-32.png";
                mapRoute.marker = methods.addMarker({
                        lat: route.to.lat + (0.0001 * (Math.random() - 0.5)),
                        lng: route.to.lng + (0.0001 * (Math.random() - 0.5))
                    },
                    icon,
                    machine.id + "-" + i,
                    'Task ' + i + " " + machine.model);

                routes[machine.id].push(mapRoute);
                i += 1;
            });
        }

        methods.getRoads = function() {
            return $http.get(DJANGOURL + '/maps/get-roads');
        }

        methods.buildRoads = function() {
            return methods.getRoads().then(function(response) {
                roads = [];
                response.data.forEach(function(road) {
                    roads.push(methods.addRoad(road.points, '#0000aa', 0.4, false, 4));
                });
                $log.debug(roads)
            });
        }


        methods.showGroup = function(group, show) {
            if (group == 'roads') {
                roads.forEach(function(road) {
                    if (show)
                        road.setMap(map);
                    else
                        road.setMap(null);
                });
                return;
            }
            markers[group].forEach(function(marker) {
                if (show)
                    marker.setMap(map);
                else marker.setMap(null);
            });
        }

        return methods;
    }
})();