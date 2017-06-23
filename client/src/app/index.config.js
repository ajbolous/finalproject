var SERVERIP = "0.0.0.0";
var DJANGOURL = "http://" + SERVERIP + ":8000";

(function() {
    'use strict';



    angular
        .module('opmopApp')
        .config(config)
        .constant('malarkey', malarkey)
        .constant('toastr', toastr)
        .constant('moment', moment);

    /** @ngInject */
    function config($logProvider, toastr, $routeProvider, $locationProvider) {
        // Enable log
        $logProvider.debugEnabled(true);

        // Set options third-party lib
        toastr.options.timeOut = 3000;
        toastr.options.positionClass = 'toast-top-right';
        toastr.options.preventDuplicates = true;
        toastr.options.progressBar = true;

        // Set Router
        $locationProvider.html5Mode(true);
        $locationProvider.hashPrefix('#');

        //ROUTES 
        $routeProvider.when('/', {
            templateUrl: 'app/views/main/main.html',
            controller: 'MainController',
            controllerAs: '$ctrl'
        });

        $routeProvider.when('/machines', {
            templateUrl: 'app/views/machines/machines.html',
            controller: 'MachinesController',
            controllerAs: '$ctrl'
        });

        $routeProvider.when('/missions', {
            templateUrl: 'app/views/missions/missions.html',
            controller: 'MissionsController',
            controllerAs: '$ctrl'
        });
    }

})();