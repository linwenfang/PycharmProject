from numpy import *
import numpy as np
import re
import time
import random
from skLearn.externals import joblib

'''加载样本'''


def loadSample(filename):
    f = open(filename, 'r')  # 打开文件
    inData = f.readlines()  # 读取文件数据，以列表形式返回
    dataSet = list()  # 用于存储格式化之后的数据
    for line in inData:
        line = line.strip()  # 将line开头和结尾的空行去掉
        strList = re.split(r'[\s,\t]+', line)  # strList为返回的列表,列表中的元素为str类型
        '''将strList中的str类型的元素转换为float类型，方便计算'''
        numList = list()
        for item in strList:
            num = float(item)
            numList.append(num)
        dataSet.append(numList)  # 将每一个样本以列表的形式存到dataSet这个列表中
    f.close()
    return dataSet


'''属性归一化：由于样本属性数值上的差距可能很大，为了消除这种情况对实验结果的影响
所以将样本属性归一化至[0,1]这个区间内'''


def Normalization(dataSet):
    # 找每一列的最大最小值
    vec_Max = list()  # 存储每一列的最大值
    vec_Min = list()  # 存储每一列的最小值
    maxValue = float('-inf')  # 初始化最大值,float('inf')为正无穷，float('-inf')为负无穷
    minValue = float('inf')  # 初始化最小值
    dataSet = np.array(dataSet)  # 将dataSet转为np数组的形式
    for j in range(len(dataSet[0]) - 1):  # 循环属性列，属性共len(dataSet[0]) - 1列，最后一列是类标
        '''循環找第j列的最大值與最小值'''
        for i in range(len(dataSet)):  # 循环样本个数
            if dataSet[i][j] < minValue:
                minValue = dataSet[i][j]
            if dataSet[i][j] > maxValue:
                maxValue = dataSet[i][j]
        vec_Max.append(maxValue)  # 第j列的最大值
        vec_Min.append(minValue)  # 第j列的最小值
    for j in range(len(dataSet[0]) - 1):  # 循環屬性列
        for i in range(len(dataSet)):
            '''若第j列的最大值与最小值的差小于10的-6次方,则将第j列的值都设置为0，否则按以下公式计算第j列的值'''
            if vec_Max[j] - vec_Min[j] < 1e-6:  # 若第j列的最大值与最小值的差小于10的-6次方
                dataSet[i][j] = (dataSet[i][j] - vec_Min[j]) / (vec_Max[j] - vec_Min[j]) + 0.001
            else:
                dataSet[i][j] = (dataSet[i][j] - vec_Min[j]) / (vec_Max[j] - vec_Min[j])
    '''以上代码执行之后，dataSet为归一化后的数组'''
    # 再将数组转化为列表
    dataSet = dataSet.tolist()
    return dataSet


'''求向量内积'''


def inner_product(x1, x2):
    a = 0.0
    for i in range(len(x1)):
        a += x1[i] * x2[i]
    return a


'''将样本集samples中得样本投射到球面上,并作向量单位化处理'''


def Unitization(dataSet):
    # 这里不需要进行数组的计算，所以直接去列表中的元素进行计算就可以了
    maxInner = float('-inf')  # 初始化最大内积
    # 找最大内积
    for i in range(len(dataSet)):  # 循环样本数
        # 第i行数据的内积,注意计算时要把最后一行的类标去掉
        t = inner_product(dataSet[i][:-1], dataSet[i][:-1])
        if maxInner < t:
            maxInner = t  # 最大内积为maxInner
    for i in range(len(dataSet)):  # 增加一维，将样本投射到球面上
        # d为第i个样本的内积
        d = inner_product(dataSet[i][:-1], dataSet[i][:-1])
        t = sqrt(maxInner - d)  # 这是将要增加的那一维属性值
        dataSet[i].insert(-1, t)  # 将t加到属性的最后一维，也就是类标前面的那一维
    '''为什么要模长归一化处理？为什么要这样计算?是不是为了让最后插入的那一列也在[0,1]区间内？如果这样的化，那就先升维，再归一化不行么？'''
    for i in range(len(dataSet)):  # 向量模长归一化处理
        x = sqrt(inner_product(dataSet[i][:-1], dataSet[i][:-1]))
        for j in range(len(dataSet[0]) - 1):
            dataSet[i][j] /= x
    return dataSet


'''给样本集合排序，将相同的类别的样本放在一起，结果存入子集序号向量I中,初始化覆盖标记'''


