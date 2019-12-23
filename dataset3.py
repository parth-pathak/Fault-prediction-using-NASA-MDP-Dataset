import os
import arff
import xlwt
import math
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

files = []
data_path = "MDP\\D''\\"
for f in os.listdir(data_path):
    files.append(f)
for i in range(len(files)):
    f_path = os.path.join(data_path, files[i])
    a = np.array(list(arff.load(f_path)))
    size = a.shape
    t = math.ceil(0.8*size[0])
    X = a[:t,:-1]
    y = a[:t,-1]
    X_embedded = TSNE(perplexity=10, n_components=3).fit_transform(X)
    x_axis1 = []
    y_axis2 = []
    z_axis1 = []
    z_axis2 = []
    x_axis2 = []
    y_axis1 = []
    for j in range(t):
        if y[j]=='Y':
            x_axis2.append(X_embedded[j][0])
            y_axis2.append(X_embedded[j][1])
            z_axis2.append(X_embedded[j][2])
        if y[j]=='N':
            x_axis1.append(X_embedded[j][0])
            y_axis1.append(X_embedded[j][1])
            z_axis1.append(X_embedded[j][2])
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.plot3D(x_axis1, y_axis1, z_axis1, 'ro', color='orange', label='Not Defective')
    ax.plot3D(x_axis2, y_axis2, z_axis2, 'ro', color='Indigo', label='Defective')
    plt.legend()
    plt.show()
