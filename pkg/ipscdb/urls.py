from django.conf.urls import patterns, include, url
from ipscdb import views

urlpatterns = patterns('',
    url(r'^$', views.about, name='about'),
    url(r'^search$', views.search, name='search'),
    url(r'^research$', views.research, name='research'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^faqs$', views.faqs, name='faqs'),
    url(r'^studies$', views.studies, name='studies'),
    # url(r'^home/', 'views.home', name='home'),
)