def sortData(dataSet):
    I = dict()  # 存储样本标号的字典，按样本类标存储，每一个key之下的都是样本的标号
    I1 = dict()  # 初始覆盖标记
    for i in range(len(dataSet)):  # 取样本集中的每一个样本的下标
        flag = int(dataSet[i][-1])  # 取类标
        if flag not in I.keys():
            I[flag] = list()  # 在字典中，类标为key，对应的value为一个列表，存储的是该类样本
            I1[flag] = list()  # 在字典中，类标为key，对应的value为一个列表，存储的是对应样本的覆盖标记
        I[flag].append(i)  # 将该样本的下标加入到I[key]中
        I1[flag].append(0)  # 该样本的覆盖标记初始为0
    I = dict(sorted(I.items(), key=lambda x: x[0]))  # 对字典I，按key的大小进行排序
    I1 = dict(sorted(I1.items(), key=lambda x: x[0]))
    return I1, I  # 返回样本覆盖标记集合，样本标号集合


'''异类最近(求第t类样本子集中号为s的样本在异类中得最近点（内积最大）)
t:第t类样本
s:t类中的一个样本号
异类最近-->距离最小-->内积最大

'''


def find_d1(t, s, I, I1, dataSet):
    # d1 = float('-inf')
    m = (t + 1) % len(I)
    d1 = inner_product(dataSet[s][:-1], dataSet[m][:-1])  # 求异类最近时的初始化d1
    # 计算异类中与t类中标号为s的样本的内积，返回最大的内积
    for i in I.keys():  # 循环类标
        if i != t:  # 异类中搜索
            # 在异类样本中，找与小标为s的样本的最大内积
            for data_index in I[i]:
                x = inner_product(dataSet[data_index][:-1], dataSet[s][:-1])  # 第t类的第s个样本与异类的内积
                if d1 < x:
                    d1 = x
        else:  # 同类：将同类中已被覆盖的样本当作异类样本以保证同类覆盖相独立，未覆盖的不处理
            for j in range(len(I[t])):
                if I1[t][j] == 0:  # 未被覆盖
                    continue
                else:  # 已被覆盖
                    x = inner_product(dataSet[s][:-1], dataSet[I[t][j]][:-1])  # 当做异类处理，求内积
                    if d1 < x:
                        d1 = x
    return d1  # 返回异类最大内积


'''求第t类样本子集中号为s的样本在同类中的最远距离d2（内积最小）
同类最远-->距离最大-->内积最小
'''


def find_d2(t, s, I, d1, dataSet):
    # d2 = float('inf')  # 初始化内积为无穷大
    d2 = inner_product(dataSet[s][:-1], dataSet[s][:-1])  # 求同类最远时的初始化d2
    for i in range(len(I[t])):
        x = inner_product(dataSet[s][:-1], dataSet[I[t][i]][:-1])  # t类中下标为s和下表为i的样本的内积
        if x > d1:  # 同类最远要以异类最近为界，在最近异类点的范围内找最远的同类样本
            if d2 > x:  # 求最小内积
                d2 = x
    return d2  # 返回最小内积。


'''计算覆盖      t:样本类型     s:样本序号（sui ji qu de fu gai zhong xin）
I：按样本类标组合的样本字典    I1：覆盖标记   cc：覆盖中的样本序号'''


def computCover(t, s, I, I1, cc, cInfo, dataSet,fw,dataSetOriginal):  # cc已经被覆盖的样本下标
    d1 = find_d1(t, s, I, I1, dataSet)  # 异类最近-->距离最小-->内积最大
    d2 = find_d2(t, s, I, d1, dataSet)  # 同类最远-->距离最大-->内积最小
    d = 0.5 * (d1 + d2)  # 覆盖半径,折中半径法
    '''记录覆盖信息'''
    c = list()  # [[覆盖中心],覆盖半径,覆盖类别,覆盖样本数]
    c.append(dataSet[s])  # 覆盖中心
    c.append(d)  # 覆盖半径
    c.append(int(dataSetOriginal[s][-1]))  # 覆盖类别
    cov_num = 0  # 覆盖中的样本数
    for i in range(len(I[t])):
        if I[t][i] == s:  # I[t][j]是覆盖中心本身
            I1[t][i] = 1  # 将样本下标为s的样本标记为已覆盖，记录覆盖次数
            cc.append(I[t][i])  # 将覆盖的样本下标加到cc列表中
            cov_num += 1  # 覆盖中的样本数加一
            continue  # 返回执行下一次循环
        if inner_product(dataSet[s][:-1], dataSet[I[t][i]][:-1]) >= d:  # 下标为I[t][i]的样本在覆盖范围之内
            I1[t][i] = 1  # 将样本下标为s的样本标记为已覆盖，记录覆盖次数
            cc.append(I[t][i])  # 将以覆盖的样本下标加到cc列表中
            cov_num += 1  # 覆盖中的样本数加一
    c.append(cov_num)  # 覆盖样本个数
    cInfo.append(c)
    '''保存覆盖信息'''
    fw.write("以下第一行为覆盖中心，覆盖半径："+str(c[1])+"覆盖类别："+str(c[2])+"覆盖样本数："+str(c[3])+'\n')
    fw.write(str(dataSetOriginal[s])+'\n')
    for i in cc:
        fw.write(str(dataSetOriginal[i])+'\n')







