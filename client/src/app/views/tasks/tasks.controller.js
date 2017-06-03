(function() {
    'use strict';

    angular.module('opmopApp').controller('TasksController', TasksController);

    /** @ngInject */
    function TasksController(toastr, $scope, $log, TasksService) {
        var $ctrl = this;
        /* alert on eventClick */

        $ctrl.events = [{ title: 'All Day Event', startsAt: new Date(2017, 5, 1) }];

        $ctrl.calendarView = "day";
        $ctrl.viewDate = new Date(2017, 5, 1, 9);

        function sortByKey(array, key1, key2) {
            return array.sort(function(a, b) {
                var x = a[key1][key2];
                var y = b[key1][key2];
                console.log(x, y)
                return ((x < y) ? -1 : ((x > y) ? 1 : 0));
            });
        }

        $ctrl.taskTypes = {
            'dig': true,
            'haulage': true,
            'load': true
        }

        $ctrl.refresh = function() {
            $log.debug($ctrl.taskTypes)
            TasksService.getAll().then(function(response) {
                var mission = response.data[0]
                $ctrl.mission = mission;
                var i = 0;
                $log.debug('mission', mission)
                $ctrl.events = [];
                mission.schedules.forEach(function(sched) {
                    //var sortedTasks = sortByKey(sched.tasks, 'machine', 'id');
                    sched.tasks.forEach(function(task) {

                        if ($ctrl.taskTypes[task.type] == false)
                            return;
                        var sd = new Date(task.startTime)
                        sd = new Date(sd.getFullYear(), sd.getMonth() + 1, sd.getDate(), sd.getHours(), sd.getMinutes());

                        var ed = new Date(task.endTime)
                        ed = new Date(ed.getFullYear(), ed.getMonth() + 1, ed.getDate(), ed.getHours(), ed.getMinutes());

                        var color = 'aliceblue';
                        if (task.type == 'haulage')
                            color = 'lightyellow'
                        else if (task.type == 'load')
                            color = 'lightgreen'

                        var t = {
                            title: ' Task ' + i++ + " (" + task.type + ")\n Machine: (" + task.machine.id + " - " + task.machine.model + ")",
                            startsAt: sd,
                            endsAt: ed,
                            color: {
                                primary: '#0071c5',
                                secondary: color
                            },
                            draggable: true, //Allow an event to be dragged and dropped
                            resizable: true
                        }
                        $ctrl.events.push(t);
                    });
                });

            });
        }
        $ctrl.refresh();
    }

})();