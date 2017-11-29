#coding=gbk
from imblearn.under_sampling import RandomUnderSampler

import numpy as np
import re
import os
from LearningText import toArff

# Generate the dataset
class RamUnder:
    def loadSample(self, path):
        file = open(path, 'r')
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
        labels = np.array([int(x) for x in labels])
        file.close()
        return features, labels

    def write_resample(self, path, resampled):
        f = open(path, 'w')
        for i in range(len(resampled)):
            for j in range(len(resampled[i])):
                if j < len(resampled[i]) - 1:
                    f.write(str(resampled[i][j]) + ',')
                else:
                    f.write(str(resampled[i][j]))
            f.write('\n')
        f.close()

    def run_dir(self, path_original, path_saveNew):
        pathdir_original = os.listdir(path_original)  # 列出原始样本文件夹下的文件名和文件夹名
        for name in pathdir_original:  # 对文件名进行循环
            if os.path.isfile(path_original + "\\" + name):  # 如果name是一个文件，这里传入的路径必须是绝对路径才可以判断
                X, y = self.loadSample(path_original + "\\" + name)  # 加载文件数据
                for i in range(m):  # 循环采样，每一次采样结果存放在for_i文件夹下
                    X_resampled, y_resampled = rus.fit_sample(X, y)
                    y_resampled = y_resampled[:, np.newaxis]
                    resampled = np.hstack((X_resampled, y_resampled)).tolist()
                    self.write_resample(path_saveNew + '\\for_' + str(i + 1) + '\\re_ro_' + name, resampled)
            else:  # 如果name是一个文件夹
                path1 = path_original + "\\" + name  # 更新原始数据集路径
                os.mkdir(path_saveNew + "\\" + name)  # 创建和原始数据集文件夹一致的文件夹，用于保存采样的结果
                path2 = path_saveNew + "\\" + name  # 更新保存数据的路径为新创建的文件夹
                for i in range(m):  # 在这个文件夹中创建存放每一次循环采样结果的文件夹
                    os.mkdir(path2 + "\\for_" + str(i + 1))
                self.run_dir(path1, path2)  # 调用循环采样的方法，循环调用


if __name__ == '__main__':
    m = int(input("请输入采样次数："))
    path_originial = "E:\\Papers_dataset\\OriginalDataSet"  # 存放原始数据文件的文件夹
    path_saveNew = "E:\\Papers_dataset\\ResempledDataSet\\RUS"  # 存放新采样过后的文件的文件夹
    ramdomUnder=RamUnder()
    rus = RandomUnderSampler()
    ramdomUnder.run_dir(path_originial, path_saveNew)  # 传入原始数据集文件夹和保存重采样数据集文件夹即可
    toArff.run_dir(path_saveNew,"E:\\Papers_dataset\\ResempledDataSet\\RUS_arff")

# file = open("C:\\Users\\Administrator\\Desktop\\Original_dataset20171121\\SMOTE+TonekLink\\Flag_0_white.csv", 'r')
# '''读取文件的内容，readlines返回的是一个列表'''
# contain = file.readlines()
# count = len(contain)  # 这是文件共有count行
# '''创建一个count x len(contain[0].split(','))-1的矩阵,其中len(contain[0].split(','))-1是样本属性的个数'''
# features = np.zeros((count, len(re.split(r'[ ,;:\t]+', contain[0])) - 1))
# labels = []
# index = 0
# for line in contain:  # 一行行读数据文件
#     line = line.strip()  # 删除line头和尾的空格
#     listFormLine = re.split(r'[ ,;:\t]+', line)  # 指定','为分隔符，将line分割开
#     '''将listFormLine中的前len(len(listFormLine)-1)列加入到矩阵中去'''
#     features[index:] = listFormLine[0:len(listFormLine) - 1]
#     labels.append(listFormLine[-1])  # 最后一列作为类标
#     index += 1
#     '''返回的features为特征矩阵，labels为类别列表'''
# labels=np.array([int(x) for x in labels])
# file.close()
# X=features
# y=labels
# ros = RandomOverSampler()
# X_resampled, y_resampled = ros.fit_sample(X, y)
# y_resampled=y_resampled[:,np.newaxis]
# resampled=np.hstack((X_resampled,y_resampled)).tolist()
# f=open("re_Ran_Over_OCR_0_0.csv",'w')
# for i in range(len(resampled)):
#     for j in range(len(resampled[i])):
#         if j<len(resampled[i])-1:
#             f.write(str(resampled[i][j])+',')
#         else:f.write(str(resampled[i][j]))
#     f.write('\n')
# f.close()