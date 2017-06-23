(function() {
    'use strict';

    angular.module('opmopApp')
        .component('searchUi', {
            templateUrl: 'app/components/search/search.component.html',
            controller: SearchUI,
            bindings: {
                searchCall: "&"
            }
        });

    function SearchUI($log, $scope) {
        var $ctrl = this;

        $ctrl.searchObj = {
            id: "",
            model: "",
            weightCapacity: "",
            fuelConsumption: "",

        };

        $ctrl.doSearch = function($event) {
            // if ($event.which == 13) {
            for (var field in $ctrl.searchObj) {
                if ($ctrl.searchObj[field] != "") {
                    $ctrl.searchCall({ searchObj: $ctrl.searchObj });
                    return;
                }
            }
            $ctrl.searchCall({ searchObj: undefined });

            //}
        }

    }

})();