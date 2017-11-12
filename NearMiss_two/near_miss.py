#coding=gbk
from imblearn.under_sampling import NearMiss

import numpy as np
import re

# Generate the dataset
file = open("E:\PycharmProjects\Learning_Notes\DataSet\Imbalanced Data.txt", 'r')
'''��ȡ�ļ������ݣ�readlines���ص���һ���б�'''
contain = file.readlines()
count = len(contain)  # �����ļ�����count��
'''����һ��count x len(contain[0].split(','))-1�ľ���,����len(contain[0].split(','))-1���������Եĸ���'''
features = np.zeros((count, len(re.split(r'[ ,;:\t]+', contain[0])) - 1))
labels = []
index = 0
for line in contain:  # һ���ж������ļ�
    line = line.strip()  # ɾ��lineͷ��β�Ŀո�
    listFormLine = re.split(r'[ ,;:\t]+', line)  # ָ��','Ϊ�ָ�������line�ָ
    '''��listFormLine�е�ǰlen(len(listFormLine)-1)�м��뵽������ȥ'''
    features[index:] = listFormLine[0:len(listFormLine) - 1]
    labels.append(listFormLine[-1])  # ���һ����Ϊ���
    index += 1
    '''���ص�featuresΪ��������labelsΪ����б�'''
labels=np.array([int(x) for x in labels])
file.close()
X=features
y=labels
# Apply Nearmiss
nm=NearMiss(version=2)
X_resampled = []
y_resampled = []
X_res,y_res=nm.fit_sample(X,y)
X_resampled.append(X_res)
y_resampled.append(y_res)
y_resampled=y_resampled[0]
X_resampled=X_resampled[0]
y_resampled=y_resampled[:,np.newaxis]

resampled=np.hstack((X_resampled,y_resampled)).tolist()
f=open("re_NearMiss2.csv",'w')
for i in range(len(resampled)):
    for j in range(len(resampled[i])):
        if j<len(resampled[i])-1:
            f.write(str(resampled[i][j])+',')
        else:f.write(str(resampled[i][j]))
    f.write('\n')
f.close()

# Two subplots, unpack the axes array immediately
