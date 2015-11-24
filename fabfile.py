#fabfile.py

#process of getting stuff out of the Ed data tables into something much more useable. 

# how to join :: csvjoin -d "|" -c "concat_join_id,concat_join_id,concat_join_id,concat_join_id" math.txt reading.txt science.txt writing.txt | csvcut -c "id,year,math_grade, math_avg_score,math_basic_pct,math_proficient_pct,math_advanced_pct,math_not_tested_pct,reading_avg_score, reading_grade, reading_basic_pct,reading_proficient_pct,reading_advanced_pct,reading_not_tested_pct,science_avg_score, science_grade, science_basic_pct,science_proficient_pct,science_advanced_pct,science_not_tested_pct,writing_avg_score, writing_grade, writing_basic_pct,writing_proficient_pct,writing_advanced_pct,writing_not_tested_pct,concat_join_id" > scores_joined.txt


#id,year,math_avg_score,math_basic_pct,math_proficient_pct,math_advanced_pct,math_not_tested_pct,concat_join_id,id,year,reading_avg_score,reading_basic_pct,reading_proficient_pct,reading_advanced_pct,reading_not_tested_pct,concat_join_id,id,year,science_avg_score,science_basic_pct,science_proficient_pct,science_advanced_pct,science_not_tested_pct,concat_join_id,id,year,writing_avg_score,writing_basic_pct,writing_proficient_pct,writing_advanced_pct,writing_not_tested_pct,concat_join_id

#id,year,math_avg_score,math_grade,math_basic_pct,math_proficient_pct,math_advanced_pct,math_not_tested_pct,concat_join_id,id,year,reading_avg_score,reading_grade,reading_basic_pct,reading_proficient_pct,reading_advanced_pct,reading_not_tested_pct,concat_join_id,id,year,science_avg_score,science_grade,science_basic_pct,science_proficient_pct,science_advanced_pct,science_not_tested_pct,concat_join_id,id,year,writing_avg_score,writing_grade,writing_basic_pct,writing_proficient_pct,writing_advanced_pct,writing_not_tested_pct,concat_join_id 13,22,31 (1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,32,33,34,35,36)

#1id,2year,3math_avg_score,4grade,5math_basic_pct,6math_proficient_pct,7math_advanced_pct,8math_not_tested_pct,9concat_join_id,10id,11year,12reading_avg_score,13reading_basic_pct,14reading_proficient_pct,15eading_advanced_pct,16reading_not_tested_pct,17concat_join_id,18id,19year,20science_avg_score,21science_basic_pct,22science_proficient_pct,23science_advanced_pct,24science_not_tested_pct,25concat_join_id,26id,27year,28writing_avg_score,29writing_basic_pct,30writing_proficient_pct,31writing_advanced_pct,32writing_not_tested_pct,33concat_join_id (1,2,3,4,5,6,7,8,12,13,14,15,16,20,21,22,23,24,28,29,30,31,32,33)
""""
1agencykey = models.ForeignKey(School)
    2school_year = models.CharField(max_length=255)
    3math_avg_score = models.FloatField(blank=True, null=True)
    4grade = models.CharField(max_length=2)
    5math_basic_pct = models.FloatField(blank=True, null=True)
    6math_proficent_pct = models.FloatField(blank=True, null=True)
    7math_advanced_pct = models.FloatField(blank=True, null=True)
    8math_not_tested = models.FloatField(blank=True, null=True)
    12reading_avg_score = models.FloatField(blank=True, null=True)
    13reading_basic_pct = models.FloatField(blank=True, null=True)
    14reading_proficent_pct = models.FloatField(blank=True, null=True)
    15reading_advanced_pct = models.FloatField(blank=True, null=True)
    16reading_not_tested = models.FloatField(blank=True, null=True)
    20science_avg_score = models.FloatField(blank=True, null=True)
    21science_basic_pct = models.FloatField(blank=True, null=True)
    22science_proficent_pct = models.FloatField(blank=True, null=True)
    23science_advanced_pct = models.FloatField(blank=True, null=True)
    24science_not_tested = models.FloatField(blank=True, null=True)
    28writing_avg_score = models.FloatField(blank=True, null=True)
    29writing_basic_pct = models.FloatField(blank=True, null=True)
    30writing_proficent_pct = models.FloatField(blank=True, null=True)
    31writing_advanced_pct = models.FloatField(blank=True, null=True)
    32writing_not_tested = models.FloatField(blank=True, null=True)
    33concat_join_id = models.CharField(max_length=255)
""""





