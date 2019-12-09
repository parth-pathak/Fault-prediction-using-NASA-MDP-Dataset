import os
import arff
import math
import smote
import borderline1
import borderline
import adasyn
import numpy as np
files = []
data_path = "MDP\\D''\\"
for f in os.listdir(data_path):
    files.append(f)
for f in range(len(files)):
    print(f, end="...")
    f_path = os.path.join(data_path, files[f])
    inst = list(arff.load(f_path))
    a = np.array(inst)
    size = a.shape
    t = math.ceil(0.8*size[0])

    print('Smote, ')
    res = smote.apply(inst[:t])
    path = os.path.join("MDP\\D-smote\\training", files[f])
    arff.dump(path, res, relation=files[f][:-5])
    path = os.path.join("MDP\\D-smote\\testing", files[f])
    arff.dump(path, inst[t:], relation=files[f][:-5])

    print('Borderline1, ')
    res = borderline1.apply(inst[:t])
    path = os.path.join("MDP\\D-bl1\\training", files[f])
    arff.dump(path, res, relation=files[f][:-5])
    path = os.path.join("MDP\\D-bl1\\testing", files[f])
    arff.dump(path, inst[t:], relation=files[f][:-5])

    print('Borderline2, ')
    res = borderline.apply(inst[:t])
    path = os.path.join("MDP\\D-bl2\\training", files[f])
    arff.dump(path, res, relation=files[f][:-5])
    path = os.path.join("MDP\\D-bl2\\testing", files[f])
    arff.dump(path, inst[t:], relation=files[f][:-5])

    print('Adasyn')
    res = adasyn.apply(inst[:t])
    path = os.path.join("MDP\\D-adasyn\\training", files[f])
    arff.dump(path, res, relation=files[f][:-5])
    path = os.path.join("MDP\\D-adasyn\\testing", files[f])
    arff.dump(path, inst[t:], relation=files[f][:-5])
    
    print('...done')
