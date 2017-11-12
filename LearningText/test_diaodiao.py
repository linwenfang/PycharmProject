
import re
f = open('RBPP2.txt', 'r')
f_w=open('diaodiao.txt','w')
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
for i in range(len(dataSet)):
    f_w.write(str(int(dataSet[i][-1])) + ' ')
    for j in range(len(dataSet[i])-1):
        f_w.write(str(j+1)+':'+str(dataSet[i][j])+' ')
    f_w.write('\n')
f_w.close()


