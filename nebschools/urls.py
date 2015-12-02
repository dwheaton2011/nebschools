from django.conf.urls import *
from . import views

urlpatterns = patterns["",
    url(r'^', 'schools.views.Index', name="index"),
]