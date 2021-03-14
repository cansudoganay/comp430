import random
import numpy as np

with open('ages.txt') as f:
    lines = [line.rstrip() for line in f]

## epsilon varies
epsilon = 4.0

d = 100 ##since our age values are in between 1 and 100, inclusive
e = 2.72
p = pow(e, epsilon)/(pow(e, epsilon)+d-1)
q = (1-p)/(d-1)

## USER SIDE

ages=[]
for line in lines:
    coin = random.random()
    if(coin <= p):
        ages.append(line)
    else:
        changedAge = random.randint(1, 100)
        ages.append(changedAge)

## SERVER SIDE

E = [0] * 101 #array for ages
n = 100000 #we have 100000 lines in ages.txt

nv = [0] * 101
actualAges = [0] * 101

for i in ages:
    nv[int(i)]=nv[int(i)]+1

for i in lines:
    actualAges[int(i)]=actualAges[int(i)]+1

for v in range(1,101):
    E[v]=(nv[v]*p + (n-nv[v])*q)

## error calculation

error=0

for i in range(1,101):
    error+=abs(actualAges[i]-E[i])

print("For ε = ", epsilon, " Error is: ", error/100)