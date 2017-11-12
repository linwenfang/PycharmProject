import numpy as np
import re
from collections import Counter
import random


def loadSample(filename):
    f = open(filename, 'r')
    inData = f.readlines()  # 读取f中的内容
    dataSet = list()
    for line in inData:
        line = line.strip()  # 去掉line行首和行尾的空格
        strList = re.split(r'[\s,\t]+', line)  # 正则表达式分割样本属性列，分割后属性值类型为str
        numList = list()
        for item in strList:
            num = float(item)  # 将属性值类型str---->float
            numList.append(num)  # numlist存放的是每一个样本的属性行
        dataSet.append(numList)
    f.close()
    return dataSet  # 返回一个处理后的列表类型的数据集


'''分割样本类别和样本特征，返回属性集合，
和样本类别集合属性集合
和样本类别集合中的样本一一对应
'''


def split_Y(dataSet):
    dataSet1 = list()  # 样本集合
    dataLabelSet = list()  # 样本类别集合
    for i in range(len(dataSet)):
        dataSet1.append(dataSet[i][:-1])  # 添加样本属性
        dataLabelSet.append(int(dataSet[i][-1]))  # 添加样本类别
    return dataSet1, dataLabelSet


'''计算测试样本与各训练样本的欧式距离'''


def calOushi(trainSet, testInstance):
    '''输入是个列表，要转换为数组才可以计算'''
    trainSet = np.array(trainSet)
    testInstance = np.array(testInstance)
    # distSet为欧氏距离集合，按顺序存放每一个测试样本与所有的训练样本的欧氏距离
    '''每个训练样本和测试样本的欧氏距离'''
    distSet = np.sqrt(np.sum(np.square(testInstance - trainSet), axis=1))  # 计算欧氏距离np.sum(axis=1)按行累加
    return distSet


'''对距离集合排序,取比例最大的类别'''


def sor_dist(distSet, dataLebelSet, k):
    labels = list()
    sortIndex = np.argsort(distSet)[0:k]  # 把下标按距离远近排序，argsort的结果为下标的数组,取前k个
    for i in sortIndex:
        labels.append(dataLebelSet[i])  # 取欧氏距离最小的k个值的类别
    countLabels = dict(Counter(labels))  # 统计labels中的元素出现次数，用字典的形式保存
    max_count = sorted(countLabels.items(), key=lambda x: x[1], reverse=True)  # 按字典的value大小，将countLabels中的数据从大到小排序
    return max_count[0][0]


'''计算正确率'''


def cal_acc(new_testLabels, old_testLabels):
    m = 0  # 正样本个数
    n = 0  # 测试样本总数
    if len(new_testLabels) == len(old_testLabels):
        for i in range(len(new_testLabels)):
            if new_testLabels[i] == old_testLabels[i]:  # 新测试样本的类别与原测试样本的类别相等
                m += 1
            n += 1
    accuracy = m / n * 100.0
    return accuracy


'''分类'''


def classify(trainData, testData, k):
    '''划分属性与类标'''''''''
    trainData, trainLabels = split_Y(trainData)
    testData, testLabels = split_Y(testData)
    new_labels = list()  # 测试样本预测的类标
    accuracy = list()  # 预测正确率
    '''对testData的每一个样本循环'''
    for i in range(len(testData)):
        '''欧氏距离'''
        distSet = calOushi(trainData, testData[i])  # 计算欧氏距离
        '''排序'''
        max_count = sor_dist(distSet, trainLabels, k)  # 对欧氏距离用下标排序，去欧氏距离最小的k个样本下标，返回类别比例最大的类标
        new_labels.append(max_count)  # 按顺序添加到预测集合里
    for j in range(len(testLabels)):
        print(testData[j], "----->", testLabels[j], "----->", new_labels[j])
    acc = cal_acc(new_labels, testLabels)  # 预测准确率
    return acc


'''划分训练集和测试集（n交叉验证）'''


def donfold(dataSet, nfold, k):
    dataCnt = len(dataSet)  # 样本长度
    while True:
        if nfold < 1:
            nfold = int(input("交叉份数不能小于1，请重新输入"))
            continue
        if nfold > dataCnt:
            nfold = int(input("交叉份数不能大于样本数目，请重新输入："))
            continue
        break
    print("样本总共分为", nfold, "份，其中", nfold - 1, "份作为训练，剩下1份作为测试")
    unit = int(dataCnt / nfold)  # 每份样本数
    dataSelectedCnt = unit * nfold  # 实际处理的样本数
    dataSelectedSet = dataSet[0:dataSelectedCnt]  # 实际处理的样本
    print("总样本数：", dataSelectedCnt, "训练样本数：", unit, "测试样本数：", dataSelectedCnt - unit)
    it1 = 0
    istart = 0
    accuracy = list()  # 正确率集合
    for i in range(nfold):
        print("第", i + 1, "次", nfold, "交叉验证")
        it2 = it1 + unit  # 划分下标
        trainData = dataSelectedSet[istart:it1] + dataSelectedSet[it2:]  # 训练集
        testData = dataSelectedSet[it1:it2]  # 测试集
        acc = classify(trainData, testData, k)  # 分类函数，返回的是样本测试的准确率
        accuracy.append(acc)  # 把第i次交叉验证的准确率存到accuracy中
        print("第", i + 1, "次准确率为：", acc, "%")
    print("当k=", k, "时，平均正确率为：", sum(accuracy) / len(accuracy), "%")


if __name__ == '__main__':
    dataSet = loadSample('pendigits.txt')
    # random.shuffle(dataSet)  # 打乱样本
    print("k=0时退出：")
    nfold = int(input("样本划分份数："))
    while True:
        k = int(input("请输入k："))
        if k == 0:
            break
        donfold(dataSet, nfold, k)
