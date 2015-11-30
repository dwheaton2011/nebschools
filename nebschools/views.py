from nebschools.models import *
from django.shortcuts import *
from django.db.models import *
from django.http import HttpResponse
import datetime

#last_updated = datetime.datetime(2015, 12, 5)
#total_count = School.objects.aggregate(quoi=Sum("num"))

def Index(request):
    total_count = School.objects.aggregate(quoi=Sum("num"))
    dictionaries = {"total_count": total_count, }
    return render_to_response("/templates/index.html", dictionaries)
