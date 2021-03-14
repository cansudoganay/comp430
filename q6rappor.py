import random
import numpy as np

with open('ages.txt') as f:
    lines = [line.rstrip() for line in f]

## epsilon varies
epsilon = 4.0

e = 2.72
p = pow(e, epsilon/2)/(pow(e, epsilon/2)+1)
q = 1/(pow(e, epsilon/2)+1)

actualAges=[0]*101
for i in lines:
    actualAges[int(i)]=actualAges[int(i)]+1

## USER SIDE
ages=[]

for line in lines:
    v = np.linspace(0, 0, 101)
    v[int(line)] = 1
    for j in range (1,101):
        coin = random.random()
        if(coin > p):
            if(v[int(j)]==0):
                v[int (j)]=1
            elif(v[int (j)]==1):
                v[int (j)]=0
                #print(v, line)
    ages.append(v)

## SERVER SIDE

E=[0]*101
C=[0]*101
n = 100000 ##size of our dataset

for i in range (0,100000):
    for j in range (0,101):
        E[j]+=(ages[i][j])

for i in range (0,101):
    C[i]=(E[i]-n*q)/(p-q)

## error calculation

error=0

for i in range(1,101):
     error+=abs(actualAges[i]-C[i])

print("For ε = ", epsilon, " Error is: ", error/100)
