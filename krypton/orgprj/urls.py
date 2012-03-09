from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

from .views import project_page

urlpatterns = patterns('',
    url(r'^(?P<prj_path>[^~]*)/$', project_page, name='project_page'),
)

for tool in settings.KRYPTON_TOOLS:
    m = __import__(tool + '.urls')
    urlpatterns += m.urls.urlpatterns
