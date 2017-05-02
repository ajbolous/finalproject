(function() {
    'use strict';

    angular.module('opmopApp').controller('MachinesModalController', MachinesModalController);

    /** @ngInject */
    function MachinesModalController(toastr, $scope, $log, MachinesService, $uibModalInstance, options) {
        var $ctrl = this;
        $ctrl.isEdit = options.isEdit;
        if (options.isEdit) {
            $ctrl.machine = options.machine;
            $ctrl.title = "Edit Machine";
        } else {
            $ctrl.machine = {};
            $ctrl.title = "Add Machine";
        }

        $ctrl.save = function() {
            return $uibModalInstance.close($ctrl.machine);
        }

        $ctrl.discard = function() {
            return $uibModalInstance.dismiss('discard');
        }

    }

})();