#coding=gbk
import random
import re
import numpy as np
from LearningText import toArff
import os
class Basic:
    '''��������'''
    def loadSample(self, filename):
        f = open(filename, 'r')  # ���ļ�
        inData = f.readlines()  # ��ȡ�ļ����ݣ����б���ʽ����
        dataSet = list()  # ���ڴ洢��ʽ��֮�������
        for line in inData:
            line = line.strip()  # ��line��ͷ�ͽ�β�Ŀ���ȥ��
            strList = re.split(r'[\s,\t]+', line)  # strListΪ���ص��б�,�б��е�Ԫ��Ϊstr����
            '''��strList�е�str���͵�Ԫ��ת��Ϊfloat���ͣ��������'''
            numList = list()
            for item in strList:
                num = float(item)
                numList.append(num)
            dataSet.append(numList)
        f.close()
        return dataSet
class CCA:
    '''���Թ�һ������������������ֵ�ϵĲ����ܴܺ�Ϊ���������������ʵ������Ӱ��
    ���Խ��������Թ�һ����[0,1]���������'''

    def Normalization(self, dataSet):
        # ��ÿһ�е������Сֵ
        vec_Max = list()  # �洢ÿһ�е����ֵ
        vec_Min = list()  # �洢ÿһ�е���Сֵ
        maxValue = float('-inf')  # ��ʼ�����ֵ,float('inf')Ϊ�����float('-inf')Ϊ������
        minValue = float('inf')  # ��ʼ����Сֵ
        dataSet = np.array(dataSet)  # ��dataSetתΪnp�������ʽ
        for j in range(len(dataSet[0]) - 1):  # ѭ�������У����Թ�len(dataSet[0]) - 1�У����һ�������
            '''ѭ�h�ҵ�j�е����ֵ�c��Сֵ'''
            for i in range(len(dataSet)):  # ѭ����������
                if dataSet[i][j] < minValue:
                    minValue = dataSet[i][j]
                if dataSet[i][j] > maxValue:
                    maxValue = dataSet[i][j]
            vec_Max.append(maxValue)  # ��j�е����ֵ
            vec_Min.append(minValue)  # ��j�е���Сֵ
        for j in range(len(dataSet[0]) - 1):  # ѭ�h������
            for i in range(len(dataSet)):
                if vec_Max[j]-vec_Min[j]==0:
                    vec_Max[j]=vec_Max[j]+0.001
                '''����j�е����ֵ����Сֵ�Ĳ�С��10��-6�η�,�򽫵�j�е�ֵ������Ϊ0���������¹�ʽ�����j�е�ֵ'''
                if vec_Max[j] - vec_Min[j] < 1e-6:  # ����j�е����ֵ����Сֵ�Ĳ�С��10��-6�η�
                    dataSet[i][j] = (dataSet[i][j] - vec_Min[j]) / (vec_Max[j] - vec_Min[j])
                else:
                    dataSet[i][j] = (dataSet[i][j] - vec_Min[j]) / (vec_Max[j] - vec_Min[j])
        '''���ϴ���ִ��֮��dataSetΪ��һ���������'''
        # �ٽ�����ת��Ϊ�б�
        dataSet = dataSet.tolist()
        return dataSet

    '''�������ڻ�'''

    def inner_product(self, x1, x2):
        a = 0.0
        for i in range(len(x1)):
            a += x1[i] * x2[i]
        return a

    '''��������samples�е�����Ͷ�䵽������,����������λ������'''

    def Unitization(self, dataSet):
        # ���ﲻ��Ҫ��������ļ��㣬����ֱ��ȥ�б��е�Ԫ�ؽ��м���Ϳ�����
        maxInner = float('-inf')  # ��ʼ������ڻ�
        # ������ڻ�
        for i in range(len(dataSet)):  # ѭ��������
            # ��i�����ݵ��ڻ�,ע�����ʱҪ�����һ�е����ȥ��
            t = self.inner_product(dataSet[i][:-1], dataSet[i][:-1])
            if maxInner < t:
                maxInner = t  # ����ڻ�ΪmaxInner
        for i in range(len(dataSet)):  # ����һά��������Ͷ�䵽������
            # dΪ��i���������ڻ�
            d = self.inner_product(dataSet[i][:-1], dataSet[i][:-1])
            t = np.sqrt(maxInner - d)  # ���ǽ�Ҫ���ӵ���һά����ֵ
            dataSet[i].insert(-1, t)  # ��t�ӵ����Ե����һά��Ҳ�������ǰ�����һά
        '''ΪʲôҪģ����һ������ΪʲôҪ��������?�ǲ���Ϊ�������������һ��Ҳ��[0,1]�����ڣ���������Ļ����Ǿ�����ά���ٹ�һ������ô��'''
        for i in range(len(dataSet)):  # ����ģ����һ������
            x = np.sqrt(self.inner_product(dataSet[i][:-1], dataSet[i][:-1]))
            for j in range(len(dataSet[0]) - 1):
                dataSet[i][j] /= x
        return dataSet

    '''�������������򣬽���ͬ��������������һ�𣬽�������Ӽ��������I��,��ʼ�����Ǳ��'''

    def sorData(self, dataSet):
        I = dict()  # �洢������ŵ��ֵ䣬���������洢��ÿһ��key֮�µĶ��������ı��
        I1 = dict()  # ��ʼ���Ǳ��
        for i in range(len(dataSet)):  # ȡ�������е�ÿһ���������±�
            flag = int(dataSet[i][-1])  # ȡ���
            if flag not in I.keys():
                I[flag] = list()  # ���ֵ��У����Ϊkey����Ӧ��valueΪһ���б��洢���Ǹ�������
                I1[flag] = list()  # ���ֵ��У����Ϊkey����Ӧ��valueΪһ���б��洢���Ƕ�Ӧ�����ĸ��Ǳ��
            I[flag].append(i)  # �����������±���뵽I[key]��
            I1[flag].append(0)  # �������ĸ��Ǳ�ǳ�ʼΪ0
        I = dict(sorted(I.items(), key=lambda x: x[0]))  # ���ֵ�I����key�Ĵ�С��������
        I1 = dict(sorted(I1.items(), key=lambda x: x[0]))
        return I1, I  # �����������Ǳ�Ǽ��ϣ�������ż���

    '''�������(���t�������Ӽ��к�Ϊs�������������е�����㣨�ڻ����)
    t:��t������
    s:t���е�һ��������
    �������-->������С-->�ڻ����

    '''

    def find_d1(self, t, s, I, I1, dataSet):
        # d1 = float('-inf')
        m = (t + 1) % len(I)
        d1 = self.inner_product(dataSet[s][:-1], dataSet[m][:-1])  # ���������ʱ�ĳ�ʼ��d1
        # ������������t���б��Ϊs���������ڻ������������ڻ�
        for i in I.keys():  # ѭ�����
            if i != t:  # ����������
                # �����������У�����С��Ϊs������������ڻ�
                for data_index in I[i]:
                    x = self.inner_product(dataSet[data_index][:-1], dataSet[s][:-1])  # ��t��ĵ�s��������������ڻ�
                    if d1 < x:
                        d1 = x
            else:  # ͬ�ࣺ��ͬ�����ѱ����ǵ������������������Ա�֤ͬ�า���������δ���ǵĲ�����
                for j in range(len(I[t])):
                    if I1[t][j] == 0:  # δ������
                        continue
                    else:  # �ѱ�����
                        x = self.inner_product(dataSet[s][:-1], dataSet[I[t][j]][:-1])  # �������ദ�����ڻ�
                        if d1 < x:
                            d1 = x
        return d1  # ������������ڻ�

    '''���t�������Ӽ��к�Ϊs��������ͬ���е���Զ����d2���ڻ���С��
    ͬ����Զ-->�������-->�ڻ���С
    '''

    def find_d2(self, t, s, I, d1, dataSet):
        # d2 = float('inf')  # ��ʼ���ڻ�Ϊ�����
        d2 = self.inner_product(dataSet[s][:-1], dataSet[s][:-1])  # ��ͬ����Զʱ�ĳ�ʼ��d2
        for i in range(len(I[t])):
            x = self.inner_product(dataSet[s][:-1], dataSet[I[t][i]][:-1])  # t�����±�Ϊs���±�Ϊi���������ڻ�
            if x > d1:  # ͬ����ԶҪ���������Ϊ�磬����������ķ�Χ������Զ��ͬ������
                if d2 > x:  # ����С�ڻ�
                    d2 = x
        return d2  # ������С�ڻ���

    '''���㸲��      t:��������     s:������ţ�sui ji qu de fu gai zhong xin��
    I�������������ϵ������ֵ�    I1�����Ǳ��   cc�������е��������'''

    def computCover(self, t, s, I, I1, cc, cInfo, dataSet, fw, fd,
                    dataSetOriginal,del_old,del_old_min,del_old_maj):
        d1 = self.find_d1(t, s, I, I1, dataSet)  # �������-->������С-->�ڻ����
        d2 = self.find_d2(t, s, I, d1, dataSet)  # ͬ����Զ-->�������-->�ڻ���С
        d = 0.5 * (d1 + d2)  # ���ǰ뾶,���а뾶��
        '''��¼������Ϣ'''

        c = list()  # [[��������],���ǰ뾶,�������,����������]
        c.append(dataSet[s])  # ��������
        c.append(d)  # ���ǰ뾶
        c.append(int(dataSetOriginal[s][-1]))  # �������
        cov_num = 0  # �����е�������
        for i in range(len(I[t])):
            if I[t][i] == s:  # I[t][j]�Ǹ������ı���
                I1[t][i] = 1  # �������±�Ϊs���������Ϊ�Ѹ��ǣ���¼���Ǵ���
                cc.append(I[t][i])  # �����ǵ������±�ӵ�cc�б���
                cov_num += 1  # �����е���������һ
                continue  # ����ִ����һ��ѭ��
            if self.inner_product(dataSet[s][:-1], dataSet[I[t][i]][:-1]) >= d:  # �±�ΪI[t][i]�������ڸ��Ƿ�Χ֮��
                I1[t][i] = 1  # �������±�Ϊs���������Ϊ�Ѹ��ǣ���¼���Ǵ���
                cc.append(I[t][i])  # ���Ը��ǵ������±�ӵ�cc�б���
                cov_num += 1  # �����е���������һ
        c.append(cov_num)  # ������������
        cInfo.append(c)
        '''���渲����Ϣ'''
        if len(cc) == 1:  # д�븲����������Ϊ1��������Ҳ����Ҫ���������
            for i in cc:  # д��ɾ��������
                del_old.append(i)#ɾ�����ܸ���
                if dataSetOriginal[i][-1] == 0:  # ԭʼ�����е�������
                    del_old_min.append(i)
                else:
                    del_old_maj.append(i)  # ԭʼ�����еĶ�����
                for j in range(len(dataSetOriginal[i])):
                    if j < len(dataSetOriginal[i]) - 1:
                        fd.write(str(dataSetOriginal[i][j]) + ',')
                    else:
                        fd.write(str(int(dataSetOriginal[i][j])))
                fd.write('\n')





                # for j in range(len(dataSetOriginal[i])):
                #     if j < len(dataSetOriginal[i]) - 1:
                #         fd.write(str(dataSetOriginal[i][j]) + ',')
                #     else:
                #         fd.write(str(int(dataSetOriginal[i][j])))
                # fd.write('\n')
            # fd.write(str(dataSetOriginal[cc[0]][1:-1]) + '\n')
        else:
            for i in cc:  # д�����ձ�������������
                for j in range(len(dataSetOriginal[i])):
                    if j < len(dataSetOriginal[i]) - 1:
                        fw.write(str(dataSetOriginal[i][j]) + ',')
                    else:
                        fw.write(str(int(dataSetOriginal[i][j])))
                fw.write('\n')

    def My_cca(self, load_file, re_sampled_file, del_file,fcca,name):
        basi = Basic()
        dataSet_Original = basi.loadSample(load_file)  # ��������
        NormalData = self.Normalization(dataSet_Original)  # ��һ��
        unitData = self.Unitization(NormalData)  # ͶӰ
        fw = open(re_sampled_file, 'w')  # д�����մ������ļ�
        fd = open(del_file, 'w')  # д��ccaɾ����ԭʼ����
        I1, I = self.sorData(unitData)  # �Ƚ����������е��������򣬳�ʼ�����Ǳ��
        cInfo = list()  # [[��������],���ǰ뾶,�������,����������]
        del_old=list()#���ڴ洢����������У���ԭʼ���������
        del_old_maj = list()
        del_old_min = list()
        for t in I.keys():  # ѭ���������
            UnLearnedIdSet = I[t]  # ��I[t](t������)�е�������ȫ������UnLearnedIdSet
            while (len(UnLearnedIdSet)):
                cc = list()  # �����е��������
                s = random.choice(UnLearnedIdSet)  # ��UnLearnedIdSet�����ѡȡһ����������Ϊ��������
                self.computCover(t, s, I, I1, cc, cInfo, unitData, fw, fd,
                                 dataSet_Original,del_old,del_old_min,del_old_maj)  ##cc�Ǹ����У������ǵ�������ţ�cInfo�ǵõ��ĸ���
                UnLearnedIdSet = list(set(UnLearnedIdSet) ^ set(cc))  # ��UnLearnedIdSet��ɾ��cc���ѱ����ǵ������±�
        #[���������������Ŀ�����������Ŀ]
        fcca.write(name + ',')
        fcca.write(str(len(del_old)) + ',')
        fcca.write(str(len(del_old_maj)) + ',')
        fcca.write(str(len(del_old_min)) + '\n')
        fcca.close()
        fd.close()
        fw.close()
