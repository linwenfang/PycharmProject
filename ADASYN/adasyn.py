# coding=gbk
from imblearn.over_sampling import ADASYN
import numpy as np
import re
import os
from LearningText import toArff

# Generate the dataset
class Ada:
    def loadSample(self, path):
        file = open(path, 'r')
        '''��ȡ�ļ������ݣ�readlines���ص���һ���б�'''
        contain = file.readlines()
        count = len(contain)  # �����ļ�����count��
        '''����һ��count x len(contain[0].split(','))-1�ľ���,����len(contain[0].split(','))-1���������Եĸ���'''
        features = np.zeros((count, len(re.split(r'[ ,;:\t]+', contain[0])) - 1))
        labels = []
        index = 0
        for line in contain:  # һ���ж������ļ�
            line = line.strip()  # ɾ��lineͷ��β�Ŀո�
            listFormLine = re.split(r'[ ,;:\t]+', line)  # ָ��','Ϊ�ָ�������line�ָ
            '''��listFormLine�е�ǰlen(len(listFormLine)-1)�м��뵽������ȥ'''
            features[index:] = listFormLine[0:len(listFormLine) - 1]
            labels.append(listFormLine[-1])  # ���һ����Ϊ���
            index += 1
            '''���ص�featuresΪ��������labelsΪ����б�'''
        labels = np.array([int(x) for x in labels])
        file.close()
        return features, labels

    def write_resample(self, path, resampled):
        f = open(path, 'w')
        for i in range(len(resampled)):
            for j in range(len(resampled[i])):
                if j < len(resampled[i]) - 1:
                    f.write(str(resampled[i][j]) + ',')
                else:
                    f.write(str(resampled[i][j]))
            f.write('\n')
        f.close()

    def run_dir(self, path_original, path_saveNew):
        pathdir_original = os.listdir(path_original)  # �г�ԭʼ�����ļ����µ��ļ������ļ�����
        for name in pathdir_original:  # ���ļ�������ѭ��
            if os.path.isfile(path_original + "\\" + name):  # ���name��һ���ļ������ﴫ���·�������Ǿ���·���ſ����ж�
                X, y = self.loadSample(path_original + "\\" + name)  # �����ļ�����
                for i in range(m):  # ѭ��������ÿһ�β�����������for_i�ļ�����
                    X_resampled, y_resampled = ada.fit_sample(X, y)
                    y_resampled = y_resampled[:, np.newaxis]
                    resampled = np.hstack((X_resampled, y_resampled)).tolist()
                    self.write_resample(path_saveNew + '\\for_' + str(i + 1) + '\\re_ADASYN_' + name, resampled)
            else:  # ���name��һ���ļ���
                path1 = path_original + "\\" + name  # ����ԭʼ���ݼ�·��
                os.mkdir(path_saveNew + "\\" + name)  # ������ԭʼ���ݼ��ļ���һ�µ��ļ��У����ڱ�������Ľ��
                path2 = path_saveNew + "\\" + name  # ���±������ݵ�·��Ϊ�´������ļ���
                for i in range(m):  # ������ļ����д������ÿһ��ѭ������������ļ���
                    os.mkdir(path2 + "\\for_" + str(i + 1))
                self.run_dir(path1, path2)  # ����ѭ�������ķ�����ѭ������


if __name__ == '__main__':
    m = int(input("���������������"))
    path_originial = "E:\\Papers_dataset\\OriginalDataSet"  # ���ԭʼ�����ļ����ļ���
    path_saveNew = "E:\\Papers_dataset\\ResempledDataSet\\ADASYN"  # ����²���������ļ����ļ���
    ada_syn = Ada()
    ada = ADASYN()
    ada_syn.run_dir(path_originial, path_saveNew)  # ����ԭʼ���ݼ��ļ��кͱ����ز������ݼ��ļ��м���
    toArff.run_dir(path_saveNew,"E:\\Papers_dataset\\ResempledDataSet\\ADASYN_arff")
