from .models import *
from django.shortcuts import *
from django.db.models import *
from schools.models import *
from django.http import HttpResponse
import datetime

last_updated = datetime.datetime(2015, 12, 5)
total_count = School.objects.aggregate(quoi=Sum("num"))

def index(request):
    return HttpResonse("hello world")

""""

def Main(request):
    sum_by_year = Refugee.objects.values("year").annotate(Sum("num")).order_by('year')
    sum_by_state = Refugee.objects.values("stateabbr", "stateabbr__statename").annotate(Sum("num")).order_by('stateabbr__statename')
    dictionaries = {'total_count':total_count, 'sum_by_year':sum_by_year,'sum_by_state':sum_by_state, 'sum_by_country':sum_by_country,'last_updated':last_updated,}
    return render_to_response('refugees/main.html', dictionaries)

def State(request, st):
    state = st
    refs = Refugee.objects.filter(stateabbr=st)
    state_total = refs.aggregate(Sum("num"))
    first = refs[0]
    state_sum_by_country = refs.values("countrycode__name").annotate(Sum("num"))
    sum_by_city = refs.values("city", "countrycode", "countrycode__name").annotate(Sum("num")).order_by('city')
    state_sum_by_year = refs.values("year").annotate(Sum("num")).order_by('year')
    dictionaries = {'state_sum_by_country':state_sum_by_country, 'sum_by_country':sum_by_country, 'sum_by_year':state_sum_by_year, 'sum_by_city':sum_by_city, 'state':state, 'first':first, 'state_total':state_total, 'list_of_states':list_of_states,}
    return render_to_response('refugees/state.html', dictionaries)

def Country(request, country):
    refs = Refugee.objects.filter(countrycode=country)
    country_total = refs.aggregate(Sum("num"))
    first = refs[0]
    sum_by_state = refs.values("stateabbr", "stateabbr__statename", "stateabbr__fips").annotate(Sum("num")).order_by('stateabbr__statename')
    country_sum_by_year = refs.values("year").annotate(Sum("num")).order_by('year')
    dictionaries = {'country_total': country_total, 'first':first, 'sum_by_state':sum_by_state, 'country_sum_by_year':country_sum_by_year, 'list_of_states':list_of_states, 'sum_by_country':sum_by_country,}
    return render_to_response('refugees/country.html', dictionaries)

def About(request):
    dictionaries = {'total_count':total_count, 'last_updated':last_updated,}
    return render_to_response('refugees/about.html', dictionaries)
    
    """"