(function() {
    'use strict';

    angular.module('opmopApp').controller('MachinesController', MachinesController);

    /** @ngInject */
    function MachinesController(toastr, $scope, $log, MachinesService) {
        var $ctrl = this;

        $ctrl.gridOptions = {
            enableFiltering: true,
            onRegisterApi: function(gridApi) {
                $ctrl.gridApi = gridApi;
            }
        };

        MachinesService.getAll().then(function(response) {
            $ctrl.gridOptions.data = response.data;
        });
    }

})();