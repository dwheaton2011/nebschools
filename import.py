import sys, os, string
import csv
import django
csv.register_dialect('piper', delimiter='|')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "schools.settings")
django.setup()
from nebschools.models import District, School, ACT, CohortGrad, Dropout, ELL, Enrollment, FedAcct, FRL, NESAscores
import urllib, urllib2, string, datetime, time, re
from django.template.defaultfilters import slugify, urlize

#"""
"""
with open("districts.txt", "rb") as csvfile:
    readerpipe = csv.reader(csvfile, delimiter='|')
    for row in readerpipe:
        distid = row[0]
        distnm = row[2].title()
        county = row[3]
        dist_id = row[4]
        state_acc = row[5]
        nca_acc = row[6]
        esu = row[7]
        title = row[8]
        d, dcreated = District.objects.get_or_create(agencykey=distid, distname=distnm,  distslug=slugify(distnm), county=county, dist_id=dist_id, state_acc=state_acc, nca_acc=nca_acc, esu=esu, title=title)
        print d
"""
"""
with open("Agencies.txt", "rb") as csvfile:
    readerpipe = csv.reader(csvfile, delimiter='|')
    for row in readerpipe:
        schoolid = row[0]
        schoolnm = row[2].title()
        county = row[3]
        dist_id = row[4]
        state_acc = row[5]
        nca_acc = row[6]
        esu = row[7]
        title = row[8]
        distunique = row[0][:6]+"000"
        d = District.objects.get(agencykey=distunique)
        s, screated = School.objects.get_or_create(district=d, agencykey=schoolid, schoolname=schoolnm,  schoolslug=slugify(schoolnm), county=county, dist_id=dist_id, state_acc=state_acc, nca_acc=nca_acc, esu=esu, title=title)
        #print s
""" 

