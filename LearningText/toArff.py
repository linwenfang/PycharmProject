#coding=gbk
import re
import os

def run_dir(path_original, path_saveNew):
    pathdir_original = os.listdir(path_original)  # 列出原始样本文件夹下的文件名和文件夹名
    for name in pathdir_original:  # 对文件名进行循环
        if os.path.isfile(path_original + "\\" + name):  # 如果name是一个文件，这里传入的路径必须是绝对路径才可以判断
            if name[-5:]=='.arff':
                continue
            else:
                os.rename(path_original + "\\" + name,path_original + "\\" + name[:-4]+'.arff')# 改文件名
            '''读取文件'''
            f_r = open(path_original+ "\\" + name[:-4]+'.arff', 'r')
            inData = f_r.readlines()  # 读取文件数据，以列表形式返回
            numAttribute = len(re.split(r'[\s,\t]+', inData[0].strip()))  # 属性列的个数
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
            f_r.close()
            '''写入文件'''
            f_w = open(path_saveNew+ "\\" + name[:-4]+'.arff', 'w')
            '''arff格式写入'''
            f_w.write('% Title: ' + path_saveNew+ "\\" + name + '\n\n')
            f_w.write('@RELATION ' + path_saveNew+ "\\" + name + '\n\n')
            for i in range(numAttribute - 1):
                f_w.write('@ATTRIBUTE ' + str(i + 1) + ' NUMERIC\n')
            f_w.write('@ATTRIBUTE class {0,1}\n\n')
            f_w.write('@data\n')
            for i in range(len(dataSet)):  # 因为之前在第一行加了12345.。。所以要删去
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

        else:  # 如果name是一个文件夹
            path1 = path_original + "\\" + name  # 更新原始数据集路径
            os.mkdir(path_saveNew + "\\" + name)  # 创建和原始数据集文件夹一致的文件夹，用于保存采样的结果
            path2 = path_saveNew + "\\" + name  # 更新保存数据的路径为新创建的文件夹
            run_dir(path1, path2)  # 调用循环采样的方法，循环调用
if __name__ == '__main__':

    path_original="C:\\Users\Administrator\Desktop\\Original_dataset - 副本"
    path_saveNew="C:\\Users\Administrator\Desktop\\test_dic"
    run_dir(path_original,path_saveNew)