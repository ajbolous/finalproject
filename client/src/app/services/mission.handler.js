(function() {
    'use strict';

    angular
        .module('opmopApp')
        .factory('MissionHandler', MissionHandler);

    function MissionHandler($q, $log, $http, toastr) {

        var MissionHandler = function(mission) {
            this._mission = mission;
        }

        MissionHandler.prototype.getMission = function() {
            return this._mission;
        }

        MissionHandler.prototype.getMissionEvent = function() {
            return {
                title: 'Mission ' + " (" + this._mission.id + ")\n Target: (" + this._mission.target + ")",
                startsAt: this._mission.startTime,
                endsAt: this._mission.endTime,
                color: {
                    primary: '#0071c5',
                    secondary: 'aliceblue'
                },
                draggable: true, //Allow an event to be dragged and dropped
                resizable: true
            };
        }

        MissionHandler.prototype.getScheduleById = function(id) {
            return this._mission.schedules.find(function(schedule) { return schedule.id == id; });
        }

        MissionHandler.prototype.getSchedules = function() {
            return this._mission.schedules
        }

        MissionHandler.prototype.getScheduleEvents = function(schedule) {
            var events = [];
            var color = 'white';
            schedule.tasks.forEach(function(task) {
                switch (task.type) {
                    case 'haulage':
                        color = 'lightyellow';
                        break;
                    case 'load':
                        color = 'lightgreen';
                        break;
                    default:
                        color = 'aliceblue';
                }
                events.push({
                    title: ' Task ' + task.id + " (" + task.type + ")\n Machine: " + task.machineId,
                    startsAt: task.startTime,
                    endsAt: task.endTime,
                    color: {
                        primary: '#0071c5',
                        secondary: color
                    },
                    type: task.type
                });
            });
            return events;
        }

        MissionHandler.prototype.getScheduleCost = function(schedule) {
            var machines = [];
            var totalCost = 0;
            return $http.get(DJANGOURL + '/tasks/get-costs').then(function(response) {
                for (var key in response.data) {
                    totalCost += response.data[key]['total'];
                    machines.push({
                        "label": key,
                        "value": response.data[key]['total']
                    });
                }
                return machines;
            });
        }

        MissionHandler.prototype.allocateSchedule = function(schedule) {
            var self = this;
            return $http.get(DJANGOURL + '/tasks/alloc-sched', { params: { mid: this.getMission().id, sid: schedule.id } }).then(function(response) {


                var sched = response.data.mas.schedule
                sched.date = fixDate(sched.date);
                sched.tasks.forEach(function(task) {
                    task.startTime = fixDate(task.startTime);
                    task.endTime = fixDate(task.endTime);
                });

                self.getMission().schedules[sched.id] = sched;

                sched = response.data.rand.schedule
                sched.date = fixDate(sched.date);
                sched.tasks.forEach(function(task) {
                    task.startTime = fixDate(task.startTime);
                    task.endTime = fixDate(task.endTime);
                });

                return response.data;
            });

        }


        function fixDate(date) {
            var fixedDate = new Date(date);
            fixedDate.setDate(fixedDate.getDate());
            return fixedDate;
        }

        // function _getTaskAllocation(mission, date) {
        //     return $http.get(DJANGOURL + '/tasks/alloc-sched').then(function(response) {
        //         $log.debug(response);
        //     });
        // }

        return MissionHandler
    }
})();