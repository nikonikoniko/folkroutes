from django.conf.urls import include, url
from django.contrib import admin

from constellation import views

urlpatterns = [
    url(r'^json/links/$', views.links_json, name='links_json'),
    url(r'^json/floatsam/$', views.floatsam_json, name='floatsam_json'),

    url(r'^jetsam/change/(?P<makerslug>[\w-]+)/(?P<slug>[\w-]+)/$', views.add_jetsam, name='add_jetsam'),
    url(r'^jetsam/change/(?P<makerslug>[\w-]+)/$', views.add_jetsam, name='add_jetsam'),
    url(r'^jetsam/change$', views.add_jetsam, name='add_jetsam'),

    url(r'^jetsam/delete/(?P<slug>[\w-]+)/$', views.delete_jetsam, name='delete_jetsam'),


    url(r'^edit/(?P<slug>[\w-]+)/$', views.edit_floatsam, name='edit_floatsam'),
    url(r'^edit$', views.edit_floatsam, name='edit_floatsam'),

    url(r'^request/(?P<slug>[\w-]+)/$', views.request_floatsam, name='request_floatsam'),
    url(r'^request$', views.request_floatsam, name='request_floatsam'),

    url(r'^accept/(?P<initiator_slug>[\w-]+)/(?P<recipient_slug>[\w-]+)/$', views.accept_request, name='accept_request'),
    url(r'^deny/(?P<initiator_slug>[\w-]+)/(?P<recipient_slug>[\w-]+)/$', views.deny_request, name='deny_request'),


    url(r'^(?P<slug>[\w-]+)/$', views.floatsam_detail, name='floatsam_detail'),
    url(r'^json/(?P<slug>[\w-]+)/$', views.json_floatsam_detail, name='json_floatsam_detail'),



]
