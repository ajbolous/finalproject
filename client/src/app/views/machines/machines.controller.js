(function() {
    'use strict';

    angular.module('opmopApp').controller('MachinesController', MachinesController);

    /** @ngInject */
    function MachinesController(toastr, $scope, $log, $uibModal, MachinesService) {
        var $ctrl = this;

        $ctrl.gridOptions = {
            enableFiltering: true,
            onRegisterApi: function(gridApi) {
                $ctrl.gridApi = gridApi;
            }
        };

        $ctrl.addMachine = function() {
            var modalInstance = $uibModal.open({
                animation: true,
                templateUrl: 'app/views/machines/machines-modal/machines-modal.html',
                controller: 'MachinesModalController',
                controllerAs: '$ctrl',
            });
        }


        MachinesService.getAll().then(function(response) {
            $ctrl.gridOptions.data = response.data;

        })

    }

})();