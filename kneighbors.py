import arff
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import os
from sklearn.model_selection import train_test_split

files = []
data_path = "MDP\\D''\\"
for f in os.listdir(data_path):
    f_path = os.path.join(data_path, f)
    files.append(f_path)

for f in files:
    print(f)
    a = np.array(list(arff.load(f)))
    size = a.shape
    t = int(0.8 * size[0])
    x = a[:t, :-1]
    y = a[:t, -1]
    for g in range(len(y)):
        if y[g]=='Y':
            y[g] = 1.0
        else:
            y[g] = 0.0
    print('      Training......')
    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(x, y)
    print('      Done......')
    correct = 0
    total = 0
    for r in range(t, size[0]):
        x = a[r][:-1]
        y = a[r][-1]
        if y=='Y':
            y = 1.0
        else:
            y = 0.0
        res = clf.predict([x])
        if res[0]==y:
            correct += 1
        total += 1
    ans = (correct/total)*100
    print('      '+str(ans)+'% accurate prediction')
