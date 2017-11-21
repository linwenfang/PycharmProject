#coding=gbk
import re
import os

def run_dir(path_original, path_saveNew):
    pathdir_original = os.listdir(path_original)  # �г�ԭʼ�����ļ����µ��ļ������ļ�����
    for name in pathdir_original:  # ���ļ�������ѭ��
        if os.path.isfile(path_original + "\\" + name):  # ���name��һ���ļ������ﴫ���·�������Ǿ���·���ſ����ж�
            if name[-5:]=='.arff':
                continue
            else:
                os.rename(path_original + "\\" + name,path_original + "\\" + name[:-4]+'.arff')# ���ļ���
            '''��ȡ�ļ�'''
            f_r = open(path_original+ "\\" + name[:-4]+'.arff', 'r')
            inData = f_r.readlines()  # ��ȡ�ļ����ݣ����б���ʽ����
            numAttribute = len(re.split(r'[\s,\t]+', inData[0].strip()))  # �����еĸ���
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
            f_r.close()
            '''д���ļ�'''
            f_w = open(path_saveNew+ "\\" + name[:-4]+'.arff', 'w')
            '''arff��ʽд��'''
            f_w.write('% Title: ' + path_saveNew+ "\\" + name + '\n\n')
            f_w.write('@RELATION ' + path_saveNew+ "\\" + name + '\n\n')
            for i in range(numAttribute - 1):
                f_w.write('@ATTRIBUTE ' + str(i + 1) + ' NUMERIC\n')
            f_w.write('@ATTRIBUTE class {0,1}\n\n')
            f_w.write('@data\n')
            for i in range(len(dataSet)):  # ��Ϊ֮ǰ�ڵ�һ�м���12345.��������Ҫɾȥ
                if i == -1:
                    continue
                else:
                    for j in range(len(dataSet[i])):
                        if j < len(dataSet[i]) - 1:
                            f_w.write(str(dataSet[i][j]) + ',')
                        else:
                            f_w.write(str(int(dataSet[i][j])))
                f_w.write('\n')
            f_w.close()

        else:  # ���name��һ���ļ���
            path1 = path_original + "\\" + name  # ����ԭʼ���ݼ�·��
            os.mkdir(path_saveNew + "\\" + name)  # ������ԭʼ���ݼ��ļ���һ�µ��ļ��У����ڱ�������Ľ��
            path2 = path_saveNew + "\\" + name  # ���±������ݵ�·��Ϊ�´������ļ���
            run_dir(path1, path2)  # ����ѭ�������ķ�����ѭ������
if __name__ == '__main__':

    path_original="C:\\Users\Administrator\Desktop\\Original_dataset - ����"
    path_saveNew="C:\\Users\Administrator\Desktop\\test_dic"
    run_dir(path_original,path_saveNew)