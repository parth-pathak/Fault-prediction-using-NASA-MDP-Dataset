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
    danger = []
    for i in range(len(minority)):
        x = minority[i][:-1]
        nn = []
        for j in range(len(inst)):
            z = list(inst[j])[:-1]
            dist = math.sqrt(sum([(x[l]-z[l])**2 for l in range(len(x))]))
            if dist != 0:
                nn.append((list(inst[j]), dist))
        knn = sorted(nn, key=second)[:(2*k)]
        new = [a[0] for a in knn]
        m = 0
        for a in new:
            if a[-1]=='N':
                m+=1
        if m>k and m<(2*k):
            danger.append(minority[i])
    for i in range(len(danger)):
        x = danger[i][:-1]
        nn = []
        for j in range(len(danger)):
            if i != j:
                z = danger[j][:-1]
                dist = math.sqrt(sum([(x[l]-z[l])**2 for l in range(len(x))]))
                nn.append((danger[j], dist))
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
