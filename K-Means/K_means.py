from numpy import *
from random import _inst
import numpy as np
import matplotlib.pyplot as plt
import re

def fileMat(filename):
    file = open(filename, "r")
    contain = file.readlines()
    count = len(contain)
    features = zeros((count, len(re.split(r'[ ,;:\t]+',contain[0])) - 1))

    labels = []
    index = 0
    for lines in contain:
        line = lines.strip()
        listForm = re.split(r'[ ,;:\t]+',line)
        features[index:] = listForm[0:len(listForm) - 1]
        labels.append(listForm[-1])
        index += 1
    return labels, features


'''初始化聚类中心,随机取3个样本点'''


def initCentroids(dataSet, K):
    # 初始化k个质心，随机获取
    # 在dataSet中任取K个向量作为初始的中心向量
    return _inst.sample(dataSet, K)


'''样本点与每个聚类中心的距离'''


def ouShi(point1, point2):
    distance = np.sqrt(np.sum(np.square(point1 - point2)))
    return distance


'''计算样本中心点'''


def getMean(clusterDict):
    centerSet = list()
    for key in clusterDict.keys():
        centerSet.append(np.mean(np.array(clusterDict[key]), axis=0))  # 簇中样本的平均值
    return centerSet  # 返回的是簇中心的列表


'''聚类'''


def cluster(dataSet, centerSet):
    clusterDict = dict()
    for item in dataSet:
        flag = 0#类别标记
        minDistance = float("inf")#最小值
        for i in range(len(centerSet)):
            distance = ouShi(item, centerSet[i])
            if distance < minDistance:
                minDistance = distance
                flag = i  # 第i类
        if flag not in clusterDict.keys():
            clusterDict[flag] = list()
        clusterDict[flag].append(item)
    return clusterDict


'''计算平方误差,是根据簇中样本点与该簇中心点的欧氏距离的平方计算的'''


def getE(clusterDic):
    sum = 0.0
    for key in clusterDic.keys():
        distance = 0.0
        centerDistance = np.mean(clusterDic[key])
        for item in clusterDic[key]:
            dis = np.square(ouShi(item, centerDistance))
            distance += dis
        sum += distance
    return sum


def showCluster(centerSet, clusterDict):
    # 展示聚类结果

    colorMark = ['or', 'ok', 'og', 'oy',  'ob']  # 不同簇类的标记 'or' --> 'o'代表圆，'r'代表red，'b':blue
    centroidMark = ['dr', 'dk', 'dg', 'dy',  'db']  # 质心标记 同上'd'代表棱形
    for key in clusterDict.keys():
        plt.plot(centerSet[key][0], centerSet[key][1], centroidMark[key], markersize=12)  # 画质心点
        for item in clusterDict[key]:
            plt.plot(item[0], item[1], colorMark[key])  # 画簇类下的点

    plt.show()


if __name__ == '__main__':
    dataLabels, dataSet = fileMat("pen")
    firstCenterSet = initCentroids(list(dataSet), 2)
    print('初始聚类中心为：', firstCenterSet)
    clusterDict = cluster(dataSet, firstCenterSet)
    newE = getE(clusterDict)
    oldE = -0.0001
    print("------------------------------------ 第1次迭代 ------------------------------------")
    for key in clusterDict.keys():
        buff = list()
        for i in range(len(clusterDict[key])):
            buff.append(list(clusterDict[key][i]))
        print(key, ' --> ', buff)
    newCenterSet = list()
    for i in range(len(firstCenterSet)):
        newCenterSet.append(list(firstCenterSet[i]))
    print('k个均值向量: ', newCenterSet)
    print('平均均方误差: ', newE)
    showCluster(firstCenterSet, clusterDict)
    d = 2
    while abs(newE - oldE) !=0:  # 当连续两次聚类结果小于0.0001时，迭代结束
        centerSet = getMean(clusterDict)  # 获得新的质心
        clusterDict = cluster(dataSet, centerSet)  # 新的聚类结果
        oldE = newE
        newE = getE(clusterDict)

        print('------------------------------------------- 第%d次迭代 -------------------------------------------' % d)
        for key in clusterDict.keys():
            buff = list()
            for i in range(len(clusterDict[key])):
                buff.append(list(clusterDict[key][i]))
            print(key, ' --> ', buff)
        newCenterSet = list()
        for i in range(len(firstCenterSet)):
            newCenterSet.append(list(firstCenterSet[i]))
        print('k个均值向量: ', newCenterSet)
        print('平均均方误差: ', newE)
        showCluster(centerSet, clusterDict)
        d += 1
