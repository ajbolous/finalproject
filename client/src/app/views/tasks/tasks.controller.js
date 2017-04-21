(function() {
    'use strict';

    angular.module('opmopApp').controller('TasksController', TasksController);

    /** @ngInject */
    function TasksController(toastr, $scope, $log, TasksService) {
        var $ctrl = this;

        $ctrl.gridOptions = {
            enableFiltering: true,
            onRegisterApi: function(gridApi) {
                $ctrl.gridApi = gridApi;
            }
        };

        TasksService.getAll().then(function(response) {
            $ctrl.gridOptions.data = response.data;
        });
    }

})();