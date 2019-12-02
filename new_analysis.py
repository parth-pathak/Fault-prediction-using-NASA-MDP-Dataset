import os
import arff
import xlwt
import numpy as np
from sklearn import metrics
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def accuracy(clf, X, Y):
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    cm = metrics.confusion_matrix(y_test, y_pred)
    tn = cm[0][0]
    fn = cm[1][0]
    tp = cm[1][1]
    fp = cm[0][1]
    return tp/(tp+fn)

files=[]
data_path = "MDP\\D''\\"
for f in os.listdir(data_path):
    files.append(f)
workbook = xlwt.Workbook()
style = xlwt.easyxf('font: bold 1; align: wrap on,vert centre, horiz center;')
sheet1 = workbook.add_sheet('Sheet 1')
sheet1.write(0, 0, 'Serial No.', style)
sheet1.write(0, 1, 'Dataset', style)
sheet1.write(0, 2, 'Calculation of Dice Similarity coefficient', style)
sheet1.merge(0, 0, 2, 6)
sheet1.merge(0, 2, 0, 0)
sheet1.merge(0, 2, 1, 1)
sheet1.write(1, 2, 'Random Forest', style)
sheet1.write(1, 3, 'k-NN (k=7)', style)
sheet1.write(1, 4, 'AdaBoost', style)
sheet1.write(1, 5, 'Gaussian NB', style)
sheet1.write(1, 6, 'LinearSVC', style)
sheet1.merge(1, 2, 2, 2)
sheet1.merge(1, 2, 3, 3)
sheet1.merge(1, 2, 4, 4)
sheet1.merge(1, 2, 5, 5)
sheet1.merge(1, 2, 6, 6)
for i in range(len(files)):
    f_path = os.path.join(data_path, files[i])
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
    
    print(f_path)
    sheet1.write(i+3, 0, str(i+1))
    sheet1.write(i+3, 1, files[i][:-5])
    clf = RandomForestClassifier(n_estimators = 100, max_depth=2, random_state = 0)
    dsc = accuracy(clf, X, Y)
    sheet1.write(i+3, 2, dsc)
    clf = KNeighborsClassifier(n_neighbors=7)
    dsc = accuracy(clf, X, Y)
    sheet1.write(i+3, 3, dsc)
    clf = AdaBoostClassifier(n_estimators = 100, random_state = 0)
    dsc = accuracy(clf, X, Y)
    sheet1.write(i+3, 4, dsc)
    clf = GaussianNB()
    dsc = accuracy(clf, X, Y)
    sheet1.write(i+3, 5, dsc)
    clf = LinearSVC(random_state=0)
    dsc = accuracy(clf, X, Y)
    sheet1.write(i+3, 6, dsc)
workbook.save("Original\\Specificity.xls")
