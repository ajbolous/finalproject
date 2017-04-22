(function() {
    'use strict';

    angular.module('opmopApp').controller('MapsController', MapsController);

    /** @ngInject */
    function MapsController(toastr, $scope, $log, MapsService) {
        var $ctrl = this;

        $ctrl.editRoads = false;


        MapsService.initMap();
        MapsService.buildRoads();
        MapsService.setEditRoads($ctrl.editRoads);
        MapsService.getShortestPath();
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
    }

})();