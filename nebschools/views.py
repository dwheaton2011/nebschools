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
    act_objects = ACT.objects.filter(agencykey=school).order_by('-school_year')
    grad_objects = CohortGrad.objects.filter(agencykey=school).exclude(grad_pct=None).order_by('-school_year')
    ell_objects = ELL.objects.filter(agencykey=school).exclude(ellpct=None).order_by('-school_year')
    enrollment_objects = Enrollment.objects.filter(agencykey=school).order_by('-school_year')
    fed_objects = FedAcct.objects.filter(agencykey=school).order_by('-school_year')
    frl_objects = FRL.objects.filter(agencykey=school)
    nesa_objects = NESAscores.objects.filter(agencykey=school).exclude(math_avg_score=None)
    dictionaries = {"school" : school, "act_objects" : act_objects, "grad_objects" : grad_objects, "ell_objects" : ell_objects, "enrollment_objects" : enrollment_objects, "fed_objects" : fed_objects, "frl_objects" : frl_objects, "nesa_objects" : nesa_objects}
    return render_to_response ("schools.html", dictionaries)


def Search(request):
    query = request.GET.get('q', '')
    #exploded = query.split(" ")
    #district_qset = Q()
    #school_qset = Q()
    #for term in exploded:
    #    district_qset &= Q(standard_name__icontains=term) | Q(candidate_detail__cand_name__icontains=term)
    #    
    #for term in exploded:
    #    school_qset &= Q(cand_name__icontains=term)
    if query:
        district_results = District.objects.filter(distname__icontains=query)
        school_results = School.objects.filter(schoolname__icontains=query)
    else:
        district_results = []
        school_results = []
    dictionaries = { 'district_results': district_results, 'school_results': school_results, 'query': query, }
    return render_to_response('search.html', dictionaries)