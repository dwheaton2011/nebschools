from django.db import models

# Create your models here. 
#this stuff is pipe deliniated
#anything mathy or ranked has to be intergers or floats. 
#on long text strings, do max legenth 225

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
        return "/district/%i/" % self.id
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
        return "/schools/%i/" % self.id
    def __unicode__(self):
        return self.schoolname
    
class ACT(models.Model):
    agencykey = models.ForeignKey(School)
    school_year = models.CharField(max_length=255) #make sure the format is 20122013 not 2012-2013
    actenglish = models.FloatField(blank=True, null=True) #save methods are bunk, do this instead.
    actmath = models.FloatField(blank=True, null=True)
    actreading = models.FloatField(blank=True, null=True)
    actscience = models.FloatField(blank=True, null=True)
    actcomposite = models.FloatField(blank=True, null=True)
    concatid = models.CharField(max_length=255) #convert all of the models to this style. 
#    def save(self, **kwargs):
#        self.concatid = self.concatid.replace("-","")
#        self.school_year = self.school_year.replace("-","")
#        self.actenglish = self.actenglish.replace(-1.0,"") #does this have to be "" or not?
#        self.actmath = self.actenglish.replace(-1.0,"")
#        self.actreading = self.actenglish.replace(-1.0,"")
#        self.actscience = self.actenglish.replace(-1.0,"")
#        self.actcomposite = self.actenglish.replace(-1.0","")
#        super(ACT, self).save()
        
class CohortGrad(models.Model):
    agencykey = models.ForeignKey(School)
    school_year = models.CharField(max_length=255)
    grad_pct = models.CharField(max_length=255, blank=True, null=True) #note that they're -1s
    concatid = models.CharField(max_length=255)
    #def save(self):
        #self.grad_pct = self.grad_pct.replace("-1.0","")
        #super(CohortGrad, self).save()

class Dropout(models.Model):
    agencykey = models.ForeignKey(District)
    school_year = models.CharField(max_length=255)
    dropout_rate = models.FloatField(blank=True, null=True)
    concatid = models.CharField(max_length=255)
    #def save(self):
        #self.dropout_rate = self.dropout_rate.replace("-1.0000","")
        #super(Dropout, self).save()
    
class ELL(models.Model):
    agencykey = models.ForeignKey(School)
    school_year = models.CharField(max_length=255)
    ellpct = models.FloatField(blank=True, null=True)
    #def save(self):
        #self.ellpct = self.ellpct.replace("-1.0000","")
        #super(ELL, self).save()
        
class Enrollment(models.Model):
    agencykey = models.ForeignKey(School)
    enrollment = models.IntegerField()
    school_year = models.CharField(max_length=255) #thisdata goes back the farthest
    concatid = models.CharField(max_length=255)
    
class FedAcct(models.Model):
    agencykey = models.ForeignKey(School)
    school_year = models.CharField(max_length=255)
    grade_tested = models.IntegerField()
    year_testedstatus = models.CharField(max_length=255)
    change = models.CharField(max_length=255)

class FRL(models.Model): #this data is only year-of
    agencykey = models.ForeignKey(School)
    FRLpct = models.FloatField(blank=True, null=True)
    concatid = models.CharField(max_length=255) 
    #def save(self):
        #self.FRLpct= self.FRLpct.replace("-1.0000","")
        #super(FRL, self).save()

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
    #def save(self):
        #self.school_year = self.school_year.replace("-","")
        #self.math_avg_score = self.math_avg_scrore.replace("-1.0","")
        #self.math_basic_pct = self.math_proficent_pct.replace("1.0","")
        #self.math_advanced_pct = self.math_advanced_pct.replace("-1.0","")
        #self.math_not_tested = self.math_not_tested.replace("-1.0","")
        #self.reading_avg_score = self.reading_avg_scrore.replace("-1.0","")
        #self.reading_basic_pct = self.reading_proficent_pct.replace("1.0","")
        #self.reading_advanced_pct = self.reading_advanced_pct.replace("-1.0","")
        #self.reading_not_tested = self.reading_not_tested.replace("-1.0","")
        #self.science_avg_score = self.science_avg_scrore.replace("-1.0","")
        #self.science_basic_pct = self.science_proficent_pct.replace("1.0","")
        #self.science_advanced_pct = self.science_advanced_pct.replace("-1.0","")
        #self.science_not_tested = self.science_not_tested.replace("-1.0","")
        #self.writing_avg_score = self.writing_avg_scrore.replace("-1.0","")
        #self.writing_basic_pct = self.writing_proficent_pct.replace("1.0","")
        #self.writing_advanced_pct = self.writing_advanced_pct.replace("-1.0","")
        #self.writing_not_tested = self.writing_not_tested.replace("-1.0","")
        #super(NESAscores, self).save()
        
#class SPED(models.Model)
    #id = models.CharField() #districtlevel
    #school_year = models.CharField()
    #SPEDpct = models.FloatField()
    
#class HAL(models.Model) #this is at the district level, which as percent could work
    #agencykey = models.ForeignKey(Agencies)
    #school_year = models.CharField()
    #HALpct = models.FloatField()    