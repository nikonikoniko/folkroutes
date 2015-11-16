from django.conf.urls import include, url
from django.contrib import admin

from constellation import views

urlpatterns = [
    url(r'^json/links/$', views.links_json, name='links_json'),
    url(r'^json/floatsam/$', views.floatsam_json, name='floatsam_json'),
    url(r'^jetsam/change/(?P<makerslug>[\w-]+)/(?P<slug>[\w-]+)/$', views.add_jetsam, name='add_jetsam'),
    url(r'^jetsam/change/(?P<makerslug>[\w-]+)/$', views.add_jetsam, name='add_jetsam'),
    url(r'^jetsam/change$', views.add_jetsam, name='add_jetsam'),
    url(r'^(?P<slug>[\w-]+)/$', views.floatsam_detail, name='floatsam_detail'),
    url(r'^json/(?P<slug>[\w-]+)/$', views.json_floatsam_detail, name='json_floatsam_detail'),



]
