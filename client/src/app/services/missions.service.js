(function() {
    'use strict';

    angular
        .module('opmopApp')
        .service('MissionsService', MissionsService);

    function MissionsService($q, $log, $http, toastr, MissionHandler) {

        var missions = [];

        function fixDate(date) {
            var fixedDate = new Date(date);
            // fixedDate.setDate(fixedDate.getDate());
            return fixedDate;
        }

        function _getMissions(date) {
            return $http.get(DJANGOURL + '/tasks/get-missions').then(function(response) {
                missions = [];
                response.data.forEach(function(mission) {
                    mission.startTime = fixDate(mission.startTime);
                    mission.endTime = fixDate(mission.endTime);
                    mission.schedules.forEach(function(sched) {
                        sched.date = fixDate(sched.date);
                        sched.tasks.forEach(function(task) {
                            task.startTime = fixDate(task.startTime);
                            task.endTime = fixDate(task.endTime);
                        });
                    });
                    missions.push(new MissionHandler(mission));
                });
                return missions;
            });
        }

        return {
            getMissions: _getMissions,
        }
    }
})();