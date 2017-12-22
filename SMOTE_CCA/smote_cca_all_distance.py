# coding=gbk
from imblearn.over_sampling import SMOTE
import re
import numpy as np
import random
import os
from LearningText import toArff
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

    '''�����ݴ����np.array��ʽ'''

    def Split(self, dataSet):
        '''����һ��len(dataSet) x len(dataSet[0].split(','))-1�ľ���,���������Եĸ���'''
        features = np.zeros((len(dataSet), len(dataSet[0]) - 1))
        labels = []
        index = 0
        for line in dataSet:  # һ���ж������ļ�
            '''��line�е�ǰlen(line)-1�м��뵽������ȥ'''
            features[index:] = line[0:len(line) - 1]
            labels.append(line[-1])  # ���һ����Ϊ���
            index += 1
            '''���ص�featuresΪ��������labelsΪ����б�'''
        labels = np.array([int(x) for x in labels])
        return features, labels


class Smote:
    '''SMOTE������'''
    '''���ºϳ�������ԭʼ��������һ�����
    ������ºϳ����������Ϊ1
    �����ԭʼ���������Ϊ0'''


    def My_smote(self, X, y, re_filename):
        X_resampled = []
        y_resampled = []
        tab=[]#��ǩ
        X_res, y_res = SMOTE(kind='regular').fit_sample(X, y)  # SMOTE������
        # ���������Ľ�������numpy.ndarray��ʽ�����ҽ�y_resembledת����len(X_resemble)x1������
        X_resampled.append(X_res)
        y_resampled.append(y_res)
        X_resampled = X_resampled[0]
        y_resampled = y_resampled[0][:, np.newaxis]
        '''Ϊ�������ǩ'''
        for i in range(len(X_resampled)):
            if i < len(X):#ԭʼ���������Ϊ0
                tab.append(0)
            else:#�ºͳ����������Ϊ1
                tab.append(1)
        # '''��y_resembled��X_resembled�ϲ���ת����list����ʽ'''
        resampled = np.hstack((X_resampled, y_resampled)).tolist()
        # '''���ز������д���ļ���'''
        f = open(re_filename, 'w')
        for i in range(len(resampled)):
            for j in range(len(resampled[i])):
                if j < len(resampled[i]) - 1:
                    f.write(str(resampled[i][j]) + ',')
                else:
                    f.write(str(int(resampled[i][j])))
            f.write('\n')
        f.close()
        return tab


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

    def computCover(self, t, s, I, I1, cc, cInfo, dataSet,dataSetOriginal):
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
    def My_cca(self, load_file, re_sampled_file, del_old_file,del_new_file,f,tab,name):
        basi = Basic()
        dataSet_Original = basi.loadSample(load_file)  # ��������
        NormalData = self.Normalization(dataSet_Original)  # ��һ��
        unitData = self.Unitization(NormalData)  # ͶӰ
        fw = open(re_sampled_file, 'w')  # д�����մ������ļ�
        fd_old = open(del_old_file, 'w')  # д��ccaɾ����ԭʼ����
        fd_new=open(del_new_file,'w')#д��ccaɾ�����ºͳ�����
        I1, I = self.sorData(unitData)  # �Ƚ����������е��������򣬳�ʼ�����Ǳ��
        cInfo = list()  # [[��������],���ǰ뾶,�������,����������]
        del_old=list()#���ڴ洢����������У���ԭʼ���������
        del_new=list()#���ڴ洢����������У����ºͳɵ����������
        del_old_maj=list()
        del_old_min=list()
        del_new_maj=list()
        del_new_min=list()
        cc_list=list()
        cc_num_min=0
        cc_num_maj=0
        for t in I.keys():  # ѭ���������
            UnLearnedIdSet = I[t]  # ��I[t](t������)�е�������ȫ������UnLearnedIdSet
            while (len(UnLearnedIdSet)):
                cc = list()  # �����е��������
                s = random.choice(UnLearnedIdSet)  # ��UnLearnedIdSet�����ѡȡһ����������Ϊ��������
                self.computCover(t, s, I, I1, cc, cInfo, unitData,dataSet_Original)  ##cc�Ǹ����У������ǵ�������ţ�cInfo�ǵõ��ĸ���
                cc_list.append(cc)
                UnLearnedIdSet = list(set(UnLearnedIdSet) ^ set(cc))  # ��UnLearnedIdSet��ɾ��cc���ѱ����ǵ������±�
        '''********************************��**********************************'''

        '''ѭ��cc_list'''
        for i in range(len(cc_list)):
            if len(cc_list[i])==1:# ������ֻ��һ��������
                if dataSet_Original[cc_list[i][0]][-1] == 0:  # �������������������
                    cc_num_min += 1  # ������ֻ��һ�����������
        print("cc_num_min=",cc_num_min)
        '''ɾ��������'''
        for i in range(len(cc_list)):
            if len(cc_list[i])==1:#������ֻ��һ������
                if tab[cc_list[i][0]]==0:#ԭʼ�������Ϊ0
                    if dataSet_Original[cc_list[i][0]][-1]==1:#���ԭʼ�����Ƕ���������
                        cc_num_maj+=1
                        # del_old.append(cc_list[i][0])#ɾ����ԭʼ�����±�
                        del_old_maj.append(cc_list[i][0])#ɾ���Ķ����������±�
                        '''д��ɾ���Ķ�����'''
                        for j in range(len(dataSet_Original[cc_list[i][0]])):
                            if j < len(dataSet_Original[cc_list[i][0]]) - 1:
                                fd_old.write(str(dataSet_Original[cc_list[i][0]][j]) + ',')
                            else:
                                fd_old.write(str(int(dataSet_Original[cc_list[i][0]][j])))
                        fd_old.write('\n')
            if cc_num_maj == cc_num_min:
                print('cc_num_maj=',cc_num_maj)
                break
        '''ɾ��������'''
        for i in range(len(cc_list)):
            if len(cc_list[i])==1:#������ֻ��һ������
                if tab[cc_list[i][0]]==0:#ԭʼ�������Ϊ0
                    if dataSet_Original[cc_list[i][0]][-1]==0:#���ԭʼ����������������
                        # del_old.append(cc_list[i][0])
                        del_old_min.append(cc_list[i][0])
                        '''д��ɾ����ԭʼ����������'''
                        for j in range(len(dataSet_Original[cc_list[i][0]])):
                            if j < len(dataSet_Original[cc_list[i][0]]) - 1:
                                fd_old.write(str(dataSet_Original[cc_list[i][0]][j]) + ',')
                            else:
                                fd_old.write(str(int(dataSet_Original[cc_list[i][0]][j])))
                        fd_old.write('\n')
                else:#�ºϳ�����
                    '''ɾ���ºϳ�����������Ͷ�����'''
                    # del_new.append(cc_list[i][0])#ɾ�����ºϳɵ������±�
                    if dataSet_Original[cc_list[i][0]][-1]==0:#�ºϳɵ�����������
                        # del_new.append(cc_list[i][0])
                        del_new_min.append(cc_list[i][0])#ɾ�����ºͳɵ������������±�
                    else:
                        del_new_maj.append(cc_list[i][0])#ɾ�����ºͳɵĶ����������±�
                    '''д��ɾ�����ºϳ�����'''
                    for j in range(len(dataSet_Original[cc_list[i][0]])):
                        if j < len(dataSet_Original[cc_list[i][0]]) - 1:
                            fd_new.write(str(dataSet_Original[cc_list[i][0]][j]) + ',')
                        else:
                            fd_new.write(str(int(dataSet_Original[cc_list[i][0]][j])))
                    fd_new.write('\n')
        '''д�뱣������������'''
        del_list=del_old_maj+del_new_min+del_old_min+del_new_maj#ɾ���������±��б�
        print("del_old_maj=",len(del_old_maj))
        print("del_new_min=",len(del_new_min))
        print("del_old_min=",len(del_old_min))
        print("del_new_maj=",len(del_new_maj))

        ori_list=[i for i in range(len(dataSet_Original))]
        rew_list=list(set(ori_list).difference(set(del_list)))#��ori_list�е�Ԫ�أ�������del_list�е�Ԫ��
        for i in rew_list:
            for j in range(len(dataSet_Original[i])):
                    if j < len(dataSet_Original[i]) - 1:
                        fw.write(str(dataSet_Original[i][j]) + ',')
                    else:
                        fw.write(str(int(dataSet_Original[i][j])))
            fw.write('\n')
        '''д��smote+ccaɾ������Ϣ'''

        # [total,new,new_min,new_maj,old,old_min,old_maj]
        f.write(name+',')
        f.write(str(len(del_list))+',')
        f.write(str(len(del_new_min)+len(del_new_maj))+',')
        f.write(str(len(del_new_min)) + ',')
        f.write(str(len(del_new_maj)) + ',')
        f.write(str(len(del_old_min)+len(del_old_maj))+',')
        f.write(str(len(del_old_min)) + ',')
        f.write(str(len(del_old_maj)) + '\n')

        fd_new.close()
        fd_old.close()
        fw.close()
