(function() {
    'use strict';

    angular.module('opmopApp').controller('MainController', MainController);

    /** @ngInject */
    function MainController(toastr, $scope, $log, MachineService) {
        var $ctrl = this;

        console.log(this);
        $ctrl.columns = ['name', 'lastname'];
        MachineService.getAll().then(function(response) {
            var machine = response.data[0];

            $ctrl.columns = Object.keys(machine);
            $log.debug($ctrl.columns);
            $ctrl.data = response.data;

        });

    }

})();