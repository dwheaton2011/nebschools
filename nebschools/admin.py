from django.contrib import admin

from nebschools.models import District

admin.site.register(District)

from nebschools.models import School

admin.site.register(School)