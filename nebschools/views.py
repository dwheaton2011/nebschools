from nebschools.models import *
from django.shortcuts import *
from django.db.models import *
from django.http import HttpResponse
import datetime


def Index(request):
    total_count = District.objects.count()
    school_count = School.objects.count()
    dictionaries = {"total_count": total_count, "school_count": school_count }
    return render_to_response("index.html", dictionaries)

def DistrictPage(request):
    district_objects = District.objects.all()
    dictionaries = {"district_objects" : district_objects }
    return render_to_response("district.html", dictionaries)

""""

def Districts(request):
    #a count of the districts
    #a dropdown menu to select distructs
    return render_to_response('', dictionaries)

def Schools(request):

    return render_to_response('',dictionaries)

"""