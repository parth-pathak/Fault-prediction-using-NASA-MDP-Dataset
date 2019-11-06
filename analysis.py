import os
import arff
import xlwt
import numpy as np
from knn import KNNclassifier
files = []
data_path = "MDP\\D''\\"
for f in os.listdir(data_path):
    files.append(f)
workbook = xlwt.Workbook()
style = xlwt.easyxf('font: bold 1; align: horiz center')
sheet1 = workbook.add_sheet('Sheet 1')
sheet1.write(0, 0, 'Serial No.', style)
sheet1.write(0, 1, 'Dataset', style)
sheet1.write(0, 2, 'Algo 1\n(SVM)\nAccuracy', style)
sheet1.write(0, 3, 'Algo 2\n(KNN)', style)
sheet1.merge(0, 1, 3, 3)
sheet1.merge(0, 1, 4, 4)
sheet1.merge(0, 0, 3, 4)
sheet1.merge(0, 2, 0, 0)
sheet1.merge(0, 2, 1, 1)
sheet1.merge(0, 2, 2, 2)
sheet1.write(2, 3, 'Accuracy', style)
sheet1.write(2, 4, 'Smallest k', style)
sheet1.write(0, 5, 'Algo 3\n(RF)\nAccuracy', style)
sheet1.merge(0, 2, 5, 5)
for i in range(len(files)):
    sheet1.write(i+3, 0, str(i+1))
    sheet1.write(i+3, 1, files[i][:-5])
    knn = KNNclassifier(files[i])
    sheet1.write(i+3, 3, str(knn[0]))
    sheet1.write(i+3, 4, str(knn[1]))
workbook.save("Analysis.xls")
