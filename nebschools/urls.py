from django.conf.urls import *

urlpatterns = patterns("",
    (r'^', 'schools.templates.index.html'),
)