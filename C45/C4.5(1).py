# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 09:17:12 2017

@author: Administrator
"""

from math import log
import operator
import numpy as np
import os
from sklearn.cross_validation import train_test_split


class C45():
    def calcShannonEnt(self,dataSet):
#        """
#    输入：数据集
#    输出：数据集的香农熵
#    描述：计算给定数据集的香农熵；熵越大，数据集的混乱程度越大
#    """
        numEntries = len(dataSet)
        labelCounts = {}
        for featVec in dataSet:
            currentLabel = featVec[-1]
            if currentLabel not in labelCounts.keys():
                labelCounts[currentLabel] = 0
            labelCounts[currentLabel] += 1
        shannonEnt = 0.0
        for key in labelCounts:
            prob = float(labelCounts[key])/numEntries
            shannonEnt -= prob * log(prob, 2)
        return shannonEnt
    
    def splitDataSet(self,dataSet, axis, value):
#        """
#    输入：数据集，选择维度，选择值
#    输出：划分数据集
#    描述：按照给定特征划分数据集；去除选择维度中等于选择值的项
#    """
        retDataSet = []
        for featVec in dataSet:
            if featVec[axis] == value:
                reduceFeatVec = featVec[:axis]
                reduceFeatVec.extend(featVec[axis+1:])
                retDataSet.append(reduceFeatVec)
        return retDataSet
    
    def chooseBestFeatureToSplit(self,dataSet):
#        """
#    输入：数据集
#    输出：最好的划分维度
#    描述：选择最好的数据集划分维度
#    """
        numFeatures = len(dataSet[0]) - 1
        baseEntropy = c45.calcShannonEnt(dataSet)
        bestInfoGainRatio = 0.0
        bestFeature = -1
        for i in range(numFeatures):
            featList = [example[i] for example in dataSet]
            uniqueVals = set(featList)
            newEntropy = 0.0
            splitInfo = 0.0
            for value in uniqueVals:
                subDataSet = c45.splitDataSet(dataSet, i, value)
                prob = len(subDataSet)/float(len(dataSet))
                newEntropy += prob * c45.calcShannonEnt(subDataSet)
                splitInfo += -prob * log(prob, 2)
            infoGain = baseEntropy - newEntropy
            if (splitInfo == 0): # fix the overflow bug
                continue
            infoGainRatio = infoGain / splitInfo
            if (infoGainRatio > bestInfoGainRatio):
                bestInfoGainRatio = infoGainRatio
                bestFeature = i
        return bestFeature
    
    def majorityCnt(self,classList):
#        """
#    输入：分类类别列表
#    输出：子节点的分类
#    描述：数据集已经处理了所有属性，但是类标签依然不是唯一的，
#          采用多数判决的方法决定该子节点的分类
#    """
        classCount = {}
        for vote in classList:
            if vote not in classCount.keys():
                classCount[vote] = 0
            classCount[vote] += 1
        sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reversed=True)
        return sortedClassCount[0][0]
    
    def createTree(self,dataSet, labels):
#        """
#    输入：数据集，特征标签
#    输出：决策树
#    描述：递归构建决策树，利用上述的函数
#    """
        classList = [example[-1] for example in dataSet]
        if classList.count(classList[0]) == len(classList):
            # 类别完全相同，停止划分
            return classList[0]
        if len(dataSet[0]) == 1:
            # 遍历完所有特征时返回出现次数最多的
            return c45.majorityCnt(classList)
        bestFeat = c45.chooseBestFeatureToSplit(dataSet)
        bestFeatLabel = labels[bestFeat]
        myTree = {bestFeatLabel:{}}
        del(labels[bestFeat])
        # 得到列表包括节点所有的属性值
        featValues = [example[bestFeat] for example in dataSet]
        uniqueVals = set(featValues)
        for value in uniqueVals:
            subLabels = labels[:]
            myTree[bestFeatLabel][value] = c45.createTree(c45.splitDataSet(dataSet, bestFeat, value), subLabels)
        return myTree
    
#    classLabel = list()
    def classify(self,inputTree, featLabels, testVec):
#        """
#    输入：决策树，分类标签，测试数据
#    输出：决策结果
#    描述：跑决策树
#    """
        #classLabel = []
        global classLabel  #http://blog.csdn.net/liangyuannao/article/details/8704322在此处可以找到出错
        firstStr = list(inputTree.keys())[0]
        secondDict = inputTree[firstStr]
        featIndex = featLabels.index(firstStr)
        for key in secondDict.keys():
            if testVec[featIndex] == key:
                if type(secondDict[key]).__name__ == 'dict':
                    classLabel = c45.classify(secondDict[key], featLabels, testVec)
                else:
                    classLabel = secondDict[key]
        return classLabel
    
    def classifyAll(self,inputTree, featLabels, testDataSet):
