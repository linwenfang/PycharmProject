#coding=gbk
from imblearn.ensemble import EasyEnsemble
import numpy as np
import re

file = open("C:\\Users\windows\Desktop\�ĵ�\EasyEnsemble\\Balance_0_B.csv", 'r')
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
# Apply Easy Ensemble
ee = EasyEnsemble(n_subsets=2)
X_resampled, y_resampled = ee.fit_sample(X, y)
for i in range(len(y_resampled)):
    y_resampled1=y_resampled[i][:,np.newaxis]
    resampled1=np.hstack((X_resampled[i],y_resampled1)).tolist()
    f=open("C:\\Users\windows\Desktop\�ĵ�\PycharmProjects\Learning_Notes\EasyEnsemble\EASYENSEMBLE\\re_EasyEnsemble_Balance_0_B_"+str(i)+".csv",'w')
    for i in range(len(resampled1)):
        for j in range(len(resampled1[i])):
            if j<len(resampled1[i])-1:
                f.write(str(resampled1[i][j])+',')
            else:f.write(str(resampled1[i][j]))
        f.write('\n')
    f.close()
