"""schools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import *
from django.contrib import admin
from nebschools import views

urlpatterns = [
    url(r'^admin', include(admin.site.urls)),
    url(r'^district/(?P<district_slug>[\w-]+)/$', views.DistrictPage),
    url(r'^district/(?P<district_slug>[\w-]+)/(?P<school_slug>[\w-]+)/$', views.SchoolPage),
    url(r'^search', views.Search),
    url(r'^$', 'nebschools.views.Index'),
]
