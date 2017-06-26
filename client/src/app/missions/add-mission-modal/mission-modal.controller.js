(function() {
    'use strict';

    angular.module('opmopApp').controller('AddMissionModalController', AddMissionModalController);

    /** @ngInject */
    function AddMissionModalController(toastr, $scope, $log, MissionsService, $uibModalInstance) {
        var $ctrl = this;

        $ctrl.mission = {
            title: '',
            startDate: '',
            endDate: '',
            target: 0,
            digSite: undefined,
            dumps: [
                0,
                0,
                0
            ]
        }

        $ctrl.save = function() {
            return $uibModalInstance.close($ctrl.mission);
        }

        $ctrl.discard = function() {
            return $uibModalInstance.dismiss('discard');
        }

    }

})();