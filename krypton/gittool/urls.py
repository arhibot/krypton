from django.conf.urls.defaults import patterns, include, url

from .views import show_tree

urlpatterns = patterns('',
    url(r'(?P<path>.+)/~git/$', show_tree, name="show_default_tree", kwargs={'ref': None}),
    url(r'(?P<path>.+)/~git/tree/(?P<ref>.*)/$', show_tree, name="show_ref_tree"),
)
