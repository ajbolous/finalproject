(function() {
    'use strict';

    angular
        .module('opmopApp')
        .service('MapMenuService', MapMenuService);

    function MapMenuService($q, $http, $log) {

        var MapMenu = function() {
            this.div_ = document.createElement('div');
            this.div_.innerHTML = "";
            this.div_.className = 'delete-menu';
            var menu = this;

            this.addOption("Delete", function() {
                menu.removeVertex()
            });
        }
        MapMenu.prototype = new google.maps.OverlayView();

        MapMenu.prototype.onAdd = function() {
            var MapMenu = this;
            var map = this.getMap();
            this.getPanes().floatPane.appendChild(this.div_);
            // mousedown anywhere on the map except on the menu div will close the
            // menu.
            this.divListener_ = google.maps.event.addDomListener(map.getDiv(), 'mousedown', function(e) {
                if (e.target.parentElement != MapMenu.div_) {
                    MapMenu.close();
                }
            }, true);
        };

        MapMenu.prototype.addOption = function(option, callback) {

            var op = document.createElement("button");
            op.className = "btn btn-default btn-xs";
            op.innerHTML = option;
            var self = this;
            google.maps.event.addDomListener(op, 'click', function() {
                var path = self.get('path');
                var vertex = self.get('vertex');
                callback(path, vertex);
            });
            this.div_.appendChild(op);

            return op;
        }

        MapMenu.prototype.onRemove = function() {
            google.maps.event.removeListener(this.divListener_);
            this.div_.parentNode.removeChild(this.div_);

            // clean up
            this.set('position');
            this.set('path');
            this.set('vertex');
        };

        MapMenu.prototype.close = function() {
            this.setMap(null);
        };

        MapMenu.prototype.draw = function() {
            var position = this.get('position');
            var projection = this.getProjection();

            if (!position || !projection) {
                return;
            }

            var point = projection.fromLatLngToDivPixel(position);
            this.div_.style.top = point.y + 'px';
            this.div_.style.left = point.x + 'px';

        };

        /**
         * Opens the menu at a vertex of a given path.
         */
        MapMenu.prototype.open = function(map, path, vertex) {
            this.set('position', path.getAt(vertex));
            this.set('path', path);
            this.set('vertex', vertex);
            this.setMap(map);
            this.draw();
        };

        /**
         * Deletes the vertex from the path.
         */
        MapMenu.prototype.removeVertex = function() {
            var path = this.get('path');
            var vertex = this.get('vertex');

            if (!path || vertex == undefined) {
                this.close();
                return;
            }

            path.removeAt(vertex);
            this.close();
        };

        return new MapMenu();
    }
})();