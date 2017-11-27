import re
import numpy as np
import random


class Basic:
    '''加载样本'''

    def loadSample(self, filename):
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
            dataSet.append(numList)
        f.close()
        return dataSet

    '''将数据处理成np.array格式'''

    def Split(self, dataSet):
        '''创建一个len(dataSet) x len(dataSet[0].split(','))-1的矩阵,是样本属性的个数'''
        features = np.zeros((len(dataSet), len(dataSet[0]) - 1))
        labels = []
        index = 0
        for line in dataSet:  # 一行行读数据文件
            '''将line中的前len(line)-1列加入到矩阵中去'''
            features[index:] = line[0:len(line) - 1]
            labels.append(line[-1])  # 最后一列作为类标
            index += 1
            '''返回的features为特征矩阵，labels为类别列表'''
        labels = np.array([int(x) for x in labels])
        return features, labels


class ccaClean:
    '''属性归一化：由于样本属性数值上的差距可能很大，为了消除这种情况对实验结果的影响
    所以将样本属性归一化至[0,1]这个区间内'''

    def Normalization(self, dataSet):
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
                if vec_Max[j] - vec_Min[j] == 0:
                    vec_Max[j] = vec_Max[j] + 0.001
                '''若第j列的最大值与最小值的差小于10的-6次方,则将第j列的值都设置为0，否则按以下公式计算第j列的值'''
                if vec_Max[j] - vec_Min[j] < 1e-6:  # 若第j列的最大值与最小值的差小于10的-6次方
                    dataSet[i][j] = (dataSet[i][j] - vec_Min[j]) / (vec_Max[j] - vec_Min[j])
                else:
                    dataSet[i][j] = (dataSet[i][j] - vec_Min[j]) / (vec_Max[j] - vec_Min[j])
        '''以上代码执行之后，dataSet为归一化后的数组'''
        # 再将数组转化为列表
        dataSet = dataSet.tolist()
        return dataSet

    '''求向量内积'''

    def inner_product(self, x1, x2):
        a = 0.0
        for i in range(len(x1)):
            a += x1[i] * x2[i]
        return a

    '''将样本集samples中得样本投射到球面上,并作向量单位化处理'''

    def Unitization(self, dataSet):
        # 这里不需要进行数组的计算，所以直接去列表中的元素进行计算就可以了
        maxInner = float('-inf')  # 初始化最大内积
        # 找最大内积
        for i in range(len(dataSet)):  # 循环样本数
            # 第i行数据的内积,注意计算时要把最后一行的类标去掉
            t = self.inner_product(dataSet[i][:-1], dataSet[i][:-1])
            if maxInner < t:
                maxInner = t  # 最大内积为maxInner
        for i in range(len(dataSet)):  # 增加一维，将样本投射到球面上
            # d为第i个样本的内积
            d = self.inner_product(dataSet[i][:-1], dataSet[i][:-1])
            t = np.sqrt(maxInner - d)  # 这是将要增加的那一维属性值
            dataSet[i].insert(-1, t)  # 将t加到属性的最后一维，也就是类标前面的那一维
        '''为什么要模长归一化处理？为什么要这样计算?是不是为了让最后插入的那一列也在[0,1]区间内？如果这样的化，那就先升维，再归一化不行么？'''
        for i in range(len(dataSet)):  # 向量模长归一化处理
            x = np.sqrt(self.inner_product(dataSet[i][:-1], dataSet[i][:-1]))
            for j in range(len(dataSet[0]) - 1):
                dataSet[i][j] /= x
        return dataSet

    '''给样本集合排序，将相同的类别的样本放在一起，结果存入子集序号向量I中,初始化覆盖标记'''

    def sorData(self, dataSet):
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

    def find_d1(self, t, s, I, I1, dataSet):
        # d1 = float('-inf')
        m = (t + 1) % len(I)
        d1 = self.inner_product(dataSet[s][:-1], dataSet[m][:-1])  # 求异类最近时的初始化d1
        # 计算异类中与t类中标号为s的样本的内积，返回最大的内积
        for i in I.keys():  # 循环类标
            if i != t:  # 异类中搜索
                # 在异类样本中，找与小标为s的样本的最大内积
                for data_index in I[i]:
                    x = self.inner_product(dataSet[data_index][:-1], dataSet[s][:-1])  # 第t类的第s个样本与异类的内积
                    if d1 < x:
                        d1 = x
            else:  # 同类：将同类中已被覆盖的样本当作异类样本以保证同类覆盖相独立，未覆盖的不处理
                for j in range(len(I[t])):
                    if I1[t][j] == 0:  # 未被覆盖
                        continue
                    else:  # 已被覆盖
                        x = self.inner_product(dataSet[s][:-1], dataSet[I[t][j]][:-1])  # 当做异类处理，求内积
                        if d1 < x:
                            d1 = x
        return d1  # 返回异类最大内积

    '''求第t类样本子集中号为s的样本在同类中的最远距离d2（内积最小）
    同类最远-->距离最大-->内积最小
    '''

    def find_d2(self, t, s, I, d1, dataSet):
        # d2 = float('inf')  # 初始化内积为无穷大
        d2 = self.inner_product(dataSet[s][:-1], dataSet[s][:-1])  # 求同类最远时的初始化d2
        for i in range(len(I[t])):
            x = self.inner_product(dataSet[s][:-1], dataSet[I[t][i]][:-1])  # t类中下标为s和下表为i的样本的内积
            if x > d1:  # 同类最远要以异类最近为界，在最近异类点的范围内找最远的同类样本
                if d2 > x:  # 求最小内积
                    d2 = x
        return d2  # 返回最小内积。

    '''计算覆盖      t:样本类型     s:样本序号（sui ji qu de fu gai zhong xin）
    I：按样本类标组合的样本字典    I1：覆盖标记   cc：覆盖中的样本序号'''

    def computCover(self, t, s, I, I1, cc, cInfo, dataSet, fw, fd, dataSetOriginal):
        d1 = self.find_d1(t, s, I, I1, dataSet)  # 异类最近-->距离最小-->内积最大
        d2 = self.find_d2(t, s, I, d1, dataSet)  # 同类最远-->距离最大-->内积最小
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
            if self.inner_product(dataSet[s][:-1], dataSet[I[t][i]][:-1]) >= d:  # 下标为I[t][i]的样本在覆盖范围之内
                I1[t][i] = 1  # 将样本下标为s的样本标记为已覆盖，记录覆盖次数
                cc.append(I[t][i])  # 将以覆盖的样本下标加到cc列表中
                cov_num += 1  # 覆盖中的样本数加一
        c.append(cov_num)  # 覆盖样本个数
        cInfo.append(c)
        '''保存覆盖信息'''
        if len(cc) == 1:  # 写入覆盖中样本数维1的样本，也就是要清除的样本
            for i in cc:  # 写入最终保留下来的样本
                for j in range(len(dataSetOriginal[i])):
                    if j < len(dataSetOriginal[i]) - 1:
                        fd.write(str(dataSetOriginal[i][j]) + ',')
                    else:
                        fd.write(str(int(dataSetOriginal[i][j])))
                fd.write('\n')
                # fd.write(str(dataSetOriginal[cc[0]][1:-1]) + '\n')
        else:
            for i in cc:  # 写入最终保留下来的样本
                for j in range(len(dataSetOriginal[i])):
                    if j < len(dataSetOriginal[i]) - 1:
                        fw.write(str(dataSetOriginal[i][j]) + ',')
                    else:
                        fw.write(str(int(dataSetOriginal[i][j])))
                fw.write('\n')

    def My_cca(self, load_file, re_sampled_file, del_sambled_file):
        basi = Basic()
        dataSet_Original = basi.loadSample(load_file)  # 加载样本
        NormalData = self.Normalization(dataSet_Original)  # 归一化
        unitData = self.Unitization(NormalData)  # 投影
        fw = open(re_sampled_file, 'w')  # 写入最终处理后的文件
        fd = open(del_sambled_file, 'w')  # 写入cca删除的文件
        I1, I = self.sorData(unitData)  # 先将样本集合中的数据排序，初始化覆盖标记
        cInfo = list()  # [[覆盖中心],覆盖半径,覆盖类别,覆盖样本数]
        for t in I.keys():  # 循环样本类别
            UnLearnedIdSet = I[t]  # 将I[t](t类样本)中的样本号全部导入UnLearnedIdSet
            while (len(UnLearnedIdSet)):
                cc = list()  # 覆盖中的样本序号
                s = random.choice(UnLearnedIdSet)  # 从UnLearnedIdSet中随机选取一个样本号作为覆盖中心
                self.computCover(t, s, I, I1, cc, cInfo, unitData, fw, fd,
                                 dataSet_Original)  ##cc是该类中，被覆盖的样本序号，cInfo是得到的覆盖
                UnLearnedIdSet = list(set(UnLearnedIdSet) ^ set(cc))  # 在UnLearnedIdSet中删除cc中已被覆盖的样本下标

        fd.close()
        fw.close()
if __name__ == '__main__':
    load_file=""
    resemple_file=""
    del_file=""
    recca=ccaClean()
    recca.My_cca(load_file,resemple_file,del_file)