#        """
#    输入：决策树，分类标签，测试数据集
#    输出：决策结果
#    描述：跑决策树
#    """
        classLabelAll = []
        for testVec in testDataSet:
            classLabelAll.append(c45.classify(inputTree, featLabels, testVec))
        return classLabelAll
    
    def storeTree(self,inputTree, filename):
#            """
#    输入：决策树，保存文件路径
#    输出：
#    描述：保存决策树到文件
#    """
        import pickle
        fw = open(filename, 'wb')
        pickle.dump(inputTree, fw)
        fw.close()
        
    def grabTree(self,filename):
        """
    输入：文件路径名
    输出：决策树
    描述：从文件读取决策树
    """
        import pickle
        fr = open(filename, 'rb')
        return pickle.load(fr)
    
#    def createTrainSet(self,dataSet):
##        path = r'E:\work\train.txt'
##        dataSet = np.loadtxt(path,delimiter=',')
#        dataSet = dataSet.tolist()
#        features = [dataSet[0][i] for i in range(len(dataSet[0])-1)]
#        return dataSet,features
    
    #def createDataSet():
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
    
    
#    def createTestSet(self):
#        path = r'E:\work\test.txt'
#        testSet = np.loadtxt(path,delimiter=',')
#        testSet = testSet.tolist()
#        return testSet
#    
    def loadData(self):
        path='C:\\Users\Administrator\Desktop\\re_20171217 - 副本\\for_9\\re_mwsmote_yeast4.csv'
        dataSet = np.loadtxt(path,delimiter=',')
        dataSet = dataSet.tolist()
        return dataSet

    def trainTestSplit(self,dataSet):
        Max_Set = [] #多数类样本集
        Min_Set = [] #少数类样本集
#        np.random.shuffle(dataSet) #打乱样本集
        train_size = 0.9 #0.6作为训练集
#        test_size = 1 - train_size #0.4作为测试集
        for d_Set in dataSet:
            if d_Set[-1] == 1.0: #此处1代表多数类
                Max_Set.append(d_Set)
            if d_Set[-1] == 0.0: #此处0代表少数类
                Min_Set.append(d_Set)
#        np.random.shuffle(Max_Set)
#        np.random.shuffle(Min_Set)
        trainSample1,testSample1 = train_test_split(Max_Set,train_size=train_size) 
        trainSample2,testSample2 = train_test_split(Min_Set,train_size=train_size) #少数类中的80%用于训练，20%用于测试
        trainSample = trainSample1 + trainSample2
        testSample = testSample1 + testSample2
#        trainSample = trainSample.tolist()
#        testSample = testSample.tolist()
        features = [dataSet[0][i] for i in range(len(dataSet[0])-1)]
        #trainSample,testSample = train_test_split(dataSet, train_size=train_size)
        return trainSample,testSample,features 
    #def createTestSet():
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
#     def rundir(self,path):
#
    def main(self):
        correct = 0
        dataSet = c45.loadData()
        trainSample,testSample,features = c45.trainTestSplit(dataSet)
#        dataSet, features = c45.createTrainSet()
        labels_tmp = features[:] # 拷贝，createTree会改变features
        desicionTree = c45.createTree(trainSample, labels_tmp)
        print('desicionTree:\n', desicionTree)
#        testSet = c45.createTestSet()
        testSet1 = testSample[:-1] #testSet1是testSet的去除类标后的属性列
        n = len(testSample)
        TP=0  #被预测的样本是正的正样本
        FP=0  #被预测的样本是正的负样本
        FN=0  #被预测的样本是负的正样本
        TN=0  #被预测的样本是负的负样本
        print("测试样本个数：",n)
        for test_data in testSample:
            clabel = c45.classify(desicionTree, features, test_data)
            if clabel == test_data[-1]:
                correct += 1
            if clabel==0.0 and test_data[-1]==0.0: #实际是正类，预测为正类
                TP += 1
            if clabel==0.0 and test_data[-1]==1.0: #实际是负类，预测为正类
                FP+=1
            if clabel==1.0 and test_data[-1]==0.0: #实际是正类，预测为负类
                FN+=1
            if clabel==1.0 and test_data[-1]==1.0: #实际是负类，预测为负类
                TN+=1
        print("TP:",TP)
        print("FP:",FP)
        print("FN:",FN)
        print("TN:",TN)
        print("精确度(Precision):",TP/(TP+FP))
        print("召回率(Recall)",TP/(TP+FN))
        print("F-measure:",(2*TP/(TP+FP)*TP/(TP+FN))/(TP/(TP+FP)+TP/(TP+FN)))
        print("G-mean:",np.sqrt((TP/(TP+FN))*(TN/(TN+FP))))
        print("精准率（Accuracy）:",(TP+TN)/(TP+FP+FN+TN))
        print("正确分类个数：",correct)
#        print("准确率：",correct/float(n))
        print('classifyResult:\n', c45.classifyAll(desicionTree, features, testSet1))


if __name__ == '__main__':

    classLabel = list()
    c45 = C45()
    c45.main()