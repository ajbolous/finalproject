"""opmop_server URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
# import view files here
import machines.views as machineViews
import tasks.views as tasksViews

import maps.views as mapViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tasks/get-all', tasksViews.getTasks),
    url(r'^tasks/get-cost', tasksViews.getMissionCosts), 
        url(r'^tasks/get-schedules', tasksViews.getSchedules),

    url(r'^machines/add', machineViews.addMachine),
    url(r'^machines/edit', machineViews.editMachine),
    url(r'^machines/get-all', machineViews.getMachines),
    url(r'^machines/delete', machineViews.deleteMachine),
    url(r'^machines/get-route', machineViews.getMachineRoute),
    url(r'^maps/get-roads', mapViews.getRoads),
    url(r'^maps/add-location', mapViews.addLocation),
    url(r'^maps/get-locations', mapViews.getLocations)
]
