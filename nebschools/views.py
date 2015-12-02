from nebschools.models import *
from django.shortcuts import *
from django.db.models import *
from django.http import HttpResponse
import datetime


def Index(request):
    total_count = District.objects.count()
    #districts = Districts.distslug()
    school_count = School.objects.count()
    dictionaries = {"total_count": total_count, "school_count": school_count }
    return render_to_response("index.html", dictionaries)

def DistrictPage(request):
    district_objects = District.objects.all()
    dictionaries = {"district_objects" : district_objects }
    return render_to_response("district.html", dictionaries)

def SchoolPage(request):
    school_objects = School.objects.all()
    act_objects = ACT.objects.all()
    grad_objects = CohortGrad.objects.all()
    dropout_objects = Dropout.objects.all()
    ell_objects = ELL.objects.all()
    enrollment_objects = Enrollment.objects.all()
    fed_objects = FedAcct.objects.all()
    frl_objects = FRL.objects.all()
    nesa_objects = NESAscores.objects.all()
    dictionaries = {"school_objects" : school_objects, "act_objects" : act_objects, "grad_objects" : grad_objects, "dropout_objects" : dropout_objects, "ell_objects" : ell_objects, "enrollment_objects" : enrollment_objects, "fed_objects" : fed_objects, "frl_objects" : frl_objects, "nesa_objects" : nesa_objects}
    return render_to_response ("schools.html", dictionaries)