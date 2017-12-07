import os
import re
import numpy as np
collec=list()
def aver(path):
    pathdir_original = os.listdir(path)
    for name in pathdir_original:  # 对文件名进行循环
        if os.path.isfile(path + "\\" + name):  # 如果name是一个文件，这里传入的路径必须是绝对路径才可以判断
            print("正在读取"+name+"中的文件")
            f=open(path + "\\" + name,'r')
            inData = f.readlines()  # 读取文件数据，以列表形式返回
            dataSet = list()  # 用于存储格式化之后的数据
            for line in inData:
                line = line.strip()  # 将line开头和结尾的空行去掉
                strList = re.split(r'[\s,\t]+', line)  # strList为返回的列表,列表中的元素为str类型
                '''将strList中的str类型的元素转换为float类型，方便计算'''
                numList = list()
                for item in strList[1:]:
                    num = float(item)
                    numList.append(num)
                dataSet.append(np.array(numList))
            collec.append(np.array(dataSet))
            f.close()
        else:
            path1=path+"\\"+name
            aver(path1)
if __name__ == '__main__':
    path="E:\Papers_dataset\Experiment\MWMOTE\\SMOTE+TonekLink"
    path_collec="E:\Papers_dataset\Experiment\MWMOTE\\SMOTE+TonekLink\\collec.csv"
    path_std="E:\Papers_dataset\Experiment\MWMOTE\\SMOTE+TonekLink\\std.csv"
    aver(path)
    geth=list()
    collec=np.array(collec)
    # print(collec)
    # print(collec[1].shape)
    a=np.zeros(collec[1].shape)
    b=np.zeros(collec[1].shape)
    print(a)
    # np.std()
    # sum=np.zeros((collec.shape,collec[0].shape))
    for i in range(1,len(collec)):
        a+=collec[i]
    a=a/(len(collec)-1)#均值
    fw=open(path_collec,'w')
    # fw.write(str(a))
    for i in range(len(a)):  # 写入最终保留下来的样本
        for j in range(len(a[i])):
            if j < len(a[i]) - 1:
                fw.write(str(a[i][j]) + ',')
            else:
                fw.write(str(a[i][j]))
        fw.write('\n')
    fw.close()
    for j in range(1,len(collec)):
        b+=(a-collec[j])**2
    std=np.sqrt(b/(len(collec)-1))

    fw=open(path_std,'w')
    for i in range(len(std)):  # 写入最终保留下来的样本
        for j in range(len(std[i])):
            if j < len(std[i]) - 1:
                fw.write(str(std[i][j]) + ',')
            else:
                fw.write(str(std[i][j]))
        fw.write('\n')
    fw.close()
    print(a[0][0])
    # print(std)
