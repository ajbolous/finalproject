(function() {
    'use strict';

    angular.module('opmopApp').controller('MapsController', MapsController);

    /** @ngInject */
    function MapsController(toastr, $scope, $log, $uibModal, MapsService, MachinesService, ngProgressFactory) {
        var $ctrl = this;

        $ctrl.progressbar = ngProgressFactory.createInstance();
        $ctrl.progressbar.start();


        $ctrl.editRoads = false;

        MapsService.initMap();
        MapsService.buildRoads().then(function() {
            $ctrl.progressbar.complete()
        });
        MapsService.setEditRoads($ctrl.editRoads);

        $ctrl.toggleEditRoads = function() {
            $ctrl.editRoads = !$ctrl.editRoads;
            MapsService.setEditRoads($ctrl.editRoads);
        }

        $ctrl.addRoad = function() {
            MapsService.addNewRoad();
        }

        $ctrl.exportRoads = function() {
            MapsService.exportRoads();

        }

        $ctrl.addLocation = function(path, vertex) {

            var modalInstance = $uibModal.open({
                animation: true,
                templateUrl: 'app/views/maps/location-modal/location-modal.html',
                controller: 'LocationModalController',
                controllerAs: '$ctrl',
                resolve: {
                    vertex: function() {
                        return vertex;
                    },
                    path: function() {
                        return path;
                    }
                }
            });

            modalInstance.result.then(function(location) {
                $log.debug(location)
                MapsService.addLocation(location);
            });
        }


        MachinesService.getAll().then(function(response) {
            var machines = response.data;
            var locations = []
            machines.forEach(function(machine) {
                locations.push({
                    'lat': machine.location.lat,
                    'lng': machine.location.lng,
                    'label': machine.model,
                    'title': machine.id + " - " + machine.model,
                    'type': machine.type
                })
            });
            MapsService.addLocationsToMap(locations);
        });


        MapsService.getLocations().then(function(locations) {
            var maplocations = []
            locations.forEach(function(location) {
                maplocations.push({
                    'lat': location.point.lat,
                    'lng': location.point.lng,
                    'label': location.name,
                    'title': location.id + " - " + location.name,
                    'type': location.type
                });
            });
            MapsService.addLocationsToMap(maplocations);

        });

        MapsService.addMapMenuOption('Set Location', $ctrl.addLocation);

    }

})();