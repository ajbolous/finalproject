(function() {
    'use strict';

    angular.module('opmopApp').controller('MapsController', MapsController);

    /** @ngInject */
    function MapsController(toastr, $scope, $log, $uibModal, MapsService) {
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

        $ctrl.addLocation = function() {
            var modalInstance = $uibModal.open({
                animation: true,
                templateUrl: 'app/views/maps/location-modal/location-modal.html',
                controller: 'LocationModalController',
                controllerAs: '$ctrl',
                resolve: {
                    items: function() {
                        return $ctrl.items;
                    }
                }
            });

            modalInstance.result.then(function(items) {
                $log.debug(items);
            })
        }
    }

})();