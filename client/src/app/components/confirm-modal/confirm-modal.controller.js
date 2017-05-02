(function() {
    'use strict';

    angular.module('opmopApp').controller('ConfirmModalController', ConfirmModalController);

    /** @ngInject */
    function ConfirmModalController(toastr, $scope, $log, $uibModalInstance) {
        var $ctrl = this;

        $ctrl.yes = function() {
            return $uibModalInstance.close(true);
        }

        $ctrl.no = function() {
            return $uibModalInstance.close(false);
        }

    }

})();