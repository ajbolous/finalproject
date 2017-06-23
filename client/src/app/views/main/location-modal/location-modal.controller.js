(function() {
    'use strict';

    angular.module('opmopApp').controller('LocationModalController', LocationModalController);

    /** @ngInject */
    function LocationModalController(toastr, $scope, $log, MapsService, $uibModalInstance, path, vertex) {
        var $ctrl = this;
        $ctrl.vertex = path.getAt(vertex);
        $ctrl.path = path;

        $ctrl.location = {
            site: 'Dig',
            lat: $ctrl.vertex.lat(),
            lng: $ctrl.vertex.lng(),
            name: 'D122',
            material: 'iron',
            capacity: 12411
        }

        $ctrl.save = function() {
            return $uibModalInstance.close($ctrl.location);
        }

        $ctrl.discard = function() {
            return $uibModalInstance.dismiss('discard');
        }

    }

})();