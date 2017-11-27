from numpy import *
import numpy as np
import re
import time
from random import _inst
import sys
import random

'''加载样本'''
radius_scale = 0.5


def loadSample(filename):
    f = open(filename, 'r')
    inData = f.readlines()
    dataSet = list()
    for line in inData:
        line = line.strip()
        strList = re.split(r'[\s,\t]+', line)
        numList = list()
        for item in strList:
            num = float(item)
            numList.append(num)
        dataSet.append(numList)
    f.close()
    return dataSet


'''给样本集合排序，将相同的类别的标号放在一起，结果存入子集序号向量I中'''


def sortData(dataSet):
    I = dict()
    I1 = dict()  # 初始覆盖标记
    for item in dataSet:
        flag = int(item[-1])
        if flag not in I.keys():
            I[flag] = list()
            I1[flag] = list()
        I[flag].append(item[:-1])
        I1[flag].append(0)
    I = dict(sorted(I.items(), key=lambda x: x[0]))
    return I1, I


'''属性归一化'''


def Normalization(dataSet):
    # 找每一列的最大最小值
    vec_Max = list()
    vec_Min = list()
    maxValue = -1
    minValue = 999999
    dataSet = np.array(dataSet)
    for j in range(len(dataSet[0]) - 1):  # lie
        for i in range(len(dataSet)):  # hang
            if dataSet[i][j] < minValue:
                minValue = dataSet[i][j]
            if dataSet[i][j] > maxValue:
                maxValue = dataSet[i][j]
        vec_Max.append(maxValue)
        vec_Min.append(minValue)
    for j in range(len(dataSet[0]) - 1):  # lie
        for i in range(len(dataSet)):  # hang
            if vec_Max[j] - vec_Min[j] < 1e-6:
                dataSet[i][j] = 0
            else:
                dataSet[i][j] = (dataSet[i][j] - vec_Min[j]) / (vec_Max[j] - vec_Min[j])
    # dataSet = splitDataSet(dataSet)
    # 再将数组转化为列表
    features = list()
    for i in dataSet:
        features.append(i[0:len(i)])
    dataSet = features
    for i in range(len(dataSet)):
        dataSet[i] = list(dataSet[i])
    return dataSet


'''将样本集samples中得样本投射到球面上,并作向量单位化处理'''


def Unitization(dataSet):
    # dataSet = splitDataSet(dataSet)
    maxInner = inner_product(dataSet[0], dataSet[0])  # 初始化最大内积
    # 找最大内积
    for i in range(len(dataSet)):  # hang
        # 第i行数据的内积
        t = inner_product(dataSet[i][0:len(dataSet[i]) - 1], dataSet[i][0:len(dataSet[i]) - 1])
        if maxInner < t:
            maxInner = t
    for i in range(len(dataSet)):  # 增加一维，将样本投射到球面上
        d = inner_product(dataSet[i][0:len(dataSet[i]) - 1], dataSet[i][0:len(dataSet[i]) - 1])
        t = sqrt(maxInner - d)
        dataSet[i].insert(-1, t)
        # dataSet[i].append(t)
    for i in range(len(dataSet)):  # 单位化
        x = sqrt(inner_product(dataSet[i][0:len(dataSet[i]) - 1], dataSet[i][0:len(dataSet[i]) - 1]))
        for j in range(len(dataSet[0]) - 1):
            dataSet[i][j] /= x
    return dataSet


'''求向量内积'''


def inner_product(x1, x2):
    a = 0.0
    for i in range(len(x1)):
        a += x1[i] * x2[i]
    return a


'''训练样本'''