"""        
with open("ACT.txt", "rb") as csvfile:
    readerpipe = csv.reader(csvfile, delimiter='|')
    for row in readerpipe:
        try:
            schoolid = row[0]
            school_year = row[1]
            if row[2] == "-1.0":
                actenglish = None
            else: 
                actenglish = float(row[2])
            if row[3] == "-1.0":
                actmath = None
            else:
                actmath = float(row[3])
            if row[4] == "-1.0":
                actreading = None
            else: 
                actreading = float(row[4])
            if row[5] == "-1.0":
                actscience = None
            else:
                actscience = float(row[5])
            if row[6] == "-1.0":
                actomposite = None
            else:
                actcomposite = float(row[6])
            concatid = row[7]
            s = School.objects.get(agencykey=schoolid)
            a, acreated = ACT.objects.get_or_create(agencykey=s, school_year=school_year, actenglish=actenglish, actmath = actmath, actreading=actreading, actscience=actscience, actcomposite=actcomposite, concatid=concatid)
        except:
            print row[0]
"""    
"""
with open("CohortGrad.txt", "rb") as csvfile:
    readerpipe = csv.reader(csvfile, delimiter='|')
    for row in readerpipe:
        try:
            schoolid = row[0]
            school_year = row[1]
            if row[2] == "-1.0":
                grad_pct = None
            else: 
                grad_pct = float(row[2])
            concatid = row[3]
            s = School.objects.get(agencykey=schoolid)
            a, acreated = CohortGrad.objects.get_or_create(agencykey=s, school_year=school_year, grad_pct=grad_pct, concatid=concatid)
        except:
            print row[0] #values excepted out: 100600001, 230601001, 280602001, 300600001, 550605001
"""
""""
with open("Dropout.txt", "rb") as csvfile:
    readerpipe = csv.reader(csvfile, delimiter='|')
    for row in readerpipe:
        try:
            school_year = row[1]
            if row[2] == "-1.0":
                dropout_rate = None
            else: 
                dropout_rate = float(row[2])
            concatid = row[3]
            distunique = row[0]
            s = District.objects.get(agencykey=distunique)
            a, acreated = Dropout.objects.get_or_create(agencykey=s, school_year=school_year, dropout_rate=dropout_rate, concatid=concatid)
        except:
            print row[0] #values excepted out: 120032000 120032000 120032000 180070000 180070000 190059000 190059000 190059000 192001000 270046000 270046000 270046000 740501000 780104000 780104000
"""
"""
with open("ELL.txt", "rb") as csvfile:
    readerpipe = csv.reader(csvfile, delimiter='|')
    for row in readerpipe:
        try:
            schoolid = row[0]
            school_year = row[1]
            if row[2] == "-1.0000":
                ellpct = None
            else: 
                ellpct = float(row[2])
            s = School.objects.get(agencykey=schoolid)
            a, acreated = ELL.objects.get_or_create(agencykey=s, school_year=school_year, ellpct=ellpct)
        except:
            print row[0] #values excepted out: a lot of them, but 5105 out of 5247 were imported
"""
"""
with open("Enrollment.txt", "rb") as csvfile:
    readerpipe = csv.reader(csvfile, delimiter='|')
    for row in readerpipe:
        try:
            schoolid = row[0]
            enrollment = row[1]
            school_year = row[2]
            s = School.objects.get(agencykey=schoolid)
            a, acreated = Enrollment.objects.get_or_create(agencykey=s, enrollment=enrollment, school_year=school_year)
        except:
            print row[0] #13774 out of 17143 in the db, perhaps consolidation?
"""
"""
with open("FedAcct.txt", "rb") as csvfile:
    readerpipe = csv.reader(csvfile, delimiter='|')
    for row in readerpipe:
        try:
            schoolid = row[0]
            school_year = row[1]
            grade_tested = row[2]
            year_testedstatus = row[3]
            change = row[4]
            s = School.objects.get(agencykey=schoolid)
            a, acreated = FedAcct.objects.get_or_create(agencykey=s, school_year=school_year, grade_tested=grade_tested, year_testedstatus=year_testedstatus)
        except:
            print row[0]
"""            
"""    
# 010090004 010090005 100007017 100007020 120502005 150536002 190123006 190123006
192001001
192001001
192001002
192001002
192001003
192001004
270001018
270594002
270594003
290117003
530001004
652005009
810010010
810010010
880005006
900017002
900017003
"""
"""
with open("FRL.txt", "rb") as csvfile:  
    readerpipe = csv.reader(csvfile, delimiter='|')
    for row in readerpipe:
        try:
            schoolid = row[0]
            if row[1] == "-1.0000":
                FRLpct = None
            else: 
                FRLpct = float(row[1])    
            s = School.objects.get(agencykey=schoolid)
            a, acreated = FRL.objects.get_or_create(agencykey=s, FRLpct=FRLpct)
        except:
            print row[0] #
"""
with open("NESAscoresfull.txt", "rb") as csvfile:  
    readerpipe = csv.reader(csvfile, delimiter=',')
    for row in readerpipe:
        try:
            schoolid = row[0]
            sy1, sy2 = row[1].split("-")
            school_year = sy1+sy2
            if row[2] == "-1.00":
                math_avg_score = None
            elif row[2]== None:
                math_avg_score = None    
            else: 
                math_avg_score = float(row[2])
            grade = row[3]    
            if row[4] == "-1.00":
                math_basic_pct = None
            elif row[4]== None: #possibly, could be blanks, which is ""
                math_basic_pct = None    
            else: 
                math_basic_pct = float(row[4])
            if row[5] == "-1.00":
                math_proficent_pct = None
            elif row[5]== None:
                math_proficent_pct = None
            else: 
                math_proficent_pct = float(row[5])
            if row[6] == "-1.00":
                math_advanced_pct = None
            elif row[6]==None:
                math_advanced_pct = None
            else: 
                math_advanced_pct = float(row[6])
            if row[7] == "-1.00":
                math_not_tested = None
            elif row[7]==None:
                math_not_tested = None
            else: 
                math_not_tested = float(row[7])
            if row[8] == "-1.00":
                reading_avg_score = None
            elif row[8]==None:
                reading_avg_score = None
            else: 
                reading_avg_score = float(row[8])
            if row[9] == "-1.00":
                reading_basic_pct = None
            elif row[9]==None:
                reading_basic_pct = None    
            else: 
                reading_basic_pct = float(row[9])
            if row[10] == "-1.00":
                reading_proficent_pct = None
            elif row[10]==None:
                reading_proficent_pct = None    
            else: 
                reading_proficent_pct = float(row[10])
            if row[11] == "-1.00":
                reading_advanced_pct = None
            elif row[11]==None:
                reading_advanced_pct = None    
            else: 
                reading_advanced_pct = float(row[11])
            if row[12] == "-1.00":
                reading_not_tested = None
            elif row[12]==None:
                reading_not_tested = None    
            else: 
                reading_not_tested = float(row[12])
            if row[13] == "-1.00":
                science_avg_score = None
            elif row[13]== None:
                science_avg_score = None
            else: 
                science_avg_score = float(row[13])
            if row[14] == "-1.00":
                science_basic_pct = None
            elif row[14]==None:
                science_basic_pct = None    
            else: 
                science_basic_pct = float(row[14])
            if row[15] == "-1.00":
                science_proficent_pct = None
            elif row[15]==None:
                science_proficent_pct = None    
            else: 
                science_proficent_pct = float(row[15])
            if row[16] == "-1.00":
                science_advanced_pct = None
            elif row[16]==None:
                science_advanced_pct = None    
            else: 
                science_advanced_pct = float(row[16])
            if row[17] == "-1.00":
                science_not_tested = None
            elif row[17]==None:
                science_not_tested = None    
            else: 
                science_not_tested = float(row[17])
            if row[18] == "-1.00":
                writing_avg_score = None
            elif row[18]=="":
                writing_avg_score = None
            else: 
                writing_avg_score = float(row[18])
            if row[19] == "-1.00":
                writing_basic_pct = None
            elif row[19]=="":
                writing_basic_pct = None    
            else: 
                writing_basic_pct = float(row[19])
            if row[20] == "-1.00":
                writing_proficent_pct = None
            elif row[20]=="":
                writing_proficent_pct = None    
            else: 
                writing_proficent_pct = float(row[20])
            if row[21] == "-1.00":
                writing_advanced_pct = None
            elif row[21]=="":
                writing_advanced_pct = None    
            else: 
                writing_advanced_pct = float(row[21])
            if row[22] == "-1.00":
                writing_not_tested = None
            elif row[22]=="":
                writing_not_tested = None    
            else: 
                writing_not_tested = float(row[22])
            s = School.objects.get(agencykey=schoolid)    
            a, acreated = NESAscores.objects.get_or_create(agencykey=s, school_year=school_year, math_avg_score=math_avg_score, math_basic_pct=math_basic_pct, math_proficent_pct=math_proficent_pct, math_advanced_pct=math_advanced_pct, math_not_tested=math_not_tested, reading_avg_score=reading_avg_score, reading_basic_pct=reading_basic_pct, reading_proficent_pct=reading_proficent_pct, reading_advanced_pct=reading_advanced_pct, reading_not_tested=reading_not_tested, science_avg_score=science_avg_score, science_basic_pct=science_basic_pct, science_proficent_pct=science_proficent_pct, science_advanced_pct=science_advanced_pct, science_not_tested=science_not_tested, writing_avg_score=writing_avg_score, writing_basic_pct=writing_basic_pct, writing_proficent_pct=writing_proficent_pct, writing_advanced_pct=writing_advanced_pct, writing_not_tested=writing_not_tested, grade=grade)
        except:
            print row[0] #   


        # s=#NEWTABLE.objects.get_or_create(School=#newvariable#, agencykey=schoolid
        
"""       
                    s = School.objects.get(agencykey=schoolid)
            a = NESAscores.objects.get(agencykey=s, school_year=school_year, grade=grade)
            a.science_proficent_pct=science_proficent_pct
            a.science_advanced_pct=science_advanced_pct
            a.science_not_tested=science_not_tested,
            a.writing_avg_score=writing_avg_score
            a.writing_basic_pct=writing_basic_pct
            a.writing_proficent_pct=writing_proficent_pct
            a.writing_advanced_pct=writing_advanced_pct
            a.writing_not_tested=writing_not_tested
            a.save()
"""