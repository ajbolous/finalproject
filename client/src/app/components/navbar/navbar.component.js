(function() {
    'use strict';

    angular.module('opmopApp')
        .component('topNavbar', {
            templateUrl: 'app/components/navbar/navbar.component.html',
            controller: TopNavbar
        });

    function TopNavbar($log, $scope, $location) {
        var $ctrl = this;
        $ctrl.navbarCollapsed = false;

        $ctrl.links = [
            { label: 'Home', path: '/', active: true },
            { label: 'Maps', path: '/maps', active: false },
            { label: 'Machines', path: '/machines', active: false },
            { label: 'Tasks', path: '/tasks', active: false },
            { label: 'Admin', path: '/admin', active: false },
            { label: 'Help', path: '/help', active: false },

        ]

        $ctrl.selectLink = function(link) {
            $log.debug(link)
            this.links.forEach(function(l) {
                l.active = false;
            });
            link.active = true;
            $location.path(link.path)
            $ctrl.navbarCollapsed = true;
        }
    }
})();