#coding=gbk
# class Car:
#     def __init__(self,newNum,newColor):
#         self.wheelNum=newNum#wheelNum作为Car类的一个属性
#         self.color=newColor#color作为Car类的一个属性
#     def __str__(self):
#         msg="color="+self.color+"  wheelnum="+str(self.wheelNum)#怎么将对象的名字也传进来
#         return msg
#     def move(self):
#         print('runing...')
#     def tools(self):
#         print('正在叫....')
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def printName(self):
#         print('my name is '+self.name)
# '''都可以调用类中的方法'''
# def myPrint(anima):
#     anima.printName()
# dog1=Animal('beibei')
# myPrint(dog1)
# dog1.printName()
#
# BMW=Car(4,'blue')
# BMW.move()
# AUDI=Car(4,'red')
# print(BMW.color)
# print(BMW.wheelNum)
# print(BMW)
# print(AUDI)
#
# class People(object):
#
#     def __init__(self, name):
#         self.__name = name
#         self.name=name
#
#     def getName(self):
#         return self.__name,self.name
#
#     def setName(self, newName):
#         if len(newName) >= 5:
#             self.__name = newName
#         else:
#             print("error:名字长度需要大于或者等于5")
#
# xiaoming = People("dongGe")
# xiaoming.name='ahahhahaha'
# print(xiaoming.getName())
# xiaoming.setName("wanger")
# print(xiaoming.getName())
#
# xiaoming.setName("lisi")
# print(xiaoming.getName())
import time
# class test_del:
#     def __init__(self,name):
#         print("init方法被调用")
#         self.__name=name
#     def __del__(self):
#         print("del方法被调用")
#         print("%s对象要被删除了"%self.__name)
# dog=test_del('第一个')
# del dog
# cat=test_del('第二个')
# cat2 = cat
# cat3 = cat
#
# print("---马上 删除cat对象")
# # del cat
# print("---马上 删除cat2对象")
# # del cat2
# print("---马上 删除cat3对象")
# del cat3
#
# print("程序2秒钟后结束")
# time.sleep(2)
'''私有属性可以通过调用父类的方法访问，私有方法在子类中是不可以访问的'''
# class Cat(object):
#     def __init__(self,name,color='black'):
#         self.__name=name
#         self.color=color
#     def run(self):
#         print("%s can run"%self.__name)
#     def __test(self):
#         print("我是pravite")
#         print(self.__name)
#         print(self.color)
#     def test(self):
#         print("我是public")
#         print(self.__name)
#         print(self.color)
# class Bosi(Cat):
#     def setNewName(self,newName):
#         self.__name=newName
#     def eat(self):
#         print("%s is eating..."%self.__name)
#     def run(self):
#         print("%s is runing..."%self.__name)
# bs=Bosi('indinan','white')
# bs.setNewName('liuhaha')
#coding=utf-8
# class base(object):
#     def test(self):
#         print('----base test----')
# class A(base):
#     def test(self):
#         print('----A test----')
#
# # 定义一个父类
# class B(base):
#     def test(self):
#         print('----B test----')
#
# # 定义一个子类，继承自A、B
# class C(A,B):
#     pass
#
#
# obj_C = C()
# obj_C.test()
#
# print(C.__mro__) #可以查看C类的对象搜索方法时的先后顺序

# class Cat(object):
#     def __init__(self,name):
#         self.name=name
#     def sayhello(self):
#         print("say hello ---1---")
# class Bosi(Cat):
#     def sayhello(self):
#         print("say hello ---2---")
#         super().sayhello()#重写方法里面调用父类的sayhello方法
# bosi=Bosi('huahua')
# bosi.sayhello()

# '''多态'''
# class F1(object):
#     def show(self):
#         print("F1 show")
# class S1(F1):
#     def show(self):
#         print("S1 show")
# class S2(F1):
#     def show(self):
#         print("S2 show")
# def Func(obj):
#     print(obj.show())
#
# s1_obj=S1()
# Func(s1_obj)
# s2_obj=S2()
# Func(s2_obj)


# '''类属性'''
# class People:
#     address='china'
# print(People.address)
# p=People()
# print(p.address)
# p.address='janpan'
# print(p.address)
# print(People.address)
# People.address='janpan'
# print(p.address)
# print(People.address)








