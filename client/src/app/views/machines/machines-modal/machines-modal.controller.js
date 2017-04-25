(function() {
    'use strict';

    angular.module('opmopApp').controller('MachinesModalController', MachinesModalController);

    /** @ngInject */
    function MachinesModalController(toastr, $scope, $log, MachinesService, $uibModalInstance) {
        var $ctrl = this;

        $ctrl.machine = {
            name: "ahdab",
            model: "Truck",
            weight: 120
        }

        $ctrl.save = function() {
            return $uibModalInstance.close($ctrl.location);
        }

        $ctrl.discard = function() {
            return $uibModalInstance.dismiss('discard');
        }

    }

})();