import csv
import fabric
from fabric.api import *

SCHOOLYEAR = "20132014"
fabric.state.output.status = False

def mungeAgencies(file):
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
               if row[1] == SCHOOLYEAR and row[0] == "SC":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                school_name = row[5]
                concat_id = county + dist_id + school_id
                state_acc = row[6]
                nca_acc = row[7]
                esu = row[8]
                title = row[9]
                concat_joinid = concat_id + year
                ls = [concat_id, school_id, school_name, county, dist_id, state_acc, nca_acc, esu, title, concat_joinid]
                print "|".join(ls)
                
def district(file):
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
               if row[1] == SCHOOLYEAR and row[0] == "DI":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                school_name = row[5]
                concat_id = county + dist_id + school_id
                state_acc = row[6]
                nca_acc = row[7]
                esu = row[8]
                title = row[9]
                concat_joinid = concat_id + year
                ls = [concat_id, school_id, school_name, county, dist_id, state_acc, nca_acc, esu, title, concat_joinid]
                print "|".join(ls)                
                
                
def sesscores(file):
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if row[1] == SCHOOLYEAR and row[0] == "SC":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                school_name = row[5]
                concat_id = county + dist_id + school_id
                FRL_pct = row[6]
                concat_joinid = concat_id + year
                sls = [concat_id, FRL_pct, concat_joinid]
                print "|".join(sls)
                
def cohortgrad(file):
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if  row[0] == "SC" and row[8] == "All students":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                school_name = row[5]
                concat_id = county + dist_id + school_id
                grad_pct = row[10]
                concat_joinid = concat_id + year
                sls = [concat_id, year, grad_pct, concat_joinid]
                print "|".join(sls) 
                
def MaleGrad(file):
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if  row[0] == "SC" and row[8] == "Male":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                school_name = row[5]
                concat_id = county + dist_id + school_id
                grad_pct = row[10]
                concat_joinid = concat_id + year
                sls = [concat_id, year, grad_pct, concat_joinid]
                print "|".join(sls)
                
def FemaleGrad(file):
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if  row[0] == "SC" and row[8] == "Female":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                school_name = row[5]
                concat_id = county + dist_id + school_id
                grad_pct = row[10]
                concat_joinid = concat_id + year
                sls = [concat_id, year, grad_pct, concat_joinid]
                print "|".join(sls)    
                
def FRLGrad(file):
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if  row[0] == "SC" and row[8] == "Students eligible for free and reduced lunch":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                school_name = row[5]
                concat_id = county + dist_id + school_id
                grad_pct = row[10]
                concat_joinid = concat_id + year
                sls = [concat_id, year, grad_pct, concat_joinid]
                print "|".join(sls)                
                
def SPEDGrad(file):
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if  row[0] == "SC" and row[8] == "Special Education Students":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                school_name = row[5]
                concat_id = county + dist_id + school_id
                grad_pct = row[10]
                concat_joinid = concat_id + year
                sls = [concat_id, year, grad_pct, concat_joinid]
                print "|".join(sls)                
                
def ELLGrad(file):
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if  row[0] == "SC" and row[8] == "English Language Learners":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                school_name = row[5]
                concat_id = county + dist_id + school_id
                grad_pct = row[10]
                concat_joinid = concat_id + year
                sls = [concat_id, year, grad_pct, concat_joinid]
                print "|".join(sls)  
                
