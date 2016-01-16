from django.conf.urls import include, url
from ipscdb import views

urlpatterns = [ 
    url(r'^$', views.about),
    url(r'^search$', views.index),
    url(r'^genes$', views.genes),
    url(r'^research$', views.research),
    url(r'^contact$', views.contact),
    url(r'^faqs$', views.faqs),
    url(r'^studies$', views.studies),
    url(r'^disclaimer$', views.disclaimer),
]
