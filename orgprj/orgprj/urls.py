from django.conf.urls.defaults import patterns, include, url

from .views import project_page, route_to_tool

urlpatterns = patterns('',
    url(r'^(?P<path>.*)/$', project_page, name='project_page'),
    url(r'^(?P<path>.*)/~(?P<tool>.*)/$', route_to_tool, name='route_to_tool'),
)

