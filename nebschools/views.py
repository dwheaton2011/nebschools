from nebschools.models import *
from django.shortcuts import *
from django.db.models import *
from schools.models import *
from django.http import HttpResponse
import datetime

last_updated = datetime.datetime(2015, 12, 5)
total_count = School.objects.aggregate(quoi=Sum("num"))

def index(request):
    return HttpResonse("hello world")