def trainSample(dataSet):
    I1, I = sortData(dataSet)
    dataAll = len(dataSet)
    cInfo = list()  # [[覆盖中心],覆盖半径,覆盖类别,覆盖样本数]
    '''对每一类样本求覆盖'''
    start_time = time.time()
    for t in I.keys():
        # 1.将I[i]中的样本号全部导入UnLearnedIdSet
        UnLearnedIdSet = []
        for j in range(len(I[t])):
            UnLearnedIdSet.append(j)
            # 对当前类别的样本进行学习
        while (len(UnLearnedIdSet)):
            cc = list()  # 覆盖中的样本序号
            s1 = _inst.sample(UnLearnedIdSet, 1)  # 随机选一个样本序号
            s = s1[0]
            computCover(t, s, I, I1, cc, cInfo)  ##cc是该类中，被覆盖的样本序号，cInfo是得到的覆盖
            UnLearnedIdSet = list(set(UnLearnedIdSet) ^ set(cc))
    end_time = time.time()
    # 记录实验数据
    k = len(cInfo)
    TrainInfo = {"训练时间": [], "训练样本总数": [], "覆盖数目": []}
    total_time = end_time - start_time
    TrainInfo["训练时间"].append(total_time)
    TrainInfo["训练样本总数"].append(dataAll)
    TrainInfo["覆盖数目"].append(len(cInfo))
    return cInfo, TrainInfo


'''计算覆盖t:样本类型s:子集中的样本序号'''


def computCover(t, s, I, I1, cc, cInfo):  # cc是覆盖样本序号
    d1 = find_d1(t, s, I, I1)  # 异类最近
    d2 = find_d2(t, s, I, d1)  # 同类最远
    d = (1 - radius_scale) * d2 + radius_scale * d1  # 覆盖半径
    a = I[t][s]
    '''记录覆盖信息'''
    c = list()
    c.append(I[t][s])  # 覆盖中心
    c.append(d)  # 覆盖半径
    c.append(t)  # 覆盖类别
    cov_num = 0
    for i in range(len(I[t])):
        k = I[t][i]
        if a == k:
            I1[t][i] = 1  # 覆盖标记
            cc.append(i)
            cov_num += 1
            continue
        if inner_product(I[t][s], I[t][i]) >= d:
            I1[t][i] = 1
            cc.append(i)
            cov_num += 1
    c.append(cov_num)  # 覆盖样本个数
    cInfo.append(c)


'''异类最近(求第t类样本子集中号为s的样本在异类中得最近点（内积最大）)
t:第t类样本
s:t类中的一个样本号
'''


def find_d1(t, s, I, I1):
    t1 = (t + 1) % len(I)
    for i in I.keys():
        if i != t:
            if i > t or i == 0:
                t1 = i
    d1 = inner_product(I[t1][0], I[t][s])
    for i in I.keys():
        if i != t:  # 异类
            for data in I[i]:
                x = inner_product(data, I[t][s])  # 第t类的第s个样本与异类的内积
                if d1 < x:
                    d1 = x
        else:  # 同类：将同类中已被覆盖的样本当作异类样本以保证同类覆盖相独立，未覆盖的不处理
            for j in range(len(I[t])):
                if I1[t][j] == 0:
                    continue
                else:
                    x = inner_product(I[t][s], I[t][j])
                    if d1 < x:
                        d1 = x
    return d1


'''求第t类样本子集中号为s的样本在同类中的最远距离d2（内积最小）'''


def find_d2(t, s, I, d1):
    d2 = inner_product(I[t][s], I[t][s])
    for i in range(len(I[t])):
        x = inner_product(I[t][s], I[t][i])
        if x > d1:  # 同类最远要以异类最近为界
            if d2 > x:
                d2 = x
    return d2


def printTrainDataInfo(dataSet, I):
    print("训练样本个数：", len(dataSet))
    print("训练样本维数：", np.array(dataSet).ndim)
    print("训练样本类别数：", len(I))
    for i in I.keys():
        n = 0
        for j in I[i]:
            n += 1
        print("类别：", i, "    个数：", n)


def printTestDataInfo(dataSet, I):
    print("测试样本个数：", len(dataSet))
    print("测试样本维数：", np.array(dataSet).ndim)
    print("测试样本类别数：", len(I))
    for i in I.keys():
        n = 0
        for j in I[i]:
            n += 1
        print("类别：", i, "    个数：", n)


'''测试样本'''


