(function() {
    'use strict';

    angular.module('opmopApp').controller('MachinesModalController', MachinesModalController);

    /** @ngInject */
    function MachinesModalController(toastr, $scope, $log, MachinesService, $uibModalInstance) {
        var $ctrl = this;

        $ctrl.machine = {

        }

        $ctrl.save = function() {
            MachinesService.addMachine($ctrl.machine);
            return $uibModalInstance.close($ctrl.location);
        }

        $ctrl.discard = function() {
            return $uibModalInstance.dismiss('discard');
        }

    }

})();