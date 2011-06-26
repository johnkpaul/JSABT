from django.conf.urls.defaults import *
from django.views.generic import ListView
from photocopy.models import Photocopy

urlpatterns = patterns('',
    url(r'^$', 'photocopy.views.home',name='home'),
    url(r'^all/', ListView.as_view(model=Photocopy,)),
    url(r'^bookmarks/add', 'photocopy.views.bookmarks', name='add_bookmarks'),
)
