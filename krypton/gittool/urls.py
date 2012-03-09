from django.conf.urls.defaults import patterns, include, url

from .views import show_obj

urlpatterns = patterns('',
    url(r'(?P<prj_path>.+)/~git/$', show_obj, name="show_object", kwargs={'ref': None, 'otype': 'tree', 'fpath': '/'}),
    url(r'(?P<prj_path>.+)/~git/(?P<otype>(tree|blob))/(?P<ref>[^/]+)/(?P<fpath>.*)/?$', show_obj, name="show_object"),
)
