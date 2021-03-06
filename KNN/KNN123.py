import math
import pprint
import re
import copy

def 计算欧氏距离(向量1,向量2):
    欧氏距离=0
    for i in range(len(向量1)):
        欧氏距离+=pow(向量1[i]-向量2[i],2)
    欧氏距离=math.sqrt(欧氏距离)
    # print(欧氏距离)
    return 欧氏距离

def 前k个排名(已分类字典,k):  #距离升序
    已分类列表=[[键,已分类字典[键]] for 键 in 已分类字典]
    for i in range(len(已分类列表)-1):
        if i>=k: break
        最小值对于序号=i
        最小值=已分类列表[i][1]
        for j in range(i+1,len(已分类列表)):
            if 最小值>已分类列表[j][1]:
                最小值=已分类列表[j][1]
                最小值对于序号=j
        if 最小值对于序号!=i:
            最小值=已分类列表[i][1]
            已分类列表[i][1]=已分类列表[最小值对于序号][1]
            已分类列表[最小值对于序号][1]=最小值
            最小值=已分类列表[i][0]
            已分类列表[i][0]=已分类列表[最小值对于序号][0]
            已分类列表[最小值对于序号][0]=最小值
    return 已分类列表

def KNN(所有向量,K=0,权值=0.5,距离算法=计算欧氏距离,动增上限=100,只算32个排名=False): #得分=1-权值/2+权值*(k-排名)/k  其中刚开始的k可能是比较小的
    '''
    K=0默认k取训练集的平方根,此时k是随训练集动态增加的。
    权值越大,越看重排在前面的样本的分类结果。权值=0则是普通的KNN,不管排哪里都只算多一个。
    '''
    if K>len(所有向量) or K<0:
        print('K值不能超过所有向量的个数范围!')
        return None
    #计算已分类字典
    已分类字典={} #格式为  {所有向量中的序号:距离得分,}
    for 第i词 in range(len(所有向量)):
        if 所有向量[第i词][2]!='':  #不为空的代表是一个已分类
            已分类字典.update([(第i词,0)])
    初始已分类字典=copy.deepcopy(已分类字典)
    初始已分类个数=len(已分类字典)
    #计算分类结果字典
    分类结果字典={}  #格式为  {所有可能的分类结果:总得分,}
    分类结果种类=[]
    for 键 in 已分类字典:
        分类结果种类.append(所有向量[键][2])
    分类结果种类=list(set(分类结果种类))
    for i in 分类结果种类:
        分类结果字典.update([(i,0)])
    print('分类结果种数=%d'%len(分类结果字典),end=',')
    #开始KNN
    for 第i词 in range(len(所有向量)):
        #已分过的不再分
        if 第i词 in 已分类字典: continue
        if 第i词%10==0:
            print(第i词)
        #分类结果字典全置0
        for 键 in 分类结果字典:
            分类结果字典[键]=0
        #计算这个词和所有已分类词的距离,输出到已分类字典
        if 只算32个排名:
            for 键 in 初始已分类字典:
                初始已分类字典[键]=距离算法(所有向量[第i词][1],所有向量[键][1])
        else:
            for 键 in 已分类字典:
                已分类字典[键]=距离算法(所有向量[第i词][1],所有向量[键][1])
        #取k
        if K==0:  #默认动态分配k
            k=int(math.sqrt(len(已分类字典)))
            if k>动增上限: k=动增上限
        elif len(已分类字典)>=K:
            k=K
        else:  #这种情况出现,可能说明类别不平等,导致结果全集中到某一类
            k=len(已分类字典)
        #已分类字典,距离得分排名
        if 只算32个排名:
            排序结果 = 前k个排名(初始已分类字典,k)
        else:
            排序结果 = 前k个排名(已分类字典,k)
        排序结果 = [i[0] for i in 排序结果]   #存的是所有向量中的序号
        #取前k个,计算相同分类结果的得分,输出到分类结果字典
        for 第i名 in range(len(排序结果)):
            if k<=第i名: break
            分类结果字典[所有向量[排序结果[第i名]][2]]+=1-权值/2+权值*(k-第i名)/k
        #分类结果字典,总得分排名
        排序结果 = sorted(分类结果字典.items(), key=lambda t: t[1], reverse=True)
        #取第一个分类结果名作为结果。如果出现多个总得分一样的,取的是最先在所有向量（按序号顺序）中出现的那个分类结果名
        所有向量[第i词][2]=排序结果[0][0]
        #第i词变成已分类
        已分类字典.update([(第i词,0)])
    print('所有向量个数=%d,初始已分类个数=%d,最后k=%d,权值=%f'
          %(len(所有向量),初始已分类个数,k,权值))
    return 所有向量

def 导入所有向量(地址):
    所有向量=[]
    读取=open(地址,'r',encoding='utf-8')
    原始数据=读取.readlines()
    读取.close()
    for 一行 in 原始数据:
        一行=re.subn('[\r\n]','',一行)[0].split('\t')
        一行[1]=一行[1].split(' ')
        一行[1]=[float(i) for i in 一行[1]]
        所有向量.append(一行)
    return 所有向量

def 导出分类结果(分类结果,输出地址):
    输出内容 = []
    for i in 分类结果:
        输出内容.append(i[0]+'\t'+i[2])
    写入 = open(输出地址, 'w', encoding='utf-8')
    写入.write('\r\n'.join(输出内容))
    写入.close()

# 所有向量的格式为  [['职位名',[200维向量值],'分类结果名'],[...],]  其中'分类结果名'刚开始只有32个不为空
所有向量=[['0',[18,24],''],
      ['1', [6,10], ''],
      ['2', [6,12], ''],
      ['3', [8,10], ''],
      ['4', [17,23], ''],
      ['5', [19,25], ''],
      ['6', [19,23], ''],
      ['7', [8,12], ''],
      ['8', [17,25], ''],
      ['9', [7,11], '2'],
      ['10', [14,18], '1'],]

所有向量=导入所有向量('职位名称_词向量.txt')
分类结果=KNN(所有向量,K=1,动增上限=100,只算32个排名=True)
# pprint.pprint(分类结果)
导出分类结果(分类结果,'职位名称_分为32类.txt')