(function() {
    'use strict';

    angular.module('opmopApp')
        .component('opmDataTable', {
            templateUrl: 'app/components/table/table.component.html',
            controller: OpmDataTable,
            bindings: {
                columns: '=',
                data: '='
            }
        });

    function OpmDataTable($log, $scope) {
        var $ctrl = this;
        console.log(this);
        $log.debug($ctrl.columns);
    }
})();