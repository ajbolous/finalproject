(function() {
    'use strict';

    angular.module('opmopApp')
        .component('machineUi', {
            templateUrl: 'app/components/machine-ui/machine.component.html',
            controller: MachineUI,
            bindings: {
                machine: "="
            }
        });

    function MachineUI($log, $scope) {
        var $ctrl = this;

        $ctrl.machine = undefined;

    }
})();