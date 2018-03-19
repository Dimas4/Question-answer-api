from django.conf.urls import url, include
from django.contrib import admin
from .views import PostApiView, PostDetaokAPIView

urlpatterns = [
    url(r'^post/$', PostApiView.as_view(), name='list'),
    url(r'^post/(?P<pk>[0-9]+)/$', PostDetaokAPIView.as_view(), name='list'),

]
