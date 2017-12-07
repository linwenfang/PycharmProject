import matplotlib.pyplot as plt
from skLearn.datasets import make_classification
from skLearn.decomposition import PCA

from imblearn.ensemble import BalanceCascade
import numpy as np
import re

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


# Apply Balance Cascade method
bc = BalanceCascade()
X_resampled, y_resampled = bc.fit_sample(X, y)

for i in range(len(y_resampled)):
    y_resampled1=y_resampled[i][:,np.newaxis]
    resampled1=np.hstack((X_resampled[i],y_resampled1)).tolist()
    f=open("re_balanced_Cascade"+str(i)+".txt",'w')
    for i in range(len(resampled1)):
        for j in range(len(resampled1[i])):
            if j<len(resampled1[i])-1:
                f.write(str(resampled1[i][j])+',')
            else:f.write(str(resampled1[i][j]))
        f.write('\n')
    f.close()

