import arff
import os
import math
import numpy as np

def dist(t):
    return t[1]
def distance(x, y):
    s = 0
    for i in range(len(x)):
        s += math.pow(float(x[i])-float(y[i]), 2)
    return math.sqrt(s)
def update(cl, d, neighbors, k):
    i = 0
    while i<len(neighbors)and neighbors[i][1]<d:
        i += 1
    if len(neighbors)<k:
        if i<len(neighbors):
            neighbors.insert(i, (cl, d))
        else:
            neighbors.append((cl, d))
    else:
        if i<k:
            neighbors.insert(i, (cl, d))
            neighbors = neighbors[:-1]
    return neighbors
def findMax(neighbors):
    d = {}
    for i in neighbors:
        if i[0] not in d:
            d[i[0]] = 1
        else:
            d[i[0]] += 1
    m = -1
    res = ""
    for key in d.keys():
        if d[key]>m:
            m = d[key]
            res = key
    return res
def classify(item, k):
    global items
    if k>len(items):
        k = len(items)
    neighbors = []
    for i in items:
        d = distance(i[:-1], item)
        neighbors = update(i[-1], d, neighbors, k)
    return findMax(neighbors)
def KNNclassifier(f):
    data_path = "MDP\\D''\\"
    f_path = os.path.join(data_path, f)
    a = np.array(list(arff.load(f_path)))
    size = a.shape
    t = int(0.8 * size[0])
    items = a[:t]
    acc = 0
    low = 1
    high = t-1
    k = 1
    while(low < high):
        mid = (low+high)//2
        correct = 0
        total = 0
        for i in range(t, size[0]):
            item = a[i][:-1]
            cl = a[i][-1]
            res = classify(item, low)
            if res==cl:
                correct+=1
            total+=1
        ansl = (correct/total)*100
        correct = 0
        total = 0
        for i in range(t, size[0]):
            item = a[i][:-1]
            cl = a[i][-1]
            res = classify(item, high)
            if res==cl:
                correct+=1
            total+=1
        ansh = (correct/total)*100
        correct = 0
        total = 0
        for i in range(t, size[0]):
            item = a[i][:-1]
            cl = a[i][-1]
            res = classify(item, mid)
            if res==cl:
                correct+=1
            total+=1
        ansm = (correct/total)*100
        if low==mid:
            if ansm<ansh:
                acc = ansh
                k = high
            else:
                acc = ansm
                k = mid
            break
        if ansl<=ansm:
            if ansm<ansh:
                low = mid
            else:
                high = mid
        else:
            if ansm>=ansh:
                high = mid
            else:
                if ansl<ansh:
                    low = mid
                else:
                    high = mid
    return (acc, k)