'''训练样本'''


def trainSample(dataSet,fw,dataSetOriginal):
    # I存储的是样本下标
    I1, I = sortData(dataSet)  # 先将样本集合中的数据排序，初始化覆盖标记
    dataAll = len(dataSet)  # 样本个数
    cInfo = list()  # [[覆盖中心],覆盖半径,覆盖类别,覆盖样本数]
    '''对每一类样本求覆盖'''
    start_time = time.time()  # 开始计时
    '''求t类样本的覆盖信息'''
    for t in I.keys():  # 循环样本类别
        UnLearnedIdSet = I[t]  # 将I[t](t类样本)中的样本号全部导入UnLearnedIdSet
        while (len(UnLearnedIdSet)):
            cc = list()  # 覆盖中的样本序号
            s = random.choice(UnLearnedIdSet)  # 从UnLearnedIdSet中随机选取一个样本号作为覆盖中心
            computCover(t, s, I, I1, cc, cInfo, dataSet,fw,dataSetOriginal)  ##cc是该类中，被覆盖的样本序号，cInfo是得到的覆盖

            UnLearnedIdSet = list(set(UnLearnedIdSet) ^ set(cc))  # 在UnLearnedIdSet中删除cc中已被覆盖的样本下标
    end_time = time.time()  # 结束训练计时
    # 记录实验数据
    TrainInfo = {"训练时间": [], "训练样本总数": [], "覆盖数目": []}
    total_time = end_time - start_time  # 训练时间
    TrainInfo["训练时间"].append(total_time)
    TrainInfo["训练样本总数"].append(dataAll)
    TrainInfo["覆盖数目"].append(len(cInfo))
    return cInfo, TrainInfo


'''测试样本'''


def testSample(dataSet, cInfo, rej_deal):  # rej_deal为据识处理方法
    dataAll = len(dataSet)
    refuse = 0  # 据识样本数
    recog_corr = 0  # 可识别且正确分类的样本数
    guss_corr = 0  # 对于据识样本，用据识处理方法处理后，可正确分类的样本数
    start_time = time.time()  # 开始计时
    for i in range(len(dataSet)):  # 循环样本数
        y, sampleRej = classifySample(dataSet[i], cInfo, rej_deal, dataSet)  # 分类
        if sampleRej == False:  # 可识别样本
            if y == dataSet[i][-1]:
                recog_corr += 1  # 可正确识别的样本数加1
        else:  # 据识sampleRej==True
            refuse += 1  # 据识样本数加1
            if y == dataSet[i][-1]:  # 据识样本用据识方法处理过后能正确识别的
                guss_corr += 1  # 据识处理后的识别样本数加1
    end_time = time.time()  # 结束计时
    total_time = end_time - start_time  # 训练时间
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


