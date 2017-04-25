(function() {
    'use strict';

    angular.module('opmopApp').controller('LocationModalController', LocationModalController);

    /** @ngInject */
    function LocationModalController(toastr, $scope, $log, MapsService, $uibModalInstance, path, vertex) {
        var $ctrl = this;
        $ctrl.vertex = path.getAt(vertex);
        $ctrl.path = path;

        $ctrl.location = {
            type: 'Dig',
            lat: $ctrl.vertex.lat(),
            lng: $ctrl.vertex.lng(),
            name: ''
        }
        $log.debug($ctrl);

        $ctrl.save = function() {
            return $uibModalInstance.close($ctrl.location);
        }

        $ctrl.discard = function() {
            return $uibModalInstance.dismiss('discard');
        }

    }

})();