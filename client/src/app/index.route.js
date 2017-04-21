(function() {
    'use strict';

    angular
        .module('opmopApp')
        .config(routeConfig);

    /** @ngInject */
    function routeConfig($routeProvider, $locationProvider) {
        $locationProvider.html5Mode(true);
        $locationProvider.hashPrefix('#');

        $routeProvider.when('/machines', {
            templateUrl: 'app/views/machines/machines.html',
            controller: 'MachinesController',
            controllerAs: '$ctrl'
        });

        $routeProvider.when('/tasks', {
            templateUrl: 'app/views/tasks/tasks.html',
            controller: 'TasksController',
            controllerAs: '$ctrl'
        });
    }

})();