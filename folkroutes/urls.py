from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from constellation.views import *

from folkroutes import settings

urlpatterns = [
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('seconduser.urls')),
    url(r'^floatsam/', include('constellation.urls')),
    url(r'^$', 'constellation.views.home', name='home'),
    url(r'^directory/$', 'constellation.views.directory', name='directory'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
]