class Director:

    def run_dir(self, path_original, path_saveNew):

        pathdir_original = os.listdir(path_original)  # �г�ԭʼ�����ļ����µ��ļ������ļ�����
        for name in pathdir_original:#���ļ�������ѭ��
            if os.path.isfile(path_original + "\\" + name):#���name��һ���ļ������ﴫ���·�������Ǿ���·���ſ����ж�
                for i in range(m):#ѭ��������ÿһ�β�����������for_i�ļ�����
                    fcca = open(path_saveNew + '\\for_'+str(i+1)+"\\del_cca_info.csv",'a')
                    '''cca����ԭʼ���ݼ���Ŀ¼��recca��Ŀ¼��delcca��Ŀ¼'''
                    cca = CCA()
                    cca.My_cca(path_original + "\\" + name,#ԭʼcca������ļ�
                               path_saveNew+"\\for_"+str(i+1)+'\\re_CCA_' + name,#cca�ز���֮����ļ�
                               path_saveNew+"\\for_"+str(i+1)+'\\del_cca_' + name,#cca����ɾ�����ļ�
                               fcca,name)#���ڴ洢ɾ������Ϣ
#
            else:#���name��һ���ļ���
                path1 = path_original + "\\" + name#����ԭʼ���ݼ�·��
                os.mkdir(path_saveNew + "\\" + name)#������ԭʼ���ݼ��ļ���һ�µ��ļ��У����ڱ�������Ľ��
                path2 = path_saveNew + "\\" + name#���±������ݵ�·��Ϊ�´������ļ���
                for i in range(m):#������ļ����д������ÿһ��ѭ������������ļ���
                    os.mkdir(path2+"\\for_"+str(i+1))
                self.run_dir(path1, path2)#����ѭ�������ķ�����ѭ������


