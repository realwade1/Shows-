from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.allshows),
    url(r'^shows/new$', views.newshow),
    url(r'^shows/create$', views.createshow),
    url(r'^shows/(?P<id>\d+)$', views.tvshow),
    url(r'^shows/(?P<id>\d+)/edit$', views.editshow),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^edit/(?P<id>\d+)$', views.edit)
]
