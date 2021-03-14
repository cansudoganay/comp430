import csv
import pandas as pd
import numpy as np

##clean the adult csv
f=pd.read_csv('adult.csv')
f=f[(f !='?').all(axis=1)]
f.to_csv("cleanadult.csv", index=False)


## q(D) values
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


## Lap(0, S(q)/epsilon)

## epsilon varies
epsilon = 0.001


randomSample1 = np.random.laplace(0, 1/epsilon)
randomSample2 = np.random.laplace(0, 1/epsilon)
randomSample3 = np.random.laplace(0, 1/epsilon)
randomSample4 = np.random.laplace(0, 1/epsilon)
randomSample5 = np.random.laplace(0, 1/epsilon)
randomSample6 = np.random.laplace(0, 1/epsilon)
randomSample7 = np.random.laplace(0, 1/epsilon)
randomSample8 = np.random.laplace(0, 1/epsilon)
randomSample9 = np.random.laplace(0, 1/epsilon)
randomSample10 = np.random.laplace(0, 1/epsilon)
randomSample11 = np.random.laplace(0, 1/epsilon)
randomSample12 = np.random.laplace(0, 1/epsilon)
randomSample13 = np.random.laplace(0, 1/epsilon)
randomSample14 = np.random.laplace(0, 1/epsilon)
randomSample15 = np.random.laplace(0, 1/epsilon)
randomSample16 = np.random.laplace(0, 1/epsilon)

# q(D')=q(D)+r
NPreschool = Preschool+randomSample1
Nfirst4th = first4th+randomSample2
Nfifth6th = fifth6th+randomSample3
Nninth = ninth+randomSample4
Ntwelfth = twelfth+randomSample5
Nseventh8th = seventh8th+randomSample6
Ntenth = tenth+randomSample7
Neleventh = eleventh+randomSample8
NAssocAcdm = AssocAcdm+randomSample9
NDoctorate = Doctorate+randomSample10
NAssocVoc = AssocVoc+randomSample11
NProfSchool = ProfSchool+randomSample12
NMasters = Masters+randomSample13
NSomeCollege = SomeCollege+randomSample14
NHSGrad = HSGrad+randomSample15
NBachelors = Bachelors+randomSample16

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

print("Most common education level according to Laplace is: "+ EducationLevels[returnVal])