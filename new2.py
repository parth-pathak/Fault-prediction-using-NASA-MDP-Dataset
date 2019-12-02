import os
import arff
import xlwt
import numpy as np
from sklearn import metrics
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split

def load(data_path, file):
    f_path = os.path.join(data_path, file)
    a = np.array(list(arff.load(f_path)))
    size = a.shape
    
    X = a[:,:-1]
    y = a[:,-1]
    Y = []
    for j in range(len(y)):
        if y[j]=='Y':
            Y.append(1)
        else:
            Y.append(0)
    Y = np.array(Y).astype(np.float64)
    X = np.array(X).astype(np.float64)
    return [X, Y]

def accuracy(X, Y):
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)
    clf = AdaBoostClassifier(n_estimators = 100, random_state = 0)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    cm = metrics.confusion_matrix(y_test, y_pred)
    tn = cm[0][0]
    fn = cm[1][0]
    tp = cm[1][1]
    fp = cm[0][1]
    recall = tp/(tp+fn)
    fm = (5*tp)/((5*tp)+4*fn+fp)
    return [recall, fm]

files=[]
original_path = "MDP\\D''\\"
smote_path = "MDP\\D-smote\\"
bl1_path = "MDP\\D-bl1\\"
bl2_path = "MDP\\D-bl2\\"
cb_path = "MDP\\D-cb\\"
for f in os.listdir(original_path):
    files.append(f)
workbook = xlwt.Workbook()
style = xlwt.easyxf('font: bold 1; align: wrap on,vert centre, horiz center;')
sheet1 = workbook.add_sheet('Sheet 1')
sheet1.write(1, 3, 'Original', style)
sheet1.write(1, 4, 'SMOTE', style)
sheet1.write(1, 5, 'Borderline SMOTE1', style)
sheet1.write(1, 6, 'Borderline SMOTE2', style)
sheet1.write(1, 7, 'Cluster-based SMOTE', style)
for i in range(len(files)):
    original = load(original_path, files[i])
    smote = load(smote_path, files[i])
    bl1 = load(bl1_path, files[i])
    bl2 = load(bl2_path, files[i])
    cb = load(cb_path, files[i])
    print(files[i])
    sheet1.write(i+2, 1, str(i+1))
    sheet1.write(i+2, 2, files[i][:-5])
    ora = accuracy(original[0], original[1])
    sa = accuracy(smote[0], smote[1])
    b1a = accuracy(bl1[0], bl1[1])
    b2a = accuracy(bl2[0], bl2[1])
    ca = accuracy(cb[0], cb[1])
    sheet1.write(i+2, 3, ora[1])
    sheet1.write(i+2, 4, sa[1])
    sheet1.write(i+2, 5, b1a[1])
    sheet1.write(i+2, 6, b2a[1])
    sheet1.write(i+2, 7, ca[1])

workbook.save("FM.xls")