'''ѭ����β���'''
class Director:

    def run_dir(self, path_original, path_saveNew):
        # global f
        pathdir_original = os.listdir(path_original)  # �г�ԭʼ�����ļ����µ��ļ������ļ�����
        for name in pathdir_original:#���ļ�������ѭ��
            if os.path.isfile(path_original + "\\" + name):#���name��һ���ļ������ﴫ���·�������Ǿ���·���ſ����ж�
                dataSet = based.loadSample(path_original + "\\" + name)#�����ļ�����
                X, y = based.Split(dataSet)#����smote����
                for i in range(m):#ѭ��������ÿһ�β�����������for_i�ļ�����
                    f=open(path_saveNew + '\\for_'+str(i+1)+"\\del_smote_info.csv",'a')
                    sm=Smote()
                    tab=sm.My_smote(X, y, path_saveNew + '\\for_'+str(i+1)+'\\re_SMOTE_' + name)
                    '''cca����reamote��Ŀ¼��recca��Ŀ¼��delcca��Ŀ¼'''
                    cca = CCA()
                    cca.My_cca(path_saveNew+"\\for_"+str(i+1)+'\\re_SMOTE_' + name,#cca���������
                               path_saveNew+"\\for_"+str(i+1)+'\\re_SMOTE_CCA_' + name,#�ز���д�������
                               path_saveNew+"\\for_"+str(i+1)+'\\del_old_' + name,#ccaɾ�������������е�ԭʼ����
                               path_saveNew + "\\for_" + str(i + 1) + '\\del_new_' + name,#ccaɾ�������������е�smote�ϳɵ�����
                               f,#�����������Ϣ
                                tab,name)
                    f.close()

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
    path_saveNew='E:\Papers_dataset\ResempledDataSet\CCA_all_1'
    dic=Director()
    dic.run_dir(path_original,path_saveNew)
    toArff.run_dir(path_saveNew,'E:\Papers_dataset\ResempledDataSet\CCA_all_1_arff')
