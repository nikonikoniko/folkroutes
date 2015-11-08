from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from constellation.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('seconduser.urls')),
    url(r'^floatsam/', include('constellation.urls')),
    url(r'^$', 'constellation.views.home', name='home'),
    url(r'^directory/$', 'constellation.views.directory', name='directory'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
]
