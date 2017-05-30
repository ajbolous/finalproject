(function() {
    'use strict';

    angular.module('opmopApp')
        .component('topNavbar', {
            templateUrl: 'app/components/navbar/navbar.component.html',
            controller: TopNavbar
        });

    function TopNavbar($log, $scope, $location) {
        var $ctrl = this;
        $ctrl.navbarCollapsed = true;

        $ctrl.leftLinks = [
            { label: 'Monitor', path: '/', active: true, icon: "fa-desktop" },
            { label: 'Maps', path: '/maps', active: false, icon: "fa-map-marker" },
            { label: 'Machines', path: '/machines', active: false, icon: "fa-truck" },
            { label: 'Tasks', path: '/tasks', active: false, icon: "fa-tasks" },
        ]

        $ctrl.rightLinks = [

            { label: 'Admin', path: '/admin', active: false, icon: "fa-user" },
            { label: 'Help', path: '/help', active: false, icon: "fa-asterisk" },
        ]

        $ctrl.leftLinks.forEach(function(link) {
            link.active = false;

            if ($location.path().endsWith(link.path)) {
                link.active = true;
            };
        });

        $ctrl.rightLinks.forEach(function(link) {
            link.active = false;

            if ($location.path().endsWith(link.path)) {
                link.active = true;
            };
        });


        $ctrl.selectLink = function(link) {
            $log.debug(link)
            this.leftLinks.forEach(function(l) {
                l.active = false;
            });

            this.rightLinks.forEach(function(l) {
                l.active = false;
            });
            link.active = true;
            $location.path(link.path)
        }
    }
})();