def HispanicGrad(file):
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if  row[0] == "SC" and row[8] == "Ethnic7 - Hispanic":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                school_name = row[5]
                concat_id = county + dist_id + school_id
                grad_pct = row[10]
                concat_joinid = concat_id + year
                sls = [concat_id, year, grad_pct, concat_joinid]
                print "|".join(sls)
                
def NativeGrad(file):
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if  row[0] == "SC" and row[8] == "Ethnic7 - American Indian/Alaska Native":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                school_name = row[5]
                concat_id = county + dist_id + school_id
                grad_pct = row[10]
                concat_joinid = concat_id + year
                sls = [concat_id, year, grad_pct, concat_joinid]
                print "|".join(sls)

def AsianGrad(file):
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if  row[0] == "SC" and row[8] == "Ethnic7 - Asian":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                school_name = row[5]
                concat_id = county + dist_id + school_id
                grad_pct = row[10]
                concat_joinid = concat_id + year
                sls = [concat_id, year, grad_pct, concat_joinid]
                print "|".join(sls)
                
def BlackGrad(file):
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if  row[0] == "SC" and row[8] == "Ethnic7 - Black or African American":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                school_name = row[5]
                concat_id = county + dist_id + school_id
                grad_pct = row[10]
                concat_joinid = concat_id + year
                sls = [concat_id, year, grad_pct, concat_joinid]
                print "|".join(sls)                
                
def PacificGrad(file):
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if  row[0] == "SC" and row[8] == "Ethnic7 - Native Hawaiian or Other Pacific Islander":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                school_name = row[5]
                concat_id = county + dist_id + school_id
                grad_pct = row[10]
                concat_joinid = concat_id + year
                sls = [concat_id, year, grad_pct, concat_joinid]
                print "|".join(sls)  
                
def WhiteGrad(file):
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if  row[0] == "SC" and row[8] == "Ethnic7 - White":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                school_name = row[5]
                concat_id = county + dist_id + school_id
                grad_pct = row[10]
                concat_joinid = concat_id + year
                sls = [concat_id, year, grad_pct, concat_joinid]
                print "|".join(sls)                
                
def twoormoreGrad(file):
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if  row[0] == "SC" and row[8] == "Ethnic7 - Two or More Races":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                school_name = row[5]
                concat_id = county + dist_id + school_id
                grad_pct = row[10]
                concat_joinid = concat_id + year
                sls = [concat_id, year, grad_pct, concat_joinid]
                print "|".join(sls)                
                
def dropout(file): #only district level data, what fools!
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if row[0] == "DI":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                school_name = row[5]
                concat_id = county + dist_id + school_id
                dropout_pct = row[6]
                concat_joinid = concat_id + year
                sls = [concat_id, year, dropout_pct, concat_joinid]
                print "|".join(sls)
                
def NeSAWrit(file):
    with open(file, "rb") as f:
        headers = ["id", "year", "writing_avg_score", "writing_basic_pct", "writing_proficient_pct", "writing_advanced_pct", "writing_not_tested_pct", "concat_join_id"]
        print "|".join(headers)
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if  row[0] == "SC" and row[7] == "All Students":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                concat_id = county + dist_id + school_id
                grade = row[8]
                avg_score = row[10]
                basic_pct = row [11]
                proficent_pct = row [12]
                advanced_pct = row [13]
                not_tested_pct = row [14]
                concat_joinid = concat_id + year
                sls = [concat_id, year, avg_score, grade, basic_pct, proficent_pct, advanced_pct, not_tested_pct, concat_joinid]
                print "|".join(sls)    
                
