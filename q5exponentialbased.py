import csv
import pandas as pd
import numpy as np
import decimal

##clean the adult csv
f=pd.read_csv('adult.csv')
f=f[(f !='?').all(axis=1)]
f.to_csv("cleanadult.csv", index=False)


## qf(D) values
Preschool = 1
first4th = 8
fifth6th = 22
ninth = 38
twelfth = 43
seventh8th = 55
tenth = 82
eleventh = 89
AssocAcdm = 398
Doctorate = 399
AssocVoc = 504
ProfSchool = 592
Masters = 1393
SomeCollege = 1990
HSGrad = 2416
Bachelors = 3178

## S(qf)=1
Sensitivity = 1

## epsilon varies
epsilon = 0.001

## e=2.72
denominator = 0
denominator += pow(2.72, epsilon*Preschool/2)
denominator += pow(2.72, epsilon*first4th/2)
denominator += pow(2.72, epsilon*fifth6th/2)
denominator += pow(2.72, epsilon*ninth/2)
denominator += pow(2.72, epsilon*twelfth/2)
denominator += pow(2.72, epsilon*seventh8th/2)
denominator += pow(2.72, epsilon*tenth/2)
denominator += pow(2.72, epsilon*eleventh/2)
denominator += pow(2.72, epsilon*AssocAcdm/2)
denominator += pow(2.72, epsilon*Doctorate/2)
denominator += pow(2.72, epsilon*AssocVoc/2)
denominator += pow(2.72, epsilon*ProfSchool/2)
denominator += pow(2.72, epsilon*Masters/2)
denominator += pow(2.72, epsilon*SomeCollege/2)
denominator += pow(2.72, epsilon*HSGrad/2)
denominator += pow(2.72, epsilon*Bachelors/2)


NPreschool = (pow(2.72, epsilon*Preschool/2))/denominator
Nfirst4th = (pow(2.72, epsilon*first4th/2))/denominator
Nfifth6th = (pow(2.72, epsilon*fifth6th/2))/denominator
Nninth = (pow(2.72, epsilon*ninth/2))/denominator
Ntwelfth = (pow(2.72, epsilon*twelfth/2))/denominator
Nseventh8th = (pow(2.72, epsilon*seventh8th/2))/denominator
Ntenth = (pow(2.72, epsilon*tenth/2))/denominator
Neleventh = (pow(2.72, epsilon*eleventh/2))/denominator
NAssocAcdm = (pow(2.72, epsilon*AssocAcdm/2))/denominator
NDoctorate = (pow(2.72, epsilon*Doctorate/2))/denominator
NAssocVoc = (pow(2.72, epsilon*AssocVoc/2))/denominator
NProfSchool = (pow(2.72, epsilon*ProfSchool/2))/denominator
NMasters = (pow(2.72, epsilon*Masters/2))/denominator
NSomeCollege = (pow(2.72, epsilon*SomeCollege/2))/denominator
NHSGrad = (pow(2.72, epsilon*HSGrad/2))/denominator
NBachelors = (pow(2.72, epsilon*Bachelors/2))/denominator

Nvalues=[NPreschool, Nfirst4th, Nfifth6th, Nninth, Ntwelfth, Nseventh8th, Ntenth, Neleventh,
         NAssocAcdm, NDoctorate, NAssocVoc, NProfSchool, NMasters, NSomeCollege, NHSGrad, NBachelors]
EducationLevels = ['Preschool', '1st-4th', '5th-6th', '9th', '12th', '7th-8th', '10th', '11th',
                   'Assoc-Acdm', 'Doctorate', 'Assoc-Voc', 'Prof School', 'Masters', 'Some College', 'HS-Grad', 'Bachelors']

maxNumber=Nvalues[0]
returnVal=0

for i in range(0,len(Nvalues)):
    if(Nvalues[i]>maxNumber):
        maxNumber=Nvalues[i]
        returnVal=i

print("Most common education level according to Exponential is: "+ EducationLevels[returnVal])