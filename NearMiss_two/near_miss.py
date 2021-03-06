#coding=gbk
from imblearn.under_sampling import NearMiss

import numpy as np
import re

# Generate the dataset
file = open("E:\PycharmProjects\Learning_Notes\DataSet\Imbalanced Data.txt", 'r')
'''读取文件的内容，readlines返回的是一个列表'''
contain = file.readlines()
count = len(contain)  # 这是文件共有count行
'''创建一个count x len(contain[0].split(','))-1的矩阵,其中len(contain[0].split(','))-1是样本属性的个数'''
features = np.zeros((count, len(re.split(r'[ ,;:\t]+', contain[0])) - 1))
labels = []
index = 0
for line in contain:  # 一行行读数据文件
    line = line.strip()  # 删除line头和尾的空格
    listFormLine = re.split(r'[ ,;:\t]+', line)  # 指定','为分隔符，将line分割开
    '''将listFormLine中的前len(len(listFormLine)-1)列加入到矩阵中去'''
    features[index:] = listFormLine[0:len(listFormLine) - 1]
    labels.append(listFormLine[-1])  # 最后一列作为类标
    index += 1
    '''返回的features为特征矩阵，labels为类别列表'''
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
