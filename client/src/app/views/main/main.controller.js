(function() {
    'use strict';

    angular.module('opmopApp').controller('MainController', MainController);

    /** @ngInject */
    function MainController(toastr, $scope, $log, MachineService) {
        var $ctrl = this;

        $ctrl.gridOptions = {
            enableFiltering: true,
            onRegisterApi: function(gridApi) {
                $ctrl.gridApi = gridApi;
            }
        };

        MachineService.getAll().then(function(response) {
            $ctrl.gridOptions.data = response.data;
        });
    }

})();