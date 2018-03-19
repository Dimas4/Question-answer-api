from django.conf.urls import url, include
from django.contrib import admin
from .views import home, send, delete

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^(?P<pk>[0-9]+)/send/$', send, name='send'),
    url(r'^(?P<pk>[0-9]+)/delete/$', delete, name='delete')
]
