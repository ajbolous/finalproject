(function() {
    'use strict';

    angular.module('opmopApp').controller('AlgorithmController', AlgorithmController);

    /** @ngInject */
    function AlgorithmController(toastr, $scope, $log, $uibModal, MachinesService, TasksService, ngProgressFactory) {
        var $ctrl = this;
        $ctrl.machines = [];
        $ctrl.progressbar = ngProgressFactory.createInstance();
        $ctrl.progressbar.start();
        $ctrl.tasks = undefined;
        $ctrl.schedules = [{ id: 1, name: 'sch1', target: 100, date: '1/5/2016' }]

        $ctrl.refreshMachines = function() {
            MachinesService.getAll().then(function(machines) {
                $ctrl.machines = machines;
                $ctrl.filteredMachines = undefined;
                $ctrl.progressbar.complete();
            });
        }

        $ctrl.refreshMachines();
        $ctrl.getSchedules = function() {
            TasksService.getSchedules().then(function(schedules) {
                $log.debug(schedules);
                $ctrl.schedules = schedules;
            });

        }
        $ctrl.showDetails = function(schedule) {
            $log.debug(schedule);
            $ctrl.tasks = schedule.tasks;

        }
        $ctrl.getSchedules();



    }

})();