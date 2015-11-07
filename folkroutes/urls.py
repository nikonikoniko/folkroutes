from django.conf.urls import include, url
from django.contrib import admin

from constellation.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('seconduser.urls')),
    url(r'^$', 'constellation.views.home', name='home'),
]
