# import numpy as np
# TP=int(input('TP='))
# FP=int(input('FP='))
# TN=int(input('TN='))
# FN=int(input('FN='))
# Gmeas=np.sqrt((TP/(TP+FP))*(TN/(TN+FN)))
# print(Gmeas)
import os
import re

os.chdir('C:\\Users\windows\Desktop\weka_arff\SMOTE_TomekLink\SMOTE_Tomek')
pathdir_old = os.listdir()
for fileName_old in pathdir_old:
    if fileName_old[-5:] == '.arff':
        continue
    else:
        os.renames(fileName_old, fileName_old[:-4] + '.arff')  # 改文件名
pathdir_new = os.listdir()
for fileName_new in pathdir_new:
    f_r = open(fileName_new, 'r')  # 读取文件
    dataSet = f_r.readlines()
    numAttribute = len(re.split(r'[\s,\t]+', dataSet[0].strip()))  # 属性列的个数
    f_r.close()
    '''读取文件'''
    f_r = open(fileName_new, 'r')
    inData = f_r.readlines()  # 读取文件数据，以列表形式返回
    dataSet = list()  # 用于存储格式化之后的数据
    for line in inData:
        line = line.strip()  # 将line开头和结尾的空行去掉
        strList = re.split(r'[\s,\t]+', line)  # strList为返回的列表,列表中的元素为str类型
        '''将strList中的str类型的元素转换为float类型，方便计算'''
        numList = list()
        for item in strList:
            num = float(item)
            numList.append(num)
        dataSet.append(numList)
    f_r.close()
    '''写入文件'''
    f_w = open(fileName_new, 'w')
    '''arff格式写入'''
    f_w.write('% Title: '+fileName_new+'\n\n')
    f_w.write('@RELATION '+fileName_new+'\n\n')
    for i in range(numAttribute-1):
        f_w.write('@ATTRIBUTE '+str(i+1)+' NUMERIC\n')
    f_w.write('@ATTRIBUTE class {0,1}\n\n')
    f_w.write('@data\n')
    for i in range(len(dataSet)):  # 因为之前在第一行加了12345.。。所以要删去
        if i == -1:
            continue
        else:
            for j in range(len(dataSet[i])):
                if j < len(dataSet[i]) - 1:
                    f_w.write(str(dataSet[i][j]) + ',')
                else:
                    f_w.write(str(int(dataSet[i][j])))
        f_w.write('\n')
    f_w.close()

