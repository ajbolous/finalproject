(function() {
    'use strict';

    angular.module('opmopApp').controller('LocationModalController', LocationModalController);

    /** @ngInject */
    function LocationModalController(toastr, $scope, $log, MapsService, $uibModalInstance) {
        var $ctrl = this;
        $ctrl = this;
        $ctrl.location = {
            type: 'Dig',
            lat: '0',
            lng: '0',
            name: ''
        }

        $ctrl.save = function() {
            return $uibModalInstance.close($ctrl.location);
        }

        $ctrl.discard = function() {
            return $uibModalInstance.dismiss('discard');
        }

    }

})();