if __name__ == '__main__':
    based = Basic()
    # sm = Smote()
    # dataSet = based.loadSample('C:\\Users\Administrator\Desktop\Original_dataset - ����\EasyEnsemble\\abalone_0_7.csv')
    # # print(dataSet[0])
    # X, y = based.Split(dataSet)
    # print(type(X))
    # print(type(y))
    # sm.My_smote(X, y, 'C:\\Users\Administrator\Desktop\\test_dic\EasyEnsemble\\re_SMOTE_abalone_0_7.csv')
    # cca=CCA()
    # cca.My_cca('C:\\Users\Administrator\Desktop\\test_dic\EasyEnsemble\\re_SMOTE_abalone_0_7.csv',
    #            'C:\\Users\Administrator\Desktop\\test_dic\EasyEnsemble\\re_cca_abalone_0_7.csv',
    #            'C:\\Users\Administrator\Desktop\\test_dic\EasyEnsemble\\del_cca_abalone_0_7.csv')
    m=int(input("������ѭ��������"))
    path_original='E:\Papers_dataset\OriginalDataSet'
    path_saveNew='E:\Papers_dataset\ResempledDataSet\CCA_all'
    dic=Director()
    dic.run_dir(path_original,path_saveNew)
    toArff.run_dir(path_saveNew,'E:\Papers_dataset\ResempledDataSet\CCA_all_arff')
