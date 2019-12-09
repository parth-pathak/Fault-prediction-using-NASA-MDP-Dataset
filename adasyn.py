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
    d = len(minority)//len(majority)
    g = (len(majority)-len(minority))*1
    synthetic = []
    ri = []
    k = 5
    xzi = []
    for i in range(len(minority)):
        x = minority[i][:-1]
        nn = []
        for j in range(len(inst)):
            z = list(inst[j])[:-1]
            dist = math.sqrt(sum([(x[l]-z[l])**2 for l in range(len(x))]))
            if dist != 0:
                nn.append((list(inst[j]), dist))
        knn = sorted(nn, key=second)[:k]
        new = [a[0] for a in knn]
        xz = new[0]
        for a in new:
            if a[-1]=='Y':
                xz = a
        xzi.append(xz)
        m = 0
        for a in new:
            if a[-1]=='N':
                m+=1
        ri.append(m/k)
    rx = [r/sum(ri) for r in ri]
    gi = [g*r for r in rx]
    for i in range(len(minority)):
        x = minority[i][:-1]
        xz = xzi[i][:-1]
        r = random.random()
        while r==0 or r==1:
            r = random.random()
        dist = math.sqrt(sum([(x[l]-xz[l])**2 for l in range(len(x))]))
        temp = [(x[l]+dist*r) for l in range(len(x))]
        temp.append(minority[i][-1])
        synthetic.append(temp)
    for i in synthetic:
        inst.append(i)
    return inst
