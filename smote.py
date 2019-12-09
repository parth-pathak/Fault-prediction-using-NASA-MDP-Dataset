import math
import numpy as np
import random
def second(a):
    return a[1]
def apply(inst):
    majority = []
    minority = []
    for i in inst:
        i = list(i)
        if i[-1]=='N':
            majority.append(i)
        else:
            minority.append(i)
    k = len(majority)//len(minority)
    synthetic = []
    for i in range(len(minority)):
        x = minority[i][:-1]
        nn = []
        for j in range(len(minority)):
            if i != j:
                z = minority[j][:-1]
                dist = math.sqrt(sum([(x[l]-z[l])**2 for l in range(len(x))]))
                nn.append((minority[j], dist))
        knn = sorted(nn, key=second)[:k]
        new = [a[0] for a in knn]
        r = random.random()
        while r==0 or r==1:
            r = random.random()
        for j in range(len(new)):
            temp = [x[l]+r*abs(x[l]-new[j][l]) for l in range(len(new[j])-1)]
            temp.append(new[j][-1])
            synthetic.append(temp)
    for i in synthetic:
        inst.append(i)
    return inst
