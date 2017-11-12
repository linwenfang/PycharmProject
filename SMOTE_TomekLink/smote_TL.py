
from imblearn.combine import SMOTETomek
import numpy as np
import re

file = open("C:\\Users\windows\Desktop\文档\MWSMOTE\\OCR_0_0.csv", 'r')
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
# Apply SMOTE + Tomek links
sm = SMOTETomek()
X_resampled, y_resampled = sm.fit_sample(X, y)
y_resampled=y_resampled[:,np.newaxis]
resampled=np.hstack((X_resampled,y_resampled)).tolist()
f=open("C:\\Users\windows\Desktop\文档\PycharmProjects\Learning_Notes\SMOTE_TomekLink\MWSMOTE\\re_SMOTE_TL_OCR_0_0.csv",'w')
for i in range(len(resampled)):
    for j in range(len(resampled[i])):
        if j<len(resampled[i])-1:
            f.write(str(resampled[i][j])+',')
        else:f.write(str(resampled[i][j]))
    f.write('\n')
f.close()
