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


        var vertexMenu = undefined;
        methods.initMap = function(el) {

            map = new google.maps.Map(document.getElementById('map'), {
                zoom: 15,
                center: mapCoords,
                mapTypeId: 'satellite'
            });
            vertexMenu = new DeleteMenu();

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

            google.maps.event.addListener(road, 'rightclick', function(e) {
                // Check if click was on a vertex control point
                if (e.vertex == undefined) {
                    return;
                }
                vertexMenu.open(map, road.getPath(), e.vertex);
            });

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



        function DeleteMenu() {

            function addOption(parent, option, callback) {

                var op = document.createElement("div");
                op.innerHTML = option;
                google.maps.event.addDomListener(op, 'click', function() {
                    $log.debug("clicked delete");
                    callback()
                });
                parent.appendChild(op);

                return op;
            }

            this.div_ = document.createElement('div');
            this.div_.innerHTML = "delete";
            this.div_.className = 'delete-menu';

            google.maps.event.addDomListener(this.div_, 'click', function() {
                $log.debug("clicked delete");
            });
        }
        DeleteMenu.prototype = new google.maps.OverlayView();

        DeleteMenu.prototype.onAdd = function() {
            var deleteMenu = this;
            var map = this.getMap();
            this.getPanes().floatPane.appendChild(this.div_);
            $log.debug(map)
                // mousedown anywhere on the map except on the menu div will close the
                // menu.
            this.divListener_ = google.maps.event.addDomListener(map.getDiv(), 'mousedown', function(e) {
                if (e.target != deleteMenu.div_) {
                    deleteMenu.close();
                }
            }, true);
        };

        DeleteMenu.prototype.onRemove = function() {
            google.maps.event.removeListener(this.divListener_);
            this.div_.parentNode.removeChild(this.div_);

            // clean up
            this.set('position');
            this.set('path');
            this.set('vertex');
        };

        DeleteMenu.prototype.close = function() {
            this.setMap(null);
        };

        DeleteMenu.prototype.draw = function() {
            var position = this.get('position');
            var projection = this.getProjection();

            if (!position || !projection) {
                return;
            }

            var point = projection.fromLatLngToDivPixel(position);
            this.div_.style.top = point.y + 'px';
            this.div_.style.left = point.x + 'px';

            $log.debug(point.y, point.x)
        };

        /**
         * Opens the menu at a vertex of a given path.
         */
        DeleteMenu.prototype.open = function(map, path, vertex) {
            this.set('position', path.getAt(vertex));
            this.set('path', path);
            this.set('vertex', vertex);
            this.setMap(map);
            this.draw();
            $log.debug("here", path, path.getAt(vertex));
        };

        /**
         * Deletes the vertex from the path.
         */
        DeleteMenu.prototype.removeVertex = function() {
            var path = this.get('path');
            var vertex = this.get('vertex');

            if (!path || vertex == undefined) {
                this.close();
                return;
            }

            path.removeAt(vertex);
            this.close();
        };

        return methods;
    }
})();