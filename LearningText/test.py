# # import random
# # player=input("请输入：剪刀（0），石头（1），布（2）：")
# # player=int(player)
# # computer=random.randint(0,2)
# # print("电脑=%d，用户=%d"%(computer,player))
# # if (player==0 and computer==1) or (player==1 and computer==2) or (player==2 and computer==0):
# #     print("用户获胜")
# # elif(player==computer):
# #     print("平局")
# # else:
# #     print("电脑获胜")
#
# # ==========================================================
# # i=1
# # while i<=5:
# #     j = 1
# #     while j<=i:
# #         print("*",end="")
# #         j+=1
# #     i=i+1
# #     print()
#
# # ==========================================================
# # i=1
# # while i <= 5:
# #     j=5
# #     while j>=i:
# #         print("*", end="")
# #         j -= 1
# #     i=i+1
# #     print()
#
# # ==========================================================
# # i = 1
# # while i <= 9:
# #     j = 1
# #     while j <= i:
# #         print("%d*%d=%d  " % (j, i, i * j), end='')
# #         j += 1
# #     print()
# #     i += 1
#
# # ==========================================================
# # for i in range(1,10):
# #     for j in range(1,10):
# #         if j<=i:
# #             print("%d*%d=%d  "%(j,i,j*i),end='')
# #     print()
#
# # ==========================================================
# # 一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配
# # import random
# # teacher=['A','B','C','D','E','F','G','H']
# # temp=[[],[],[]]
# # for name in teacher:
# #     index=random.randint(0,2)
# #     temp[index].append(name)
# # for i in temp:
# #     k=temp.index(i)+1
# #     print("办公室%d的人数为%d"%(k,len(i)))
# #     print("办公室的人分别为：")
# #     for j in i:
# #         print("%s"%j,end='')
# #     print()
# #     print("....................")
#
# # ==========================================================
# # # 提示信息
# # print("1、添加一个名字")
# # print("2、删除一个名字")
# # print("3、查找一个名字")
# # print("4、修改一个名字")
# # print("5、退出系统")
# # # 获取用户选择
# # names=[]
# # while True:
# #     print("="*20)
# #     num=int(input("请输入您的选择："))
# #     # 功能实现
# #     if num==1:
# #         names.append(input("请输入您要添加的名字："))
# #     elif num==2:
# #         flag=1
# #         while flag==1:
# #             print(names)
# #             name=input("请输入您要删除的名字：")
# #             if name not in names:
# #                 print("输入错误，请重新输入！")
# #                 flag=1
# #             else:
# #                 names.remove(name)
# #                 print("删除成功！")
# #                 flag=2
# #     elif num==3:
# #         name = input("请输入要查找的名字：")
# #         if name in names:
# #             print("查找成功！此同学的序号为：%d"%(names.index(name)+1))
# #         else:
# #             print("查找不成功！")
# #     elif num==4:
# #         print(names)
# #         name = input("请输入要修改的名字：")
# #         new_name=input("将此名字改为：")
# #         names[names.index(name)]=new_name
# #     elif num==5:
# #         break
# #     else:
# #         print("输入错误！请重新输入！")
#
# # ==========================================================
# # 打印提示
# # card_info=[]
# # def print_manu():
# #     print("1、添加一个新名片")
# #     print("2、删除一个新名片")
# #     print("3、修改一个新名片")
# #     print("4、查询一个新名片")
# #     print("5、显示所有名片")
# #     print("6、退出系统")
# # #用户选择
# # def add_card_info():
# #     new_info = {}
# #     new_name = input("请输入您的名字：")
# #     new_addr = input("请输入您的地址：")
# #     new_QQ = input("请输入您的QQ：")
# #     new_tel = input("请输入您的电话：")
# #
# #     new_info['name'] = new_name
# #     new_info['addr'] = new_addr
# #     new_info['QQ'] = new_QQ
# #     new_info['tel'] = new_tel
# #     global card_info
# #     card_info.append(new_info)
# # def del_card_info():
# #     global card_info
# #     del_name = input("请输入要删除名片的姓名：")
# #     flag = 0
# #     for temp in card_info:
# #         if temp['name'] == del_name:
# #             card_info.remove(temp)
# #             flag = 1
# #     if flag == 0:
# #         print("没有此人！")
# # def re_card_info():
# #     re_name = input("请输入要修改的名片姓名：")
# #     flag = 0
# #     for temp in card_info:
# #         if temp['name'] == re_name:
# #             flag = 1
# #             new_name = input("请输入修改后的姓名：")
# #             new_addr = input("请输入修改后的地址：")
# #             new_QQ = input("请输入修改后的QQ：")
# #             new_tel = input("请输入修改后的电话：")
# #             temp['name'] = new_name
# #             temp['addr'] = new_addr
# #             temp['QQ'] = new_QQ
# #             temp['tel'] = new_tel
# #     if flag == 0:
# #         print("输入错误！")
# # def sel_card_info():
# #     sel_name = input("请输入您要查询的姓名：")
# #     # flag=0
# #     for temp in card_info:
# #         if temp['name'] == sel_name:
# #             print(temp)
# #             # flag=1
# #             break
# #     # if flag==0:
# #     else:
# #         print("查无此人！")
# # print_manu()
# # while True:
# #     print("=" * 80)
# #     num = int(input("请输入您的选择："))
# # #功能实现
# #     if num ==1:
# #         add_card_info()
# #     elif num==2:
# #        del_card_info()
# #     elif num == 3:
# #         re_card_info()
# #     elif num == 4:
# #         sel_card_info()
# #     elif num==5:
# #         for temp in card_info:
# #             print("姓名：%s\t地址：%s\tQQ：%s\t电话：%s\t"%(temp['name'],temp['addr'],temp['QQ'],temp['tel']))
# #     elif num == 6:
# #         break
# #     else:
# #         print("输入错误！请重新输入！")
#
# # ==========================================================
# # dict={"name":"liu","sex":"m"}
# # for key,value in dict.items():
# #     print(key,value)
# # for i in enumerate(dict):
# #     print(i)
#
# # ==========================================================
# # 1. 编程实现对一个元素全为数字的列表，求最大值、最小值
# # a=[11,1,2,55,58,96,3,769,966,556,0,-1,-99]
# # print("最大值为%d"%max(a))
# # print("最小值为%d"%min(a))
# # 2. 编写程序，完成以下要求：
# #
# # 统计字符串中，各个字符的个数
# # 比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1
# # a="hello word"
# # for i in a:
# #     print("%s\t%d"%(i,a.count(i)))
#
# # ==========================================================
# # def get_wendu():
# #     wendu =22
# #     print(wendu)
# #     # 如果没有return，则没有返回值类型
# #     return wendu
# # def get_wendu2(wendu):
# #     wendu =wendu +2
# #     print(wendu)
# # result =get_wendu()
# # get_wendu2(result)
#
# # == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# # 不熟练的地方
#
# # def fun(a,b,*args,**kwargs):
# #     print("a=",a)
# #     print("b=",b)
# #     print("*args=",args)
# #     print("**kwargs=")
# #     for key,value in kwargs.items():
# #         print(key,"=",value)
# # fun(1, 2, 3, 4, 5, m=6, n=7, p=8)
# # print("*"*80)
# # c = (3, 4, 5)
# # d = {"m":6, "n":7, "p":8}
# # fun(1,2,3,*c,**d)
# # print("*"*80)
# # fun(1,2,3,c,d)
#
#
# # **************************************************************
# # def culNum(num):
# #     if num>=1:
# #         result=num*culNum(num-1)
# #     else:
# #         result=1
# #     return result
# # ret=culNum(4)
# # print(ret)
#
# # == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# # 不熟悉的地方
# # def fun(a,b,opt):
# #     print("a=",a)
# #     print("b=", b)
# #     result=opt(a,b)
# #     print(result)
# # fun (2,3,lambda x,y:x+y)
#
# # == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# # python 动态语言特点体现，
# # def dynamic(a,b,func):
# #     print("a=",a)
# #     print("b=",b)
# #     result=func(a,b)
# #     print(result)
# # new_func=input("请输入一个匿名函数：")
# # new_func=eval(new_func)#eval   去掉字符串的两边的引号，该是什么函数就是什么函数
# # dynamic(11,12,new_func)
#
# # == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# # 交换两个变量的值
# # a=5
# # b=9
# # a=a+b
# # b=a-b
# # a=a-b
# # print(a)
# # print(b)
#
# # == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# # 对比num+=num与num=num+num的区别
# # def selfAdd_1(a):
# #     a+=a
# #     return a
# # a_int=1
# # print(selfAdd_1(a_int))#整型变量是不可修改的
# # print(a_int)
# #
# # def selfAdd_2(b):
# #     b=b+b
# #     return b
# # b_int=1
# # print(selfAdd_2(b_int))#整型变量是不可修改的
# # print(b_int)
# #
# #
# # # 重点来啦
# # a_list = [1, 2]
# # b_list=[1,2]
# # '''在a+=a中，从一开始修改的就是a指向的那个值，所以最后指向的那个值也会变'''
# # print(selfAdd_1(a_list))
# # print(a_list)
# # '''在a=a+a中，结果是使a指向a+a这个值，而原来参数的值是不变的'''
# # print(selfAdd_2(b_list))
# # print(b_list)
#
# # == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# # a=[]
# # b=[]
# # for i in range(100,201):
# #     for j in range(2,i):
# #         if i%j==0:
# #             a.append(i)
# #             # print(i)
# #             break
# # for i in range(100,201):
# #     b.append(i)
# # for i in a:
# #     b.remove(i)
# # print(b)
#
#
# # == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# # 用函数实现输入某年某月某日，判断这一天是这一年的第几天？闰年情况也考虑进去
# # import datetime
# #
# # y = int(input('请输入4位数字的年份：'))  # 获取年份
# # m = int(input('请输入月份：'))  # 获取月份
# # d = int(input('请输入是哪一天：'))  # 获取“日”
# #
# # targetDay = datetime.date(y, m, d)  # 将输入的日期格式化成标准的日期
# # dayCount = targetDay - datetime.date(targetDay.year - 1, 12, 31)  # 减去上一年最后一天
# # print('%s是%s年的第%s天。' % (targetDay, y, dayCount.days))
# #
#
#
# # == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# # f = open('text.txt', 'w')
# # f.write('hello world, i am here!')
# # f.close()
# #
# #
# # f = open('text.txt', 'r')
# # content = f.read(5)
# # print(content)
# # print("= "*30)
# # content = f.read()
# # print(content)
# # f.close()
# #
# # f = open('test.txt', 'r')
# #
# # content = f.readlines()
# #
# # print(type(content))
# #
# # i=1
# # for temp in content:
# #     print("%d:%s"%(i, temp))
# #     i+=1
# #
# # f.close()
# #
# # f = open('test.txt', 'r')
# #
# # content = f.readline()
# # print("1:%s"%content)
# #
# # content = f.readline()
# # print("2:%s"%content)
# #
# #
# # f.close()
#
#
# # == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# # 拷贝文件
# # old_file_name=input("请输入要打开的文件名：")
# # f_read=open(old_file_name,'r')
# # position=old_file_name.rfind(".")
# # new_file_name=old_file_name[0:position]+"附件"+old_file_name[position:]#复制以后的文件名
# #
# # f_write=open(new_file_name,'w')
# # while True:
# #     content=f_read.read(1024)#大文件复制时应注意
# #     if len(content)==0:
# #         break
# #     f_write.write(content)
# # f_write.close()
# # f_read.close()
#
# # == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
#
#
# # f_loca=open('test.txt','r')
# # str=f_loca.read(9)
# # print("当前读取的数据是",str)
# # position = f_loca.tell()
# # print ("当前文件位置 : ", position)
# #
# # f_loca.seek(0,0)
# # str=f_loca.read(5)
# # print("当前读取的数据是",str)
# # position = f_loca.tell()
# # print ("当前文件位置 : ", position)
# #
# # f_loca.seek(5,1)#出错的地方
# # str=f_loca.read(5)
# # print("当前读取的数据是",str)
# # position = f_loca.tell()
# # print ("当前文件位置 : ", position)
#
# # == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# # class car:
# #     def __init__(self,newwheelnum,newcolor):
# #         self.wheelnum=newwheelnum
# #         self.color=newcolor
# #     # 移动
# #     def move(self):
# #         print('车在奔跑...')
# #
# #     # 鸣笛
# #     def toot(self):
# #         print("车在鸣笛...嘟嘟..")
# #
# #
# # BMW=car(4,'green')
# # AUDI=car(4,'red')
# # print("BMW：颜色%s轮子%d"%(BMW.color,BMW.wheelnum))
# # print("AUDI：颜色%s轮子%d"%(AUDI.color,AUDI.wheelnum))
# # print(BMW)
#
#
# # == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# # 示例属性如下:
#
# # cookedLevel : 这是数字；0~3表示还是生的，超过3表示半生不熟，超过5表示已经烤好了，超过8表示已经烤成木炭了！我们的地瓜开始时时生的
# # cookedString : 这是字符串；描述地瓜的生熟程度
# # condiments : 这是地瓜的配料列表，比如番茄酱、芥末酱等
# # 示例方法如下:
# #
# # cook() : 把地瓜烤一段时间
# # addCondiments() : 给地瓜添加配料
# # __init__() : 设置默认的属性
# # __str__() : 让print的结果看起来更好一些
#
#
# # class SweetPotato:
# #     def __init__(self):#初始状态
# #         self.cookedLeval=0
# #         self.cookedString="生的"
# #         self.condiments=[]
# #     def __str__(self):
# #         return "地瓜  状态  %s(%d)  添加的佐料有%s"%(self.cookedString,self.cookedLeval,str(self.condiments))
# #     def cook(self,time):
# #         self.cookedLeval+=time
# #         if self.cookedLeval>8:
# #             self.cookedString="烤成碳了"
# #         elif self.cookedLeval>5:
# #             self.cookedString="烤好了"
# #         elif self.cookedLeval>3:
# #             self.cookedString="半生不熟"
# #         else:self.cookedString="生的"
# #     def AddCondiments(self,condiment):
# #         self.condiments.append(condiment)
# #
# # mySweetPotato = SweetPotato()
# # print("------有了一个地瓜，还没有烤-----")
# # print(mySweetPotato.cookedLeval)
# # print(mySweetPotato.cookedString)
# # print(mySweetPotato.condiments)
# # print("------接下来要进行烤地瓜了-----")
# # print("------地瓜经烤了4分钟-----")
# # mySweetPotato.cook(4) #烤4分钟
# # print(mySweetPotato)
# # print("------地瓜又经烤了3分钟-----")
# # mySweetPotato.cook(3) #又烤了3分钟
# # print(mySweetPotato)
# # print("------接下来要添加配料-番茄酱------")
# # mySweetPotato.AddCondiments("番茄酱")
# # print(mySweetPotato)
# # print("------地瓜又经烤了5分钟-----")
# # mySweetPotato.cook(5) #又烤了5分钟
# # print(mySweetPotato)
# # print("------接下来要添加配料-芥末酱------")
# # mySweetPotato.AddCondiments("芥末酱")
# # print(mySweetPotato)
#
#
# # == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# # class Home:
# #     def __init__(self,area,addr,info):
# #         self.arae=area
# #         self.addr=addr
# #         self.info=info
# #         self.left_area=area
# #         self.contains=[]
# #     def __str__(self):
# #         mag= "房子的总面积是%d,房子的地址在%s,房子的类型是%s,房子的剩余面积是%d,"%(self.arae,self.addr,self.info,self.left_area)
# #         mag+="房子里的东西%s"%(str(self.contains))
# #         return mag
# #     def add_item(self,item):
# #         self.left_area-=item.get_area()
# #         self.contains.append(item.get_name)
# # class Bed:
# #     def __init__(self,area,info):
# #         self.area=area
# #         self.info=info
# #     def __str__(self):
# #         return "床的总面积是%d  床的类型是%s" % (self.area,  self.info)
# #     def get_area(self):
# #         return self.area
# #     def get_name(self):
# #         return self.info
# # FangZi=Home(300,"淮南","别墅")
# # print(FangZi)
# # Bed1=Bed(4,"双人床")
# # print(Bed1)
# # FangZi.add_item(Bed1)
# # print(FangZi)
#
#
# # == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# # 创建单例时，只执行1次__init__方法
# # class Dog(object):
# #     __instance=None
# #     __init_flag=False
# #
# #     def __init__(self,name):
# #         if Dog.__init_flag==False:
# #             Dog.__init_flag=True
# #             self.name=name
# #
# #     def __new__(cls,name):
# #         if cls.__instance==None:
# #             cls.__instance=object.__new__(cls)
# #             return cls.__instance
# #         else:
# #             return cls.__instance
# #
# # a=Dog("旺财")
# # print(id(a))
# # print(a.name)
# #
# # b=Dog("哮天犬")
# # print(id(b))
# # print(b.name)
# #
# # == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# # 实现分组一个 list 里面的元素,比如 [1,2,3,...100]变成 [[1,2,3],[4,5,6]....]
# # a = [x for x in  range(1,101)]
# # b = [a[x:x+3] for x in range(0,len(a),3)]
# #
# # print(b)
# #
# # print(a[0:3])
#
#
# # == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# # L1 = ['Hello', 'World', 18, 'Apple', None]
# # L2=[]
# # for s in L1:
# #     if isinstance(s,str):
# #         L2.append(s)
# # print(L2)
#
# # == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# # [1]
# # [1, 1]
# # [1, 2, 1]
# # [1, 3, 3, 1]
# # [1, 4, 6, 4, 1]
# # [1, 5, 10, 10, 5, 1]
# # [1, 6, 15, 20, 15, 6, 1]
# # [1, 7, 21, 35, 35, 21, 7, 1]
# # [1, 8, 28, 56, 70, 56, 28, 8, 1]
# # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# # def triangels():
# #     L=[1]                                                                 #定义一个list[1]
# #     while True:
# #         yield L                                                           #打印出该list
# #         L=[L[x]+L[x+1] for x in range(len(L)-1)]        #计算下一行中间的值（除去两边的1）
# #         L.insert(0,1)                                                 #在开头插入1
# #         L.append(1)                                                 #在结尾添加1
# #         if len(L)>10:                                                 #仅输出10行
# #             break
# # n = 0
# # for t in triangels():
# #     print(t)
# #     n = n + 1
# #     if n == 10:
# #         break
# # =======================================================================================================================
# # it=iter([1,2,5,4,8,9,52,68,12,-2])
# # while True:
# #     try:
# #         print(next(it))
# #     except StopIteration:
# #         break
# # =======================================================================================================================
# # from functools import reduce
# # def str2float(s):       # 将小数字符串转化为浮点数
# #     def plus1(x, y):
# #         return x * 10 + y
# #     def plus2(x, y):
# #         return x * 0.1 + y
# #     def char2num(c):
# #         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
# #
# #     dot = s.index('.')
# #     return reduce(plus1, map(char2num, s[:dot])) + 0.1 * reduce(plus2, map(char2num, s[dot+1:]))
# # print('str2float(\'123.456\') =', str2float('123.456'))
# # =======================================================================================================================
# # from functools import reduce
# # def prod(L):
# #     return reduce((lambda x,y:x*y),L)
# # print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# # =======================================================================================================================
# # 过滤掉非回数
# # def is_palindrome(n):
# #     return str(n)[::-1] == str(n)
# # output = filter(is_palindrome, range(1, 1000))
# # print(list(output))
# # =======================================================================================================================
# # L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# # print(sorted(L,key=lambda x:x[0]))
# # print(sorted(L,key=lambda x:x[1]))
# # =======================================================================================================================
# # import urllib.request
# # response=urllib.request.urlopen("http://www.baidu.com")
# # print(response.read())
# # =======================================================================================================================
# # class screen(object):
# #     @property
# #     def weight(self):
# #         return self._weight
# #     @property
# #     def height(self):
# #         return self._height
# #     @weight.setter
# #     def weight(self,weight1):
# #         if weight1>0:
# #             self._weight=weight1
# #         else:print("weight must be >0")
# #     @height.setter
# #     def height(self,height1):
# #         if height1>0:
# #             self._height=height1
# #         else:print("height must be >0")
# #         '''只读属性'''
# #     @property
# #     def resolusion(self):
# #         return self._weight*self._height
# # s=screen()
# # s.height=100
# # s.weight=50
# # print(s.resolusion)
# # #=======================================================================================================================
# # from enum import Enum
# # Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# # for name, member in Month.__members__.items():
# #     print(name, '=>', member, ',', member.value)
#
# # #=======================================================================================================================
# # '''正则表达式匹配邮箱'''
# # import re
# # n=re.match(r'^(\w*)(\@)(\w*)\.(\w*)$','soneone@gmail.com')
# # print(n.groups())
# # #=======================================================================================================================
# # from datetime import datetime
# # print(datetime.fromtimestamp(datetime.now().timestamp()))
# # from collections import namedtuple
# # point=namedtuple('liu',['x','y'])
# # p=point(1,2)
# # print(p.y)
# # #=======================================================================================================================
# # #=======================================================================================================================
# # 抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应
# # from urllib import request
# #
# # with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
# #     data = f.read()
# #     print('Status:', f.status, f.reason)
# #     for k, v in f.getheaders():
# #         print('%s: %s' % (k, v))
# #     print('Data:', data.decode('utf-8'))
# # #=======================================================================================================================
# # #=======================================================================================================================
# # 模拟iphone返回GET请求
#
# # from urllib import request
# #
# # req = request.Request('http://www.douban.com/')
# # req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# # with request.urlopen(req) as f:
# #     print('Status:', f.status, f.reason)
# #     for k, v in f.getheaders():
# #         print('%s: %s' % (k, v))
# #     print('Data:', f.read().decode('utf-8'))
# # #=======================================================================================================================
# # #=======================================================================================================================
# # 模拟微博登录
# # from urllib import request, parse
# # print('Login to weibo.cn...')
# # email = input('Email: ')
# # passwd = input('Password: ')
# # login_data = parse.urlencode([
# #     ('username', email),
# #     ('password', passwd),
# #     ('entry', 'mweibo'),
# #     ('client_id', ''),
# #     ('savestate', '1'),
# #     ('ec', ''),
# #     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# # ])
# # req = request.Request('https://passport.weibo.cn/sso/login')
# # req.add_header('Origin', 'https://passport.weibo.cn')
# # req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# # req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
# #
# # with request.urlopen(req, data=login_data.encode('utf-8')) as f:
# #     print('Status:', f.status, f.reason)
# #     for k, v in f.getheaders():
# #         print('%s: %s' % (k, v))
# #     print('Data:', f.read().decode('utf-8'))
# # #=======================================================================================================================
# # #=======================================================================================================================
# # # 生成随机验证码
# # from PIL import Image, ImageDraw, ImageFont, ImageFilter
# #
# # import random
# #
# #
# # # 随机字母:
# # def rndChar():
# #     return chr(random.randint(65, 90))
# #
# #
# # # 随机颜色1:
# # def rndColor():
# #     return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# #
# #
# # # 随机颜色2:
# # def rndColor2():
# #     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
# #
# #
# # # 240 x 60:
# # width = 60 * 4
# # height = 60
# # image = Image.new('RGB', (width, height), (255, 255, 255))
# # # 创建Font对象:
# # font = ImageFont.truetype('/Library/Fonts/arial.ttf', 36)
# # # 创建Draw对象:
# # draw = ImageDraw.Draw(image)
# # # 填充每个像素:
# # for x in range(width):
# #     for y in range(height):
# #         draw.point((x, y), fill=rndColor())
# # # 输出文字:
# # for t in range(4):
# #     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# # # 模糊:
# # image = image.filter(ImageFilter.BLUR)
# # image.save('code.jpg', 'jpeg')
# # #=======================================================================================================================
# # #=======================================================================================================================
# # from tkinter import *
# # import tkinter.messagebox as messagebox
# # '''在GUI中，每个Button、Label、输入框等，都是一个Widget。
# # Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
# # pack()方法把Widget加入到父容器中，并实现布局。
# # pack()是最简单的布局，grid()可以实现更复杂的布局。
# # 在createWidgets()方法中，我们创建一个Label，两个Button，一个文本框。当Quit被点击时，触发self.quit()使程序退出，
# # 当hello被点击时，触发self.hello(),显示message界面'''
# # class Application(Frame):
# #     def __init__(self,master=None):
# #         Frame.__init__(self,master)
# #         self.pack()
# #         self.createWidgets()
# #     def createWidgets(self):
# #         self.nameInput=Entry(self)
# #         self.nameInput.pack()
# #         self.helloLabel=Label(self,text='hello world')
# #         self.helloLabel.pack()
# #         self.helloButton=Button(self,text='hello',command=self.hello)
# #         self.helloButton.pack()
# #         self.quitButton=Button(self,text='Quit',command=self.quit)
# #         self.quitButton.pack()
# #     def hello(self):
# #         name=self.nameInput.get() or 'world'
# #         messagebox.showinfo('Message','Hello %s'%name)
# # if __name__ == '__main__':
# #     app=Application()
# #     '''设置窗口标题'''
# #     app.master.title='liuruiqing'
# #     '''主程序循环'''
# #     app.mainloop()
# # #=======================================================================================================================
# # #=======================================================================================================================
# # import re
# # from numpy import *
# #
# # file = open("iris.txt", 'r')
# # '''读取文件的内容，readlines返回的是一个列表'''
# # contain = file.readlines()
# # random.shuffle(contain)
# # count = len(contain)  # 这是文件共有count行
# #
# # for i in range(count):
# #     if i >=int(count*0.8) :
# #         f = open("TestData1.txt", 'a+')
# #         f.write(contain[i])
# #     else:
# #         f=open("TrainingData1.txt",'a+')
# #         f.write(contain[i])
# # #=======================================================================================================================
# # class Person(object):
# #     def __init__(self, name, age, taste):
# #         self.name = name
# #         self._age = age
# #         self.__taste = taste
# #
# #     def showperson(self):
# #         print(self.name)
# #         print(self._age)
# #         print(self.__taste)
# #
# #     def dowork(self):
# #         self._work()
# #         self.__away()
# #
# #     def _work(self):
# #         print('my _work')
# #
# #     def __away(self):
# #         print('my __away')
# #
# #
# # class Student(Person):
# #     def construction(self, name, age, taste):
# #         self.name = name
# #         self._age = age
# #         self.__taste = taste
# #
# #     def showstudent(self):
# #         print(self.name)
# #         print(self._age)
# #         print(self.__taste)
# #
# #     @staticmethod
# #     def testbug():
# #         _Bug.showbug()
# #
# #
# # # 模块内可以访问，当from  cur_module import *时，不导入
# # class _Bug(object):
# #     @staticmethod
# #     def showbug():
# #         print("showbug")
# #
# #
# # s1 = Student('jack', 25, 'football')
# # s1.showperson()
# # s1.dowork()
# # print('*' * 20)
# #
# # # 无法访问__taste,导致报错
# # # s1.showstudent()
# # s1.construction('rose', 30, 'basketball')
# # s1.showperson()
# # print('*' * 20)
# # #
# # # s1.showstudent()
# # # print('*' * 20)
# # #
# # Student.testbug()
# # #=======================================================================================================================
# # #======================================================================================================
# # from time import *
# #
# #
# # def w1pre(pre="hello"):
# #     def w1(func):
# #         print("------装饰器1正在装饰------")
# #
# #         def inner1(*args, **kwargs):
# #             print("%s called at %s,%s" % (func.__name__, ctime(), pre))
# #             print("--------验证权限1--------")
# #             ret = func(*args, **kwargs)
# #             return ret
# #
# #         return inner1
# #
# #     return w1
# #
# #
# # def w2(func):
# #     print("------装饰器2正在装饰------")
# #
# #     def inner2(*args, **kwargs):
# #         print("%s called at %s" % (func.__name__, ctime()))
# #         print("--------验证权限2--------")
# #         ret = func(*args, **kwargs)
# #         return ret
# #
# #     return inner2
# #
# #
# # # w1pre(pre="hahaha"),返回的是w1的引用。然后再执行@w1对函数进行装饰
# # @w1pre(pre="hahaha")
# # @w2#@w2相当于f1=w2(f1)即将f1的引用赋值给w1中的func
# # def f1(a, b):
# #     print("------正在执行f1------")
# #     print("a=%d,b=%d" % (a, b))
# #     print("a+b=", a + b)
# #     return a * b
# #
# #
# # @w2
# # def f2():
# #     print("------正在执行f2------")
# #
# #
# # print("---------------------------------")
# # ret = f1(2, 3)
# # print(ret)
# # print("---------------------------------")
# # f2()
# # =======================================================================================================================
# # #====#=======================================================================================================================
# # #====
# # 给对象绑定属性
# # class person(object):
# #     def __init__(self,name,age):
# #         self.name=name
# #         self.age=age
# #     def eat(self):
# #         print("eat food")
# # def run (self,speed):
# #     print("%s在以%d公里每秒的速度奔跑"%(self.name,speed))
# #
# # p1=person("ming",24)
# # p1.sex="male"#给实例对象p1添加sex属性，但是在person类中并没有这个属性
# # #给person类添加属性
# # person.sex="male"#默认sex=male
# # #给类绑定方法
# # import types
# # p1.run=types.MethodType(run,p1)
# # print(p1.run(50))
# # #====#=======================================================================================================================
# # def creatNum():
# #     print("-------start-------")
# #     a,b=0,1
# #     for i in range(6):
# #         print("-------1-------")
# #         yield b#程序执行停止，返回值b
# #         print("-------2-------")
# #         a,b,=b,a+b
# #         print("-------3-------")
# #     print("-------stop------")
# #
# # c=creatNum()
# # #取生成器的值，可以用for循环，next(a),a.__next__
# # print(next(c))
# # print(next(c))
# # print(next(c))
# # print(next(c))
# # print(next(c))
# # print(next(c))
# # #====#=======================================================================================================================
# # '''创建udp客户端程序'''
# # import socket
# # #socket.socket()创建套接字有两个参数，
# # # 第一个参数有两个选择：socket.AF_INET(用于interne进程间通信)
# # #socket.AF_UNIX(用于同一台机器进程间通信)
# # #第二个参数也有两个选择：socket.SOCK_STREAM(用于TCP协议)
# # #socket.SOCK_DGRAM(用于UDP协议)
# # #1、创建套接字
# # udpsocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # #2、准备接收方地址
# # sendAddr=('172.23.8.242',4000)
# # #3、从键盘获取数据
# # # sendData=input("请输入要发送的数据：")
# # #绑定发送方的端口号
# # # udpsocket.bind(("",7777))#ip地址可以不填
# # #4、发送数据到指定电脑
# # udpsocket.sendto(b'1:123456:user:pc:32:hello',sendAddr)
# # #5、等待接收方回应recvData为接收到的数据
# # recvData=udpsocket.recvfrom(1024)#1024表示本次接收的最大字节数
# # #6、关套接字
# # udpsocket.close()
# # #====#=======================================================================================================================
# # import re
# # ret=re.match(r"c:\\a","c:\\a\\\d")
# # print(ret.group())
# #
# # ret1=re.match(r"[a-zA-Z\s]{6,}","liu rui qing")
# # print(ret1.group())
# #
# # ret2=re.match(r"[\w]{4,20}@163\.com$","hello@163.com")
# # print(ret2.group())
# #
# # ret3=re.match(r"ho\s\bver\b", "ho ver abc")
# # print(ret3.group())
# #
# # ret4=re.match(r"^\w+ve","hover")
# # print(ret4.group())
# #
# # ret5=re.match(r"[1-9]?\d$|100","100")
# # print(ret5.group())
# #
# # ret6=re.match(r"<(\w*)><(\w*)>.*<(/\2)><(/\1)>","<htl><h1>www.itcast.cn</h1></htl>")
# # print(ret6.group())
# #
# # ret7=re.sub(r"\d+","999","python=997")
# # print(ret7)
# #
# # s="This is a number 234-235-22-423"
# # r=re.match(".+(\d+-\d+-\d+-\d+)",s)
# # print(r.group())
# #
# # t="""<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg"
# # src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">"""
# # tl=re.sub(r".+?(https:.+?\.jpg).+",lambda x : x.group(1),t)
# # # tl=re.search(r".+?(https:.+?\.jpg).+",t)
# # # tl=re.search(r"https.+?\.jpg",t)
# # print(tl)
# #
# # p="""http://www.interoem.com/messageinfo.asp?id=35
# # http://3995503.com/class/class09/news_show.asp?id=14
# # http://lib.wzmc.edu.cn/news/onews.asp?id=769
# # http://www.zy-ls.com/alfx.asp?newsid=377&id=6
# # http://www.fincm.com/newslist.asp?id=415"""
# # p1=re.sub(r"(http://.+?/).+",lambda x : x.group(1),p)#sub替换
# # print("p1=",p1)
# #
# # q="hello world ha ha"
# # # q1=re.match(r"(.+?\s)+.+",q)
# # q1=re.findall(r"\b[a-zA-Z]+\b",q)
# # print(q1)
#
# # #====#=======================================================================================================================
# # import re
# # import numpy as np
# # f = open("pendigits.txt", 'r')
# # inData = f.readlines()
# # dataSet = list()
# # for line in inData:
# #     line = line.strip()
# #     strList = re.split(r'[\s,\t]+', line)
# #     numList = list()
# #     for item in strList:
# #         num = float(item)
# #         numList.append(num)
# #     dataSet.append(numList)
# # f.close()
# # # print(dataSet)
# # vec_Max = list()
# # vec_Min = list()
# # maxValue = -1
# # minValue = 999999
# # dataSet = np.array(dataSet)
# # for j in range(len(dataSet[0]) - 1):  # lie
# #     for i in range(len(dataSet)):  # hang
# #         if dataSet[i][j] < minValue:
# #             minValue = dataSet[i][j]
# #         if dataSet[i][j] > maxValue:
# #             maxValue = dataSet[i][j]
# #     vec_Max.append(maxValue)
# #     vec_Min.append(minValue)
# # for j in range(len(dataSet[0]) - 1):  # lie
# #     for i in range(len(dataSet)):  # hang
# #         if vec_Max[j] - vec_Min[j] < 1e-6:
# #             dataSet[i][j] = 0
# #         else:
# #             dataSet[i][j] = (dataSet[i][j] - vec_Min[j]) / (vec_Max[j] - vec_Min[j])
# # # print(dataSet)
# # # dataSet = splitDataSet(dataSet)
# # features = list()
# # for i in dataSet:#hang
# #     features.append(i[0:len(i)])
# # # print(features)
# # dataSet = features
# # for i in range(len(dataSet)):
# #     dataSet[i] = list(dataSet[i])
# # l=[1,2,3,4,5]
# # p=[5,1]
# # print(list(set(l)^set(p)))
# # #====#=======================================================================================================================
# # !/usr/bin/env Python
# # coding=utf-8
#
# # url解码，编码，基本的读取网页功能
# # url="http://www.baidu.com/s"
# # key_word=input("请输入查询关键字：")
# # wd={"wd":key_word}
# # wd=urllib.parse.urlencode(wd)
# # fullurl=url+"?"+wd
# # print(fullurl)
# # request=urllib.request.Request(fullurl)
# # response=urllib.request.urlopen(request)
# # ht=response.read()
# # print(ht)
#
# #
# # # us_Agent={"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
# # # request=urllib.request.Request(url,headers=us_Agent)
# # # responce=urllib.request.urlopen(request)
# # ua_list = [
# #     "Mozilla/5.0 (Windows NT 6.1; ) Apple.... ",
# #     "Mozilla/5.0 (X11; CrOS i686 2268.111.0)... ",
# #     "Mozilla/5.0 (Macintosh; U; PPC Mac OS X.... ",
# #     "Mozilla/5.0 (Macintosh; Intel Mac OS... "
# # ]
# # user_agent=random.choice(ua_list)
# # # print(user_agent)
# # request=urllib.request.Request(url)
# # request.add_header("User_Agent",user_agent)
# # request.get_header("User_agent")
# # responce=urllib.request.urlopen(request)
# # html=responce.read()
# # # print(responce.getcode())
# # # print(responce.geturl())
# # # print(responce.info())
# # # # print(html)
#
#
#
#
# # '''爬取贴吧，编码有问题'''
# # kw=input("请输入要爬取得贴吧：")
# # begin_page=int(input("请输入起始页："))
# # end_page=int(input("请输入结束页："))
# # url="http://tieba.baidu.com/f?"
# # key=urllib.parse.urlencode({"kw":kw})
# # url=url+key
# # # print(url)
# #
# # for page in range(begin_page,end_page+1):
# #     pn=(page-1)*50
# #     filename="第"+str(page)+"页.html"
# #     full_url=url+"&pn="+str(pn)
# #
# #     print("正在爬取....",filename)
# #     headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
# #     request=urllib.request.Request(full_url,headers=headers)
# #     response=urllib.request.urlopen(request)
# #
# #     html=response.read()
# #     html=str(html,encoding='utf-8')
# #     # win_code=chardet.detect(html)
# #     # print(type(win_code))
# #     # html1=html.decode(win_code['encoding']).encode('utf-8')
# #     # print(html)
# #     print("正在存储....",filename)
# #     with open(filename,'w',encoding='utf-8') as f:
# #         f.write(html)
#
#
# # url="https://movie.douban.com/j/chart/top_list?"
# # headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
# # formdata = {
# #     'type':'11',
# #     'interval_id':'100:90',
# #     'action':'',
# #     'start':'0',
# #     'limit':'10'
# # }
# # data=urllib.parse.urlencode(formdata).encode(encoding='utf-8')
# # # print(data)
# # request=urllib.request.Request(url,data=data,headers=headers)
# # response=urllib.request.urlopen(request)
# # html=response.read()
# # print(str(html,encoding='utf-8'))
#
#
# # 自定义opner，debuglevel=1表示程序在执行的时候，会把收包和发包的报头在屏幕上自动打印出来
# # http_handler=urllib.request.HTTPHandler(debuglevel=1)
# # opener=urllib.request.build_opener(http_handler)
# # request=urllib.request.Request("http://www.baidu.com/")
# # response=opener.open(request)
# # html=response.read()
# # html=str(html,encoding='utf-8')
# # print(html)
#
# # ProxyHandler处理器（代理设置）
# # proxy_list = [
# #     {"http" : "124.88.67.81:80"},
# #     {"http" : "124.88.67.81:80"},
# #     {"http" : "124.88.67.81:80"},
# #     {"http" : "124.88.67.81:80"},
# #     {"http" : "124.88.67.81:80"}
# # ]
# # proxy=random.choice(proxy_list)
# # httpproxy_handler=urllib.request.ProxyHandler(proxy)
# # nullproxy_handler=urllib.request.ProxyHandler({})
# # proxy_switch=True
# # if proxy_switch:
# #     opener=urllib.request.build_opener(httpproxy_handler)
# # else:
# #     opener=urllib.request.build_opener(nullproxy_handler)
# # request=urllib.request.Request("http://www.baidu.com/")
# # response=opener.open(request)
# # html=response.read()
# # print(html)
#
# # ProxyBasicAuthHandler(代理授权验证)
# # {账号：密码@代理地址：端口号}
# # user="mr_mao_hacker"
# # passwd="sffqry9r"
# # proxy_server="61.158.163.130:16816"
# # httpproxy_handler=urllib.request.ProxyHandler({"http":user+":"+passwd+"@"+proxy_server})
# # opener=urllib.request.build_opener(httpproxy_handler)
# # request=urllib.request.Request("http://www.baidu.com/")
# # response=opener.open(request)
# # html=response.read()
# # print(str(html,encoding='utf-8'))
#
#
#
# #
# # HTTPBasicAuthHandler处理器（Web客户端授权验证）
# # 其中还有一个ProxyBasicAuthHandler()是用来授权代理处理器
# # user="mr_mao_hacker"
# # passwd="sffqry9r"
# # proxy_server="61.158.163.130:16816"
# # #构建密码管理对象
# # passwd_mgr=urllib.request.HTTPPasswordMgrWithDefaultRealm()
# # #添加账户信息
# # passwd_mgr.add_password(None,uri=proxy_server,user=user,passwd=passwd)
# # #构建一个HTTP基础用户名/密码验证的HTTPBasicAuthHandler处理器对象，参数是创建的密码管理对象
# # http_auth_handler=urllib.request.HTTPBasicAuthHandler(passwd_mgr)
# # opener=urllib.request.build_opener(http_auth_handler)
# # #通过install_opener()将opener定义为全局opener
# # urllib.request.install_opener(opener)
# # request=urllib.request.Request("http://www.baidu.com/")
# # response=urllib.request.urlopen(request)
# # http=response.read()
# # print(str(http,encoding='utf-8'))
# # #====#=======================================================================================================================
# import matplotlib.pyplot as plt
# from sklearn.datasets import make_classification
# from sklearn.decomposition import PCA
# import numpy as np
# from imblearn.over_sampling import SMOTE
#
# # print(__doc__)
#
# # def plot_resampling(ax, X, y, title):
# #     c0 = ax.scatter(X[y == 0, 0], X[y == 0, 1], label="Class #0", alpha=0.5)
# #     c1 = ax.scatter(X[y == 1, 0], X[y == 1, 1], label="Class #1", alpha=0.5)
# #     ax.set_title(title)
# #     ax.spines['top'].set_visible(False)
# #     ax.spines['right'].set_visible(False)
# #     ax.get_xaxis().tick_bottom()
# #     ax.get_yaxis().tick_left()
# #     ax.spines['left'].set_position(('outward', 10))
# #     ax.spines['bottom'].set_position(('outward', 10))
# #     ax.set_xlim([-6, 8])
# #     ax.set_ylim([-6, 6])
# #
# #     return c0, c1
#
#
# # Generate the dataset
# # X, y = make_classification(n_classes=2, class_sep=2, weights=[0.3, 0.7],
# #                            n_informative=3, n_redundant=1, flip_y=0,
# #                            n_features=20, n_clusters_per_class=1,
# #                            n_samples=80, random_state=10)
# # X = np.array(
# #     [[5.1, 3.5, 1.4, 0.2], [4.9, 3.0, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2], [4.6, 3.1, 1.5, 0.2], [5.0, 3.6, 1.4, 0.2],
# #      [7.0, 3.2, 4.7, 1.4], [6.4, 3.2, 4.5, 1.5], [6.9, 3.1, 4.9, 1.5]])
# # y = np.array([0, 0, 0, 0, 0, 1, 1, 1])
# # print(len(X))
# # print(len(y))
# # print(len(X))
# # print(y)
# # X_resampled=[]
# # y_resampled=[]
# # sm=SMOTE(kind='regular')
# # X_res,y_res=sm.fit_sample(X,y)#采样过后
# #
# # Instanciate a PCA object for the sake of easy visualisation
# # pca = PCA(n_components=2)#初始化PCA#用于降维
# # Fit and transform x to visualise inside a 2D feature space
# # X_vis = pca.fit_transform(X)
# #
# # Apply regular SMOTE
# # kind = ['regular', 'borderline1', 'borderline2', 'svm']
# # sm = [SMOTE(kind=k) for k in kind]#初始化一个SMOTE对象
# # X_resampled = []
# # y_resampled = []
# # X_res_vis = []
# # for method in sm:
# #     X_res, y_res = method.fit_sample(X, y)
# #     X_resampled.append(X_res)
# #     y_resampled.append(y_res)
#     # X_res_vis.append(pca.transform(X_res))
# #
# # # Two subplots, unpack the axes array immediately
# # f, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)
# # # Remove axis for second plot
# # ax2.axis('off')
# # ax_res = [ax3, ax4, ax5, ax6]
# #
# # c0, c1 = plot_resampling(ax1, X_vis, y, 'Original set')
# # for i in range(len(kind)):
# #     plot_resampling(ax_res[i], X_res_vis[i], y_resampled[i],
# #                     'SMOTE {}'.format(kind[i]))
# #
# # ax2.legend((c0, c1), ('Class #0', 'Class #1'), loc='center',
# #            ncol=1, labelspacing=0.)
# # plt.tight_layout()
# # plt.show()



