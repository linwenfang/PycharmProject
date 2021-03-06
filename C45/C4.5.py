# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:28:53 2017

@author: Administrator
"""

from math import log
import operator
import numpy as np


def calcShannonEnt(dataSet):
    """
    输入：数据集
    输出：数据集的香农熵
    描述：计算给定数据集的香农熵；熵越大，数据集的混乱程度越大
    """
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


def splitDataSet(dataSet, axis, value):
    """
    输入：数据集，选择维度，选择值
    输出：划分数据集
    描述：按照给定特征划分数据集；去除选择维度中等于选择值的项
    """
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    """
    输入：数据集
    输出：最好的划分维度
    描述：选择最好的数据集划分维度
    """
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGainRatio = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        splitInfo = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
            splitInfo += -prob * log(prob, 2)
        infoGain = baseEntropy - newEntropy
        if (splitInfo == 0):  # fix the overflow bug
            continue
        infoGainRatio = infoGain / splitInfo
        if (infoGainRatio > bestInfoGainRatio):
            bestInfoGainRatio = infoGainRatio
            bestFeature = i
    return bestFeature


def majorityCnt(classList):
    """
    输入：分类类别列表
    输出：子节点的分类
    描述：数据集已经处理了所有属性，但是类标签依然不是唯一的，
          采用多数判决的方法决定该子节点的分类
    """
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reversed=True)
    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    """
    输入：数据集，特征标签
    输出：决策树
    描述：递归构建决策树，利用上述的函数
    """
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        # 类别完全相同，停止划分
        return classList[0]
    if len(dataSet[0]) == 1:
        # 遍历完所有特征时返回出现次数最多的
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del (labels[bestFeat])
    # 得到列表包括节点所有的属性值
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


classLabel = list()


def classify(inputTree, featLabels, testVec):
    """
    输入：决策树，分类标签，测试数据
    输出：决策结果
    描述：跑决策树
    """
    # classLabel = []
    global classLabel  # http://blog.csdn.net/liangyuannao/article/details/8704322在此处可以找到出错
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():

        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':

                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel


def classifyAll(inputTree, featLabels, testDataSet):
    """
    输入：决策树，分类标签，测试数据集
    输出：决策结果
    描述：跑决策树
    """

    classLabelAll = []
    for testVec in testDataSet:
        classLabelAll.append(classify(inputTree, featLabels, testVec))
    return classLabelAll


def storeTree(inputTree, filename):
    """
    输入：决策树，保存文件路径
    输出：
    描述：保存决策树到文件
    """
    import pickle
    fw = open(filename, 'wb')
    pickle.dump(inputTree, fw)
    fw.close()


def grabTree(filename):
    """
    输入：文件路径名
    输出：决策树
    描述：从文件读取决策树
    """
    import pickle
    fr = open(filename, 'rb')
    return pickle.load(fr)


# def createDataSet():
#    """
#    outlook->  0: sunny | 1: overcast | 2: rain
#    temperature-> 0: hot | 1: mild | 2: cool
#    humidity-> 0: high | 1: normal
#    windy-> 0: false | 1: true
#    """
#    dataSet = [[0, 0, 0, 0, 3.0],
#               [0, 0, 0, 1, 3.0],
#               [1, 0, 0, 0, 4.0],
#               [2, 1, 0, 0, 4.0],
#               [2, 2, 1, 0, 4.0],
#               [2, 2, 1, 1, 3.0],
#               [1, 2, 1, 1, 4.0]]
#    #labels = [dataSet[0][i] for i in range(len(dataSet[0])-1)]
#
#    features = ['outlook', 'temperature', 'humidity', 'windy']
#    return dataSet, features

def createDataSet():
    path = r'C:\Users\Administrator\Desktop\re_smotetl\EasyEnsemble\for_1\re_SMOTE_Tomek_abalone_0_7.csv'
    dataSet = np.loadtxt(path, delimiter=',')
    dataSet = dataSet.tolist()
    features = [dataSet[0][i] for i in range(len(dataSet[0]) - 1)]
    # features = ['1','2','3','4','5','6','7','8','9']
    return dataSet, features


# def createTestSet():
#    label = []
#    path = r'E:\work\test.txt'
#    testSet = np.loadtxt(path,delimiter=',')
#    testSet = testSet.tolist()
#    for j in range(len(testSet)):
#        label.append(testSet[j][-1])
#    print("<------------------->")
#    print(label)
#    print("<------------------->")
#    for i in range(len(testSet)):
#        testSet[i] = testSet[i][:-1]
#    return testSet,label

def createTestSet():
    path = r'C:\Users\Administrator\Desktop\re_smotetl\EasyEnsemble\for_1\re_SMOTE_Tomek_abalone_0_7.csv'
    testSet = np.loadtxt(path, delimiter=',')
    testSet = testSet.tolist()
    return testSet


# def createTestSet():
#    """
#    outlook->  0: sunny | 1: overcast | 2: rain
#    temperature-> 0: hot | 1: mild | 2: cool
#    humidity-> 0: high | 1: normal
#    windy-> 0: false | 1: true
#    """
#    testSet = [[0, 1, 0, 0],
#               [0, 2, 1, 0],
#               [2, 1, 1, 0],
#               [0, 1, 1, 1],
#               [1, 1, 0, 1],
#               [1, 0, 1, 0],
#               [2, 1, 0, 1],
#               [1, 2, 1, 0]]
#    return testSet

def main():
    correct = 0

    dataSet, features = createDataSet()
    # print(labels)
    labels_tmp = features[:]  # 拷贝，createTree会改变features
    # print(labels_tmp)
    desicionTree = createTree(dataSet, labels_tmp)
    # storeTree(desicionTree, 'classifierStorage.txt')
    # desicionTree = grabTree('classifierStorage.txt')
    print('desicionTree:\n', desicionTree)
    # treePlotter.createPlot(desicionTree)
    testSet = createTestSet()
    testSet1 = testSet[:-1]  # testSet1是testSet的去除类标后的属性列
    #    print("****************************")
    #    print(label)
    #    print("****************************")
    n = len(testSet)
    print("测试样本个数：", n)
    for test_data in testSet:
        clabel = classify(desicionTree, features, test_data)
        if clabel == test_data[-1]:
            correct += 1
    print("正确分类个数：", correct)
    print("准确率：", correct / float(n))
    #    for test_data in testSet:
    #        classifyLabel = classifyAll(desicionTree, features, testSet)
    #        if classifyLabel == label:
    #            correct += 1
    #    print("准确率：",correct/float(n))
    print('classifyResult:\n', classifyAll(desicionTree, features, testSet1))


# for test_data in test_dataset:
#            label = self.classify(decesion_tree,test_features,test_data,mean_values)
#            print ('classify_label  correct_label:',label,test_data[-1])
#            if label == test_data[-1]:
#                correct += 1
#        print ("准确率: ",correct/float(n))


if __name__ == '__main__':
    main()