def testSample(dataSet, cInfo, rej_deal=0):  # 据识处理方法：中心最近法
    dataAll = len(dataSet)
    refuse = 0  # 据识样本数
    recog_corr = 0  # 可识别且正确分类数
    guss_corr = 0  # 对于据识样本，用据识处理方法处理后，可正确分类的样本数
    start_time = time.time()
    for i in range(len(dataSet)):
        y, sampleRej = classifySample(dataSet[i], cInfo, rej_deal)  # 分类
        if sampleRej == False:  # 可识别样本分类数
            if y == dataSet[i][-1]:
                recog_corr += 1
        else:  # 据识
            refuse += 1
            if y == dataSet[i][-1]:  # 据识样本用据识方法处理过后能正确识别的
                guss_corr += 1
    end_time = time.time()
    total_time = end_time - start_time
    TestInfo = {"测试时间": [], "测试样本总数": [], "据识样本数": [], "可正确识别的样本数": [], "据识样本处理过后可正确识别的样本数": []}
    Performence = {"可识正确率": [], "据识率": [], "据识正确率": [], "总正确率": []}

    Performence["可识正确率"].append(recog_corr / (dataAll))
    if refuse == 0:
        Performence["据识率"].append(0)
        Performence["据识正确率"].append(1)
    else:
        Performence["据识率"].append(refuse / dataAll)
        Performence["据识正确率"].append(guss_corr / refuse)

    Performence["总正确率"].append((guss_corr + recog_corr) / dataAll)

    TestInfo["测试时间"].append(total_time)
    TestInfo["测试样本总数"].append(dataAll)
    TestInfo["据识样本数"].append(refuse)
    TestInfo["可正确识别的样本数"].append(recog_corr)
    TestInfo["据识样本处理过后可正确识别的样本数"].append(guss_corr)
    return TestInfo, Performence


'''对样本x分类'''


def classifySample(x, cInfo, rej_deal):
    k1 = 0  # 用于标记样本距离覆盖中心最近的覆盖号
    k2 = 0  # 用于标记样本距离覆盖边缘最近的覆盖号
    k3 = 0  # 用于标记样本和覆盖中心的最大内积时的覆盖号
    k4 = 0  # 用于标记样本和覆盖引力最大的覆盖号
    sampleRej = True  # 初始时将样本x设为据识样本
    nearest_d = -sys.float_info[0]  # 求离覆盖中心最近，只需找x与覆盖中心的最大内积nearest_d，并标记覆盖号
    delta_d = sys.float_info[0]  # 求离覆盖边缘最近，只需找x与覆盖集中心的内积与覆盖半径差的最小绝对值，边缘最近只有在样本拒识时才有用
    max_inner = -sys.float_info[0]  # 求最大内积值
    max_gravity = -sys.float_info[0]  # 搜索最大引力
    for i in range(len(cInfo)):
        d = inner_product(cInfo[i][0], x[0:len(x) - 1])  # 覆盖中心与样本的内积
        r = cInfo[i][1]  # 覆盖半径
        if nearest_d < (d - r):
            nearest_d = d - r  # nearest_d 越大, x在覆盖C[i]中越靠近中心
            k1 = i
        if delta_d > abs(r - d):  # 找遍元最近距离，delta_d越小，离覆盖边缘越近
            delta_d = abs(r - d)
            k2 = i
        if max_inner < d:  # 找最大内积
            max_inner = d
            k3 = i
        if d < r:  # 计算覆盖引力,样本在覆盖之外
            f = float(cInfo[i][3]) / pow(d, 2.0)
            if f > max_gravity:
                max_gravity = f
                k4 = i
    y = 0  # 分类结果
    if nearest_d > 0:  # 可识别
        sampleRej = False
        y = cInfo[k1][2]
    else:  # 据识
        if rej_deal == 0:  # 中心最近
            y = cInfo[k3][2]
        if rej_deal == 1:  # 边缘最近
            y = cInfo[k2][2]
        if rej_deal == 3:  # 引力处理
            y = cInfo[k4][2]
    return y, sampleRej


'''随机训练&测试'''


def doTrainTest(dataSet):
    print("******随机测试******")
    m = int(input("请输入循环次数:"))
    sampleCnt = len(dataSet)
    trainNum = int(0.8 * sampleCnt)

    print("每次选取", sampleCnt, "个样本中的80%，共", trainNum, "个样本训练，其余的作为测试数据")
    for i in range(m):
        dataSet1 = dataSet
        random.shuffle(dataSet1)
        trainDataSet1 = dataSet1[0:trainNum]
        testDataSet1 = dataSet1[trainNum:]
        train_cInfo, TrainInfo = trainSample(trainDataSet1)
        testInfo, performence = testSample(testDataSet1, train_cInfo)
        print("第", i + 1, "次循环TrainInfo：", TrainInfo)
        print("第", i + 1, "次循环testInfo：", testInfo)
        print("第", i + 1, "次循环performrnce：", performence)


