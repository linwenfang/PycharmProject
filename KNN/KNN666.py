import numpy as np
from numpy import *
import math
import operator
from collections import Counter
import re
import matplotlib.pyplot as plt

''''读取文件内容'''


def fileMat(filename):
    file = open(filename, 'r')
    '''读取文件的内容，readlines返回的是一个列表'''
    contain = file.readlines()
    count = len(contain)  # 这是文件共有count行
    '''创建一个count x len(contain[0].split(','))-1的矩阵,其中len(contain[0].split(','))-1是样本属性的个数'''
    features = zeros((count, len(re.split(r'[ ,;:\t]+',contain[0])) - 1))
    labels = []
    index = 0
    for line in contain:  # 一行行读数据文件
        line = line.strip()  # 删除line头和尾的空格
        listFormLine = re.split(r'[ ,;:\t]+',line)  # 指定','为分隔符，将line分割开
        '''将listFormLine中的前len(len(listFormLine)-1)列加入到矩阵中去'''
        features[index:] = listFormLine[0:len(listFormLine) - 1]
        labels.append(listFormLine[-1])  # 最后一列作为类标
        index += 1
        '''返回的features为特征矩阵，labels为类别列表'''
    return features, labels


'''计算欧式距离dist = numpy.sqrt(numpy.sum(numpy.square(vec1 - vec2)))
    并排序，并分割前k个欧氏距离、排序、计算类别比例'''


def OushiDistance(trainingSet, trainingLabelSet, testInstance):
    dist = []
    labels = []
    k = 0
    for i in range(len(trainingSet)):
        '''欧式距离的计算公式'''
        distance = np.sqrt(np.sum(np.square(testInstance - trainingSet[i])))
        dist.append(distance)
        k += 1
    '''训练样本数的平方根作为k'''
    k = int(math.sqrt(k))
    '''从小到大排序后的欧氏距离的前k个下标'''
    sortIndex = np.argsort(dist)#把下标按距离远近排序
    sortIndex = sortIndex[0:k]
    '''统计训练标记的比例'''
    for i in sortIndex:
        '''取欧氏距离最小的k个值的类别'''
        labels.append(trainingLabelSet[i])
    '''统计labels中的元素的出现次数'''
    countLabels = dict(Counter(labels))
    '''按字典的value进行从大到小排序'''
    dict1 = sorted(countLabels.items(), key=lambda x: x[1], reverse=True)
    '''返回出现次数最多的'''
    return dict1[0][0]


def showSelecting(trainingLabelSet, trainingSet):
    testDict = dict()
    testDict[1] = list()
    testDict[2] = list()
    for j in range(len(trainingLabelSet)):
        if trainingLabelSet[j] == '1':
            testDict[1].append(trainingSet[j])
        elif trainingLabelSet[j] == '2':
            testDict[2].append(trainingSet[j])
    colorMark = ['or', 'ok', 'og', 'oy', 'ob']  # 不同簇类的标记 'or' --> 'o'代表圆，'r'代表red，'b':blue
    for key in testDict.keys():

        for item in testDict[key]:
            plt.plot(item[0], item[1], colorMark[key])  # 画簇类下的点

    plt.show()


def testing():
    '''读取测试文件，和训练文件'''

    trainingSet, trainingLabelSet = fileMat('TrainingData1.txt')
    testSet, testLabelSet = fileMat('TestData1.txt')
    # fullSet,fullLabelSet=fileMat('full.txt')
    testLabels = []

    n = 0
    m = 0
    for i in range(len(testSet)):
        classify = OushiDistance(trainingSet, trainingLabelSet, testSet[i])
        testLabels.append(classify)
        n += 1
    for i in range(len(testLabels)):
        print(testSet[i], "------>>", testLabels[i], "------>>", testLabelSet[i])
        if testLabelSet[i] == testLabels[i]:
            m += 1
    print("准确率为：", float(m / n))
    showSelecting(trainingLabelSet,trainingSet)
    # showSelecting(fullLabelSet,fullSet)


if __name__ == '__main__':
    print(testing())