def classifySample(x, cInfo, rej_deal, dataSet):
    k1 = 0  # 用于标记样本距离覆盖中心最近的覆盖号
    k2 = 0  # 用于标记样本距离覆盖边缘最近的覆盖号
    k3 = 0  # 用于标记样本和覆盖中心的最大内积时的覆盖号
    k4 = 0  # 用于标记样本和覆盖引力最大的覆盖号
    sampleRej = True  # 初始时将样本x设为据识样本
    nearest_d = float('-inf')  # 求离覆盖中心距离最近，只需找x与覆盖中心的最大内积nearest_d，并标记覆盖号
    delta_d = float('inf')  # 求离覆盖边缘距离最近，只需找{（（x与覆盖中心的内积）与（覆盖半径）差）的最小绝对值}，边缘最近只有在样本拒识时才有用
    max_inner = float('-inf')  # 求最大内积值
    max_gravity = float('-inf')  # 搜索最大引力
    for i in range(len(cInfo)):  # 搜索覆盖信息
        '''第i个覆盖'''
        d = inner_product(cInfo[i][0][:-1], x[:-1])  # 覆盖中心与测试样本的内积
        r = cInfo[i][1]  # 覆盖半径
        '''测试样本在覆盖半径之内'''
        if nearest_d < (d - r):
            nearest_d = d - r  # nearest_d 越大, x在覆盖C[i]中越靠近中心
            k1 = i
        '''边缘最近。测试样本与覆盖边缘距离最近的覆盖号，距离最近-->内积最大'''
        if delta_d > abs(r - d):  # 找边缘最近距离，delta_d越小，离覆盖边缘越近
            delta_d = abs(r - d)
            k2 = i
        '''中心最近。测试样本与覆盖中心距离最近的覆盖号，距离最近-->内积最大'''
        if max_inner < d:  # 找最大内积
            max_inner = d
            k3 = i
        '''最大引力。测试样本与覆盖的引力最大的覆盖号'''
        if d < r:  # 样本在覆盖之外
            # 求{覆盖中样本数/(测试样本与此覆盖中心的距离的平方)}的最大值，内积最小值就为最大引力
            f = float(cInfo[i][3]) / pow(d, 2.0)
            if f > max_gravity:
                max_gravity = f
                k4 = i
    y = 0  # 测试样本预测的类别
    if nearest_d > 0:  # 可识别，样本与覆盖中心的距离小于覆盖半径d-r>0
        sampleRej = False
        y = cInfo[k1][2]
    else:  # 据识
        if rej_deal == 0:  # 中心最近
            y = cInfo[k3][2]
        if rej_deal == 1:  # 边缘最近
            y = cInfo[k2][2]
        if rej_deal == 3:  # 万有引力
            y = cInfo[k4][2]
    return y, sampleRej  # 若sampleRej返回True，则该样本为据识样本，y为测试样本类别


'''输出平均训练信息'''


def print_ave_result(total_num, i, nfold):
    print("第", i + 1, "轮迭代的平均值:")
    print("平均覆盖数:%d" % (sum(total_num["覆盖数"]) / nfold))
    print("平均训练时间:%.3f" % (sum(total_num["训练时间"]) / nfold))
    print("平均可识正确率:%.3f" % (sum(total_num["可识正确率"]) / nfold))
    print("平均据识正确率:%.3f" % (sum(total_num["据识正确率"]) / nfold))
    print("平均总正确率:%.3f" % (sum(total_num["总正确率"]) / nfold))
    print("平均测试时间:%.3f" % (sum(total_num["测试时间"]) / nfold))


'''nfold交叉训练'''


def doNfold(dataSetOriginal, rej_deal):
    '''归一化'''
    normalData = Normalization(dataSetOriginal)
    unitData = Unitization(normalData)
    fw=open('write.txt','w')

    sampleCnt = len(unitData)  # 样本总数
    nfold = int(input("样本划分份数："))  # nfold交叉
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
    # random.shuffle(dataSet)  # 打乱样本
    dataSet1 = unitData[0:dataSelectedCnt]  # 实际参与分析的数据
    for i in range(m):
        '''第i次循环'''
        print("第", i + 1, "次", nfold, "交叉验证，总共循环", m, "次")
        total_num = {"覆盖数": [], "训练时间": [], "可识正确率": [], "据识正确率": [], "总正确率": [], "测试时间": []}
        it1 = 0
        for j in range(nfold):
            '''第j次交叉'''
            it2 = it1 + unit  # 交叉数据划分边界
            trainData = dataSet1[:it1] + dataSet1[it2:]  # 训练数据
            testData = dataSet1[it1:it2]  # 测试数据
            cInfo, trainInfo = trainSample(trainData,fw,dataSetOriginal)  # 训练
            testInfo, performence = testSample(testData, cInfo, rej_deal)  # 测试
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
            for k in cInfo:
                print(k)
        print_ave_result(total_num, i, nfold)  # 输出平均训练信息

    fw.close()



if __name__ == '__main__':
    dataSet = loadSample('pendigits.txt')
    print("1、中心最近原则")
    print("2、边界最近原则")
    print("3、万有引力原则")
    rej_deal = int(input("据识样本处理方法："))
    # normalData = Normalization(dataSet)
    # unitData = Unitization(normalData)
    doNfold(dataSet, rej_deal)
    path="model.txt"


