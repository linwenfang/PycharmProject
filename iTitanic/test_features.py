# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
# dt_train = pd.read_csv('train.csv')
# dt_test = pd.read_csv('test.csv')  # 读取csv
#
# dt_train_p = dt_train.drop(['Name', 'Ticket', 'Cabin'], axis=1)
# dt_test_p = dt_test.drop(['Name', 'Ticket', 'Cabin'], axis=1)  # 去除乘客姓名、船票信息和客舱编号三个不打算使用的列
# Pclass_Gender_grouped = dt_train_p.groupby(['Sex', 'Pclass'])  # 按照性别和舱位分组聚合
# PG_Survival_Rate = (Pclass_Gender_grouped.sum() / Pclass_Gender_grouped.count())['Survived']  # 计算存活率
#
# x = np.array([1, 2, 3])
# width = 0.3
# plt.bar(x - width, PG_Survival_Rate.female, width, color='r')
# plt.bar(x, PG_Survival_Rate.male, width, color='b')
# plt.title('Survival Rate by Gender and Pclass')
# plt.xlabel('Pclass')
# plt.ylabel('Survival Rate')
# plt.xticks([1, 2, 3])
# plt.yticks(np.arange(0.0, 1.1, 0.1))
# plt.grid(True, linestyle='-', color='0.7')
# plt.legend(['Female', 'Male'])
# plt.show()  # 画图
import pandas as pd #数据分析
import numpy as np #科学计算
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

data_train = pd.read_csv("Train.csv")
# print(data_train)
# fig = plt.figure()
# fig.set(alpha=0.2)  # 设定图表颜色alpha参数
#
# plt.subplot2grid((2,3),(0,0))# 在一张大图里分列几个小图
# data_train.Survived.value_counts().plot(kind='bar')# 柱状图
# plt.title('Rescue situation (Be saved expressed by 1)') # 标题
# plt.ylabel("number of people")
#
# plt.subplot2grid((2,3),(0,1))
# data_train.Pclass.value_counts().plot(kind="bar")
# plt.ylabel("number of people")
# plt.title("Pclass")
#
# plt.subplot2grid((2,3),(0,2))
# plt.scatter(data_train.Survived, data_train.Age)
# plt.ylabel("Age")                         # 设定纵坐标名称
# plt.grid(b=True, which='major', axis='y')
# plt.title("Age and Rescue (Be saved expressed by 1)")
#
#
# plt.subplot2grid((2,3),(1,0), colspan=2)
# data_train.Age[data_train.Pclass == 1].plot(kind='kde')
# data_train.Age[data_train.Pclass == 2].plot(kind='kde')
# data_train.Age[data_train.Pclass == 3].plot(kind='kde')
# plt.xlabel("Age")# plots an axis lable
# plt.ylabel("Density")
# plt.title("Age and Pclass")
# plt.legend(('First Class', 'Second Class','Third Class'),loc='best') # sets our legend for our graph.
#
#
# plt.subplot2grid((2,3),(1,2))
# data_train.Embarked.value_counts().plot(kind='bar')
# plt.title("Number of Embarked")
# plt.ylabel("number of people")
# plt.show()
#
# '''各乘客等级的获救情况'''
# fig = plt.figure()
# fig.set(alpha=0.2)  # 设定图表颜色alpha参数
# Survived_0 = data_train.Pclass[data_train.Survived == 0].value_counts()
# Survived_1 = data_train.Pclass[data_train.Survived == 1].value_counts()
# df=pd.DataFrame({'Rescued':Survived_1, 'Not Rescued':Survived_0})
# df.plot(kind='bar', stacked=True)
# plt.title("Pclass and Survived")
# plt.xlabel("Pclass")
# plt.ylabel("number of people")
# plt.show()#明显等级为1的乘客，获救的概率高很多
#
# '''各性别的获救情况'''
# fig = plt.figure()
# fig.set(alpha=0.2)  # 设定图表颜色alpha参数
# Survived_m = data_train.Survived[data_train.Sex == 'male'].value_counts()
# Survived_f = data_train.Survived[data_train.Sex == 'female'].value_counts()
# df=pd.DataFrame({'male':Survived_m, u'femal':Survived_f})
# df.plot(kind='bar', stacked=True)
# plt.title("Age and Survived")
# plt.xlabel("Age")
# plt.ylabel("number of people")
# plt.show()#女性获救的概率高

# '''各种舱级别情况下各性别的获救情况'''
# fig=plt.figure()
# fig.set(alpha=0.65) # 设置图像透明度，无所谓
# plt.title(u"Pclass and Age and Survived")
#
#
# ax1=fig.add_subplot(141)
# data_train.Survived[data_train.Sex == 'female'][data_train.Pclass != 3].value_counts().plot(kind='bar', label="female high class", color='#FA2479')
# ax1.set_xticklabels(["Rescued", "Not Rescued"], rotation=0)
# ax1.legend(["female/First and Second Class"], loc='best')
#
# ax2=fig.add_subplot(142)
# data_train.Survived[data_train.Sex == 'female'][data_train.Pclass == 3].value_counts().plot(kind='bar', label='female, low class', color='pink')
# ax2.set_xticklabels(["Rescued", "Not Rescued"], rotation=0)
# plt.legend(["female/Third Class"], loc='best')
#
# ax3=fig.add_subplot(143)
# data_train.Survived[data_train.Sex == 'male'][data_train.Pclass != 3].value_counts().plot(kind='bar', label='male, high class',color='lightblue')
# ax3.set_xticklabels(["Rescued", "Not Rescued"], rotation=0)
# plt.legend(["male/First and Second Class"], loc='best')
#
# ax4=fig.add_subplot(144)
# data_train.Survived[data_train.Sex == 'male'][data_train.Pclass == 3].value_counts().plot(kind='bar', label='male low class', color='steelblue')
# ax4.set_xticklabels(["Rescued", "Not Rescued"], rotation=0)
# plt.legend(["male/Third Class"], loc='best')
#
# plt.legend()
# plt.show()

'''登录港口的获救情况'''
# fig = plt.figure()
# fig.set(alpha=0.2)  # 设定图表颜色alpha参数
#
# Survived_0 = data_train.Embarked[data_train.Survived == 0].value_counts()
# Survived_1 = data_train.Embarked[data_train.Survived == 1].value_counts()
# df=pd.DataFrame({"Rescued":Survived_1, "Not Rescued":Survived_0})
# df.plot(kind='bar', stacked=True)
# plt.title(u"Port and Survived")
# plt.xlabel("Embarked")
# plt.ylabel("number of people")
#
# plt.show()
'''亲属关系'''
# g = data_train.groupby(['SibSp','Survived'])
# df = pd.DataFrame(g.count()['PassengerId'])
# print(df)
#
# g = data_train.groupby(['SibSp','Survived'])
# df = pd.DataFrame(g.count()['PassengerId'])
# print(df)
