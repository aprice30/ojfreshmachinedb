from django.conf.urls import patterns, url

from machine import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)