from nebschools.models import *
from django.shortcuts import *
from django.db.models import *
from django.http import HttpResponse
import datetime


def Index(request):
    total_count = District.objects.count()
    districts = District.objects.order_by('distname')
    school_count = School.objects.count()
    dictionaries = {"total_count": total_count, "school_count": school_count, "districts": districts }
    return render_to_response("index.html", dictionaries)

def DistrictPage(request, district_slug):
    dist = District.objects.get(distslug=district_slug)
    schools = School.objects.filter(district=dist)
    drop = Dropout.objects.filter(agencykey=dist)
    dictionaries = {"dist" : dist, "schools": schools, "drop": drop }
    return render_to_response("district.html", dictionaries)

def SchoolPage(request, district_slug, school_slug):
    school = School.objects.get(district__distslug=district_slug, schoolslug=school_slug)
    act_objects = ACT.objects.filter(agencykey=school)
    grad_objects = CohortGrad.objects.filter(agencykey=school)
    ell_objects = ELL.objects.filter(agencykey=school)
    enrollment_objects = Enrollment.objects.filter(agencykey=school)
    fed_objects = FedAcct.objects.filter(agencykey=school)
    frl_objects = FRL.objects.filter(agencykey=school)
    nesa_objects = NESAscores.objects.filter(agencykey=school)
    dictionaries = {"school" : school, "act_objects" : act_objects, "grad_objects" : grad_objects, "ell_objects" : ell_objects, "enrollment_objects" : enrollment_objects, "fed_objects" : fed_objects, "frl_objects" : frl_objects, "nesa_objects" : nesa_objects}
    return render_to_response ("schools.html", dictionaries)