def NeSAMath(file):
    with open(file, "rb") as f:
        headers = ["id", "year", "math_avg_score", "math_basic_pct", "math_proficient_pct", "math_advanced_pct", "math_not_tested_pct", "concat_join_id"]
        print "|".join(headers)
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if  row[0] == "SC" and row[7] == "All Students":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                concat_id = county + dist_id + school_id
                grade = row[8]
                avg_score = row[10]
                basic_pct = row [11]
                proficent_pct = row [12]
                advanced_pct = row [13]
                not_tested_pct = row [14]
                concat_joinid = concat_id + year
                sls = [concat_id, year, avg_score, grade, basic_pct, proficent_pct, advanced_pct, not_tested_pct, concat_joinid]
                print "|".join(sls)
                
                
def NeSARead(file):
    with open(file, "rb") as f:
        headers = ["id", "year", "reading_avg_score", "reading_basic_pct", "reading_proficient_pct", "reading_advanced_pct", "reading_not_tested_pct", "concat_join_id"]
        print "|".join(headers)
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if  row[0] == "SC" and row[7] == "All Students":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                concat_id = county + dist_id + school_id
                grade = row[8]
                avg_score = row[10]
                basic_pct = row [11]
                proficent_pct = row [12]
                advanced_pct = row [13]
                not_tested_pct = row [14]
                concat_joinid = concat_id + year
                sls = [concat_id, year, avg_score, grade, basic_pct, proficent_pct, advanced_pct, not_tested_pct, concat_joinid]
                print "|".join(sls)  
                
def NeSASci(file):
    with open(file, "rb") as f:
        headers = ["id", "year", "science_avg_score", "science_basic_pct", "science_proficient_pct", "science_advanced_pct", "science_not_tested_pct", "concat_join_id"]
        print "|".join(headers)
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if  row[0] == "SC" and row[7] == "All Students":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                concat_id = county + dist_id + school_id
                grade = row[8]
                avg_score = row[10]
                basic_pct = row [11]
                proficent_pct = row [12]
                advanced_pct = row [13]
                not_tested_pct = row [14]
                concat_joinid = concat_id + year
                sls = [concat_id, year, avg_score, grade, basic_pct, proficent_pct, advanced_pct, not_tested_pct, concat_joinid]
                print "|".join(sls)                   
           
                
def ACT(file):
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if row[0] == "SC":
                school_year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                concat_id = county + dist_id + school_id
                school_name = row[5]
                English = row[8]
                Math = row[9]
                Reading = row[10]
                Science = row[11]
                Composite = row[12]
                concat_joinid = concat_id + school_year
                sls = [concat_id, school_year, English, Math, Reading, Science, Composite, concat_joinid]
                print "|".join(sls)
                
def Enrollment(file):
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if row[0] == "SC":
                year = row [1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                concat_id = county + dist_id + school_id
                membership = row[20]
                concat_joinid = concat_id + year
                sls = [concat_id, membership, year, concat_joinid]
                print "|".join(sls)
                
def ELL(file):
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if row[0] == "SC":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                concat_id = county + dist_id + school_id
                ell = row[6]
                concat_joinid = concat_id + year
                sls = [concat_id, year, ell]
                print "|".join(sls)
                
def Fedacct(file):
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if row[0] == "SC":
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                concat_id = county + dist_id + school_id
                grade = row[6]
                thisyear = row[9]
                status = row[11]
                concat_joinid = concat_id + year
                sls = [concat_id, year, grade, thisyear, status]
                print "|".join(sls)
                
def Hal(file): #again, at the blasted districted level
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                concat_id = county + dist_id + school_id
                HAL_pct = row[6]
                concat_joinid = concat_id + year
                sls = [concat_id, year, HAL_pct]
                print "|".join(sls)
                
def SPED(file): #again, at the blasted districted level
    with open(file, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
                year = row[1]
                county = row[2]
                dist_id = row[3]
                school_id = row[4]
                concat_id = county + dist_id + school_id
                sped_pct = row[6]
                concat_joinid = concat_id + year
                sls = [concat_id, year, sped_pct]
                print "|".join(sls)
                                
                    
