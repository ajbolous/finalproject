(function () {
    'use strict';

    angular
        .module('opmopApp')
        .component('systemGage', {
            templateUrl: 'app/components/system-gage/gage.component.html',
            bindings: {
                gageLabel: '<',
                gageTitle: '<',
                gageValue: '<',
                gageWidth: '<',
                gageHeight: '<'
            },
            controller: GageController
        });

        function GageController($log, $ros){
            var $ctrl = this;
        }
})();