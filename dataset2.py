import os
import arff
import xlwt
import math
import numpy as np
files = []
data_path = "MDP\\D-adasyn\\training"
target_path = "MDP\\D-adasyn"
for f in os.listdir(data_path):
    files.append(f)
workbook = xlwt.Workbook()
style = xlwt.easyxf('font: bold 1; align: wrap on,vert centre, horiz center;')
sheet1 = workbook.add_sheet('Sheet 1')
sheet1.write(0, 0, 'Serial No.', style)
sheet1.write(0, 1, 'Dataset', style)
sheet1.write(0, 2, 'No. of Features', style)
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
    inst = list(arff.load(f_path))
    a = np.array(inst)
    size = a.shape
    sheet1.write(i+3, 2, str(size[1]))
    sheet1.write(i+3, 3, str(len(inst)))
    y = 0
    n = 0
    for r in range(len(inst)):
        if list(inst[r])[-1]=='Y':
            y += 1
        if list(inst[r])[-1]=='N':
            n += 1
    sheet1.write(i+3, 5, str(y))
    sheet1.write(i+3, 6, str(n))
    sheet1.write(i+3, 9, str(y/n))
workbook.save(os.path.join(target_path, "Datasets.xls"))
