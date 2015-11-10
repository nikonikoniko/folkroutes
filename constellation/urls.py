from django.conf.urls import include, url
from django.contrib import admin

from constellation import views

urlpatterns = [
    url(r'^(?P<slug>[0-9]+)/$', views.floatsam_detail, name='floatsam_detail'),
    url(r'^json/(?P<slug>[0-9]+)/$', views.json_floatsam_detail, name='json_floatsam_detail'),
]
