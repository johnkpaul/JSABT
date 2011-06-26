from django.conf.urls.defaults import *
from django.views.generic import ListView
from photocopy.models import Photocopy

urlpatterns = patterns('',
    url(r'^$', 'photocopy.views.home',name='home'),
    url(r'^all/', ListView.as_view(model=Photocopy,)),
    url(r'^api/search/(?P<search_query>.*)', 'photocopy.views.search', name='search'),
)
