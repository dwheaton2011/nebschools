from django.db import models


class District(models.Model):
    agencykey = models.CharField (primary_key=True, max_length=255)
    distid = models.CharField(max_length=255)
    distname = models.CharField(max_length=255)
    distslug = models.SlugField()
    county = models.CharField(max_length=255)
    dist_id = models.CharField(max_length=255)
    state_acc = models.CharField(max_length=255)
    nca_acc = models.CharField(max_length=255)
    esu = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    def get_absolute_url(self):
        return "/district/%s/" % self.distslug
    def __unicode__(self):
        return self.distname

class School(models.Model):
    agencykey = models.CharField (db_index=True, max_length=255)
    district = models.ForeignKey(District)
    schoolslug = models.SlugField()
    schoolname = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    dist_id = models.CharField(max_length=255)
    state_acc = models.CharField(max_length=255)
    nca_acc = models.CharField(max_length=255)
    esu = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    def get_absolute_url(self):
        return "/district/%s/%s/" % (self.district.distslug, self.schoolslug)
    def __unicode__(self):
        return self.schoolname
    
class ACT(models.Model):
    agencykey = models.ForeignKey(School)
    school_year = models.CharField(max_length=255)
    actenglish = models.FloatField(blank=True, null=True)
    actmath = models.FloatField(blank=True, null=True)
    actreading = models.FloatField(blank=True, null=True)
    actscience = models.FloatField(blank=True, null=True)
    actcomposite = models.FloatField(blank=True, null=True)
    concatid = models.CharField(max_length=255) 
        
class CohortGrad(models.Model):
    agencykey = models.ForeignKey(School)
    school_year = models.CharField(max_length=255)
    grad_pct = models.CharField(max_length=255, blank=True, null=True) #note that they're -1s
    concatid = models.CharField(max_length=255)

class Dropout(models.Model):
    agencykey = models.ForeignKey(District)
    school_year = models.CharField(max_length=255)
    dropout_rate = models.FloatField(blank=True, null=True)
    concatid = models.CharField(max_length=255)
    
class ELL(models.Model):
    agencykey = models.ForeignKey(School)
    school_year = models.CharField(max_length=255)
    ellpct = models.FloatField(blank=True, null=True)
        
class Enrollment(models.Model):
    agencykey = models.ForeignKey(School)
    enrollment = models.IntegerField()
    school_year = models.CharField(max_length=255)
    concatid = models.CharField(max_length=255)
    
class FedAcct(models.Model):
    agencykey = models.ForeignKey(School)
    school_year = models.CharField(max_length=255)
    grade_tested = models.IntegerField()
    year_testedstatus = models.CharField(max_length=255)
    change = models.CharField(max_length=255)

class FRL(models.Model):
    agencykey = models.ForeignKey(School)
    FRLpct = models.FloatField(blank=True, null=True)
    concatid = models.CharField(max_length=255) 

class NESAscores(models.Model):
    agencykey = models.ForeignKey(School)
    school_year = models.CharField(max_length=255)
    math_avg_score = models.FloatField(blank=True, null=True)
    grade = models.CharField(max_length=2)
    math_basic_pct = models.FloatField(blank=True, null=True)
    math_proficent_pct = models.FloatField(blank=True, null=True)
    math_advanced_pct = models.FloatField(blank=True, null=True)
    math_not_tested = models.FloatField(blank=True, null=True)
    reading_avg_score = models.FloatField(blank=True, null=True)
    reading_basic_pct = models.FloatField(blank=True, null=True)
    reading_proficent_pct = models.FloatField(blank=True, null=True)
    reading_advanced_pct = models.FloatField(blank=True, null=True)
    reading_not_tested = models.FloatField(blank=True, null=True)
    science_avg_score = models.FloatField(blank=True, null=True)
    science_basic_pct = models.FloatField(blank=True, null=True)
    science_proficent_pct = models.FloatField(blank=True, null=True)
    science_advanced_pct = models.FloatField(blank=True, null=True)
    science_not_tested = models.FloatField(blank=True, null=True)
    writing_avg_score = models.FloatField(blank=True, null=True)
    writing_basic_pct = models.FloatField(blank=True, null=True)
    writing_proficent_pct = models.FloatField(blank=True, null=True)
    writing_advanced_pct = models.FloatField(blank=True, null=True)
    writing_not_tested = models.FloatField(blank=True, null=True)
    concat_join_id = models.CharField(max_length=255)