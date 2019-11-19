import os
import arff
import numpy as np
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

data_path = "MDP\\D''\\"
f = os.path.join(data_path, "JM1.arff")

a = np.array(list(arff.load(f)))
size = a.shape

X = a[:,:-1]
y = a[:,-1]
Y = []
for i in range(len(y)):
    if y[i]=='Y':
        Y.append(1)
    else:
        Y.append(0)
Y = np.array(Y).astype(np.float64)
X = np.array(X).astype(np.float64)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

print("Gaussian Naive Bayes...", end="")
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))

print("Random Forest...", end="")
clf = RandomForestClassifier(n_estimators = 100, max_depth=2, random_state = 0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))

print("AdaBoost...", end="")
clf = AdaBoostClassifier(n_estimators = 100, random_state = 0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))

print("K Nearest Neighbors...", end="")
clf = KNeighborsClassifier(n_neighbors=7)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))

print("SVM...", end="")
clf = SVC(kernel='linear')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))
