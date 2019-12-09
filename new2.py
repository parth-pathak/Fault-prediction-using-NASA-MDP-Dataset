import os
import arff
import xlwt
import numpy as np
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

def plot_roc_curve(ora, sa, b1a, b2a, ca, file):
    plt.plot(ora[3], ora[4], color='orange', label='Original')
    plt.plot(sa[3], sa[4], color='red', label='SMOTE')
    plt.plot(b1a[3], b1a[4], color='green', label='Borderline 1')
    plt.plot(b2a[3], b2a[4], color='violet', label='Borderline 2')
    plt.plot(ca[3], ca[4], color='blue', label='ADASYN')
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Dataset Name: '+file)
    plt.legend()
    plt.show()

def load(data_path, file):
    train_path = os.path.join(data_path+"training", file)
    test_path = os.path.join(data_path+"testing", file)
    train = np.array(list(arff.load(train_path)))
    test = np.array(list(arff.load(test_path)))
    
    X_train = train[:,:-1]
    y_train = train[:,-1]
    Y_train = []
    for j in range(len(y_train)):
        if y_train[j]=='Y':
            Y_train.append(1)
        else:
            Y_train.append(0)
    Y_train = np.array(Y_train).astype(np.float64)
    X_train = np.array(X_train).astype(np.float64)

    X_test = test[:,:-1]
    y_test = test[:,-1]
    Y_test = []
    for j in range(len(y_test)):
        if y_test[j]=='Y':
            Y_test.append(1)
        else:
            Y_test.append(0)
    Y_test = np.array(Y_test).astype(np.float64)
    X_test = np.array(X_test).astype(np.float64)
    return [X_train, X_test, Y_train, Y_test]

def accuracy(X_train, X_test, y_train, y_test):
    clf = LinearSVC(random_state=0)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    cm = metrics.confusion_matrix(y_test, y_pred)
    tn = cm[0][0]
    fn = cm[1][0]
    tp = cm[1][1]
    fp = cm[0][1]
    accuracy = (tp+tn)/(tp+tn+fp+fn)
    fm = (5*tp)/((5*tp)+4*fn+fp)
    tpr = tp/(tp+fn)
    fpr = fp/(fp+tn)
    return [accuracy, fm, auc, fpr, tpr]

files=[]
original_path = "MDP\\D''\\"
smote_path = "MDP\\D-smote\\"
bl1_path = "MDP\\D-bl1\\"
bl2_path = "MDP\\D-bl2\\"
cb_path = "MDP\\D-adasyn\\"
for f in os.listdir(original_path):
    files.append(f)
workbook = xlwt.Workbook()
style = xlwt.easyxf('font: bold 1; align: wrap on,vert centre, horiz center;')
sheet1 = workbook.add_sheet('AUC')
sheet2 = workbook.add_sheet('FM')
sheet3 = workbook.add_sheet('ACC')
sheet1.write(1, 3, 'Original', style)
sheet1.write(1, 4, 'SMOTE', style)
sheet1.write(1, 5, 'Borderline SMOTE1', style)
sheet1.write(1, 6, 'Borderline SMOTE2', style)
sheet1.write(1, 7, 'ADASYN', style)
sheet2.write(1, 3, 'Original', style)
sheet2.write(1, 4, 'SMOTE', style)
sheet2.write(1, 5, 'Borderline SMOTE1', style)
sheet2.write(1, 6, 'Borderline SMOTE2', style)
sheet2.write(1, 7, 'ADASYN', style)
sheet3.write(1, 3, 'Original', style)
sheet3.write(1, 4, 'SMOTE', style)
sheet3.write(1, 5, 'Borderline SMOTE1', style)
sheet3.write(1, 6, 'Borderline SMOTE2', style)
sheet3.write(1, 7, 'ADASYN', style)
for i in range(len(files)):
    f_path = os.path.join(original_path, files[i])
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
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)
    smote = load(smote_path, files[i])
    bl1 = load(bl1_path, files[i])
    bl2 = load(bl2_path, files[i])
    cb = load(cb_path, files[i])
    print(files[i])
    sheet1.write(i+2, 1, str(i+1))
    sheet1.write(i+2, 2, files[i][:-5])
    sheet2.write(i+2, 1, str(i+1))
    sheet2.write(i+2, 2, files[i][:-5])
    sheet3.write(i+2, 1, str(i+1))
    sheet3.write(i+2, 2, files[i][:-5])
    ora = accuracy(X_train, X_test, y_train, y_test)
    sa = accuracy(smote[0], smote[1], smote[2], smote[3])
    b1a = accuracy(bl1[0], bl1[1], bl1[2], bl1[3])
    b2a = accuracy(bl2[0], bl2[1], bl2[2], bl2[3])
    ca = accuracy(cb[0], cb[1], cb[2], cb[3])
    sheet1.write(i+2, 3, ora[2])
    sheet1.write(i+2, 4, sa[2])
    sheet1.write(i+2, 5, b1a[2])
    sheet1.write(i+2, 6, b2a[2])
    sheet1.write(i+2, 7, ca[2])
    sheet2.write(i+2, 3, ora[1])
    sheet2.write(i+2, 4, sa[1])
    sheet2.write(i+2, 5, b1a[1])
    sheet2.write(i+2, 6, b2a[1])
    sheet2.write(i+2, 7, ca[1])
    sheet3.write(i+2, 3, ora[0])
    sheet3.write(i+2, 4, sa[0])
    sheet3.write(i+2, 5, b1a[0])
    sheet3.write(i+2, 6, b2a[0])
    sheet3.write(i+2, 7, ca[0])
    
    plot_roc_curve(ora, sa, b1a, b2a, ca, files[i][:-5])

workbook.save("Sheets\\Linear SVC.xls")
