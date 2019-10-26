import arff
import numpy as np
from sklearn import svm
import os

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
    print('      Training......')
    clf = svm.SVC(kernel='linear')
    clf.fit(x, y)
    print('      Done......')
    correct = 0
    total = 0
    for r in range(t, size[0]):
        x = a[r][:-1]
        y = a[r][-1]
        res = clf.predict([x])
        if res[0]==y:
            correct += 1
        total += 1
    ans = (correct/total)*100
    print('      '+str(ans)+'% accurate prediction')