'''输出平均训练信息'''


def print_ave_result(total_num, i, nfold):
    print("第", i + 1, "轮迭代的平均值:")
    print("平均覆盖数:%.3f" % (sum(total_num["覆盖数"]) / nfold))
    print("平均训练时间:%.3f" % (sum(total_num["训练时间"]) / nfold))
    print("平均可识正确率:%.3f" % (sum(total_num["可识正确率"]) / nfold))
    print("平均据识正确率:%.3f" % (sum(total_num["据识正确率"]) / nfold))
    print("平均总正确率:%.3f" % (sum(total_num["总正确率"]) / nfold))
    print("平均测试时间:%.3f" % (sum(total_num["测试时间"]) / nfold))


'''nfold交叉训练'''


def doNfold(dataSet):
    # 样本数
    sampleCnt = len(dataSet)
    nfold = int(input("样本划分份数："))
    while True:
        if nfold < 1:
            nfold = int(input("交叉份数不能小于1，请重新输入"))
            continue
        if nfold > sampleCnt:
            nfold = int(input("交叉份数不能大于样本数目，请重新输入："))
            continue
        break
    print("样本总共分为", nfold, "份，其中", nfold - 1, "份作为训练，剩下1份作为测试，直到所有的样本都被训练和测试一遍")
    m = int(input("总共循环次数："))
    unit = int(sampleCnt / nfold)  # 每份样本数
    dataSelectedCnt = unit * nfold  # 实际参与训练的样本数
    dataSet1 = dataSet
    # random.shuffle(dataSet1)  # 打乱样本
    dataSet1 = dataSet1[0:dataSelectedCnt]  # 实际参与分析的数据
    for i in range(m):
        print("第", i + 1, "次", nfold, "交叉验证，总共循环", m, "次")
        total_num = {"覆盖数": [], "训练时间": [], "可识正确率": [], "据识正确率": [], "总正确率": [], "测试时间": []}
        istart = 0
        it1 = 0
        it2 = 0
        for j in range(nfold):
            it2 = it1 + unit
            trainData = dataSet1[istart:it1] + dataSet1[it2:]  # 训练数据
            testData = dataSet1[it1:it2]  # 测试数据
            cInfo, trainInfo = trainSample(trainData)
            testInfo, performence = testSample(testData, cInfo)
            it1 = it2
            total_num["覆盖数"].append(trainInfo["覆盖数目"][0])
            total_num["训练时间"].append(trainInfo["训练时间"][0])
            total_num["可识正确率"].append(performence["可识正确率"][0])
            total_num["据识正确率"].append(performence["据识正确率"][0])
            total_num["总正确率"].append(performence["总正确率"][0])
            total_num["测试时间"].append(testInfo["测试时间"][0])
            print("**********第", j + 1, "份作为测试集，其余的作为训练集的训练测试结果**********")
            print(trainInfo)
            print(testInfo)
            print(performence)
        print_ave_result(total_num, i, nfold)


if __name__ == '__main__':
    dataSet = loadSample("pendigits.txt")  # 加载数据
    # I1, I = sortData(dataSet)
    #
    # printTrainDataInfo(dataSet, I)
    dataSetNormal = Normalization(dataSet)  # 归一化
    dataUnit = Unitization(dataSetNormal)  # 单位化
    # I1, I = sortData(dataUnit)  # 给处理过的数据排序

    '''训练样本，cInfo为覆盖集合，TrainInfo为训练后的集合的信息'''
    # cInfo1, TrainInfo = trainSample(dataUnit, I, I1)
    # print(TrainInfo)
    # print(cInfo1)
    # '''测试训练效果'''
    # TestInfo,Performence = testSample(dataUnit, cInfo1)
    # print(TestInfo)
    # print(Performence)

    '''随机选取样本进行训练测试'''
    # doTrainTest(dataUnit)
    doNfold(dataUnit)
    # cInfo[[覆盖中心],覆盖半径,覆盖类别,覆盖样本数]
