import os
import arff
import xlwt
import numpy as np
from sklearn.model_selection import train_test_split
files = []
data_path = "MDP\\D''\\"
for f in os.listdir(data_path):
    files.append(f)
workbook = xlwt.Workbook()
style = xlwt.easyxf('font: bold 1; align: horiz center')
sheet1 = workbook.add_sheet('Sheet 1')
sheet1.write(0, 0, 'Serial No.', style)
sheet1.write(0, 1, 'Dataset', style)
sheet1.write(0, 2, '#Features', style)
sheet1.write(0, 3, 'No. of Instances', style)
sheet1.merge(0, 0, 3, 4)
sheet1.write(0, 5, 'No. of Classes', style)
sheet1.merge(0, 0, 5, 8)
sheet1.merge(0, 2, 0, 0)
sheet1.merge(0, 2, 1, 1)
sheet1.merge(0, 2, 2, 2)
sheet1.write(1, 3, 'Training', style)
sheet1.write(1, 4, 'Testing', style)
sheet1.write(1, 5, 'Training', style)
sheet1.merge(1, 1, 5, 6)
sheet1.write(1, 7, 'Testing', style)
sheet1.merge(1, 1, 7, 8)
sheet1.merge(1, 2, 3, 3)
sheet1.merge(1, 2, 4, 4)
sheet1.write(2, 5, 'Y', style)
sheet1.write(2, 6, 'N', style)
sheet1.write(2, 7, 'Y', style)
sheet1.write(2, 8, 'N', style)
for i in range(len(files)):
    sheet1.write(i+3, 0, str(i+1))
    sheet1.write(i+3, 1, files[i][:-5])
    f_path = os.path.join(data_path, files[i])
    a = np.array(list(arff.load(f_path)))
    size = a.shape
    sheet1.write(i+3, 2, str(size[1]))
    X = a[:,:-1]
    y = a[:,-1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
    sheet1.write(i+3, 3, str(len(X_train)))
    sheet1.write(i+3, 4, str(len(X_test)))
    y = 0
    n = 0
    for r in range(len(y_train)):
        if y_train[r]=='Y':
            y += 1
        if y_train[r]=='N':
            n += 1
    sheet1.write(i+3, 5, str(y))
    sheet1.write(i+3, 6, str(n))
    y = 0
    n = 0
    for r in range(len(y_test)):
        if y_test[r]=='Y':
            y += 1
        if y_test[r]=='N':
            n += 1
    sheet1.write(i+3, 7, str(y))
    sheet1.write(i+3, 8, str(n))
workbook.save("Datasets.xls")
