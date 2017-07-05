(function() {
    'use strict';

    angular.module('opmopApp').controller('MainController', MainController);

    /** @ngInject */
    function MainController(toastr, $scope, $log, $uibModal, MapsService, MachinesService, ngProgressFactory) {
        var $ctrl = this;

        $ctrl.progressbar = ngProgressFactory.createInstance();
        $ctrl.progressbar.start();

        $ctrl.sidePanels = {
            markers: false,
            calendar: false
        }

        $ctrl.editRoads = false;

        $ctrl.mapMarkers = {
            shovels: true,
            trucks: true,
            loaders: true,
            locations: true,
            roads: true
        }

        MapsService.initMap();

        MapsService.buildRoads().then(function() {
            $ctrl.progressbar.complete()
        });

        $ctrl.refresh = function() {
            for (var key in $ctrl.mapMarkers)
                MapsService.showGroup(key, $ctrl.mapMarkers[key]);
        }
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

        $ctrl.openSidePanel = function(panel) {

            for (var key in $ctrl.sidePanels)
                if (key != panel)
                    $ctrl.sidePanels[key] = false;

            setTimeout(function() {
                $ctrl.sidePanels[panel] = !$ctrl.sidePanels[panel]
                $scope.$apply();
            }, 5);
        }


        $ctrl.addLocation = function(path, vertex) {

            var modalInstance = $uibModal.open({
                animation: true,
                templateUrl: 'app/maps/location-modal/location-modal.html',
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

        $ctrl.showRoute = function(machine) {
            MapsService.clearRoutes();
            MachinesService.getMachineRoute(machine).then(function(route) {
                $log.debug(route);
                MapsService.addRoute(machine, route);
            });
        }

        MachinesService.getAll().then(function(machines) {
            $ctrl.machines = machines;
            machines.forEach(function(machine) {
                MapsService.addMachineMarker(machine);
            });
        });


        MapsService.getLocations().then(function(locations) {
            locations.forEach(function(mapLocation) {
                MapsService.addLocationMarker(mapLocation);
            });

        });

    }

})();