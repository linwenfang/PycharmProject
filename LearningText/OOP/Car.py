#coding=gbk
# class Car:
#     def __init__(self,newNum,newColor):
#         self.wheelNum=newNum#wheelNum��ΪCar���һ������
#         self.color=newColor#color��ΪCar���һ������
#     def __str__(self):
#         msg="color="+self.color+"  wheelnum="+str(self.wheelNum)#��ô�����������Ҳ������
#         return msg
#     def move(self):
#         print('runing...')
#     def tools(self):
#         print('���ڽ�....')
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def printName(self):
#         print('my name is '+self.name)
# '''�����Ե������еķ���'''
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
#             print("error:���ֳ�����Ҫ���ڻ��ߵ���5")
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
#         print("init����������")
#         self.__name=name
#     def __del__(self):
#         print("del����������")
#         print("%s����Ҫ��ɾ����"%self.__name)
# dog=test_del('��һ��')
# del dog
# cat=test_del('�ڶ���')
# cat2 = cat
# cat3 = cat
#
# print("---���� ɾ��cat����")
# # del cat
# print("---���� ɾ��cat2����")
# # del cat2
# print("---���� ɾ��cat3����")
# del cat3
#
# print("����2���Ӻ����")
# time.sleep(2)
'''˽�����Կ���ͨ�����ø���ķ������ʣ�˽�з������������ǲ����Է��ʵ�'''
# class Cat(object):
#     def __init__(self,name,color='black'):
#         self.__name=name
#         self.color=color
#     def run(self):
#         print("%s can run"%self.__name)
#     def __test(self):
#         print("����pravite")
#         print(self.__name)
#         print(self.color)
#     def test(self):
#         print("����public")
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
# # ����һ������
# class B(base):
#     def test(self):
#         print('----B test----')
#
# # ����һ�����࣬�̳���A��B
# class C(A,B):
#     pass
#
#
# obj_C = C()
# obj_C.test()
#
# print(C.__mro__) #���Բ鿴C��Ķ�����������ʱ���Ⱥ�˳��

# class Cat(object):
#     def __init__(self,name):
#         self.name=name
#     def sayhello(self):
#         print("say hello ---1---")
# class Bosi(Cat):
#     def sayhello(self):
#         print("say hello ---2---")
#         super().sayhello()#��д����������ø����sayhello����
# bosi=Bosi('huahua')
# bosi.sayhello()

# '''��̬'''
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


# '''������'''
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








