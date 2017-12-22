import os
#数据处理
import pandas as pd
import numpy as np
import random
import sklearn.preprocessing as preprocessing
#可视化
import matplotlib.pyplot as plt
import seaborn as sns
#ML
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import (GradientBoostingClassifier, GradientBoostingRegressor,
                              RandomForestClassifier, RandomForestRegressor)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve






train = pd.read_csv(r'E:\PycharmProjects\titanic_data\train.csv')
test = pd.read_csv(r'E:\PycharmProjects\titanic_data\test.csv')

# from scipy import stats
# fig, axes = plt.subplots(2,1,figsize=(8,6))
# sns.set_style('white')
# sns.distplot(train.Age.fillna(-1), rug=True, color='b', ax=axes[0])
# ax0 = axes[0]
# ax0.set_title('age distribution')
# ax0.set_xlabel('')
#
# ax1 = axes[1]
# ax1.set_title('age survived distribution')
# k1 = sns.distplot(train[train.Survived==0].Age.fillna(-1), hist=False, color='r', ax=ax1, label='dead')
# k2 = sns.distplot(train[train.Survived==1].Age.fillna(-1), hist=False, color='g', ax=ax1, label='alive')
# ax1.set_xlabel('')
#
# ax1.legend(fontsize=16)



# f, ax = plt.subplots(figsize=(8,3))
# ax.set_title('Sex Age dist', size=20)
# sns.distplot(train[train.Sex=='female'].dropna().Age, hist=False, color='pink', label='female')
# sns.distplot(train[train.Sex=='male'].dropna().Age, hist=False, color='blue', label='male')
# ax.legend(fontsize=15)



# f, ax = plt.subplots(figsize=(8,3))
# ax.set_title('Pclass Age dist', size=20)
# sns.distplot(train[train.Pclass==1].dropna().Age, hist=False, color='pink', label='P1')
# sns.distplot(train[train.Pclass==2].dropna().Age, hist=False, color='blue', label='p2')
# sns.distplot(train[train.Pclass==3].dropna().Age, hist=False, color='g', label='p3')
# ax.legend(fontsize=15)



# y_dead = train[train.Survived==0].groupby('Pclass')['Survived'].count()
# y_alive = train[train.Survived==1].groupby('Pclass')['Survived'].count()
# pos = [1, 2, 3]
# ax = plt.figure(figsize=(8,4)).add_subplot(111)
# ax.bar(pos, y_dead, color='r', alpha=0.6, label='dead')
# ax.bar(pos, y_alive, color='g', bottom=y_dead, alpha=0.6, label='alive')
# ax.legend(fontsize=16, loc='best')
# ax.set_xticks(pos)
# ax.set_xticklabels(['Pclass%d'%(i) for i in range(1,4)], size=15)
# ax.set_title('Pclass Surveved count', size=20)

# pos = range(0,6)
# age_list = []
# for Pclass_ in range(1,4):
#     for Survived_ in range(0,2):
#         age_list.append(train[(train.Pclass == Pclass_)&(train.Survived == Survived_)].Age.fillna(-1))
#
# fig, axes = plt.subplots(3,1,figsize=(10,6))
#
# i_Pclass = 1
#
# for ax in axes:
#     sns.distplot(age_list[i_Pclass*2-2], hist=False, ax=ax, label='Pclass:'+str(i_Pclass)+' ,survived:0', color='r')
#     sns.distplot(age_list[i_Pclass*2-1], hist=False, ax=ax, label='Pclass:'+str(i_Pclass)+' ,survived:1', color='g')
#     i_Pclass += 1
#     ax.set_xlabel('age', size=15)
#     ax.legend(fontsize=15)



# print(train.Sex.value_counts())
# print('********************************')
# print (train.groupby('Sex')['Survived'].mean())


# ax = plt.figure(figsize=(10,4)).add_subplot(111)
# sns.violinplot(x='Sex', y='Age', hue='Survived', data=train.dropna(), split=True)
# ax.set_xlabel('Sex',size=20)
# ax.set_xticklabels(['Female','male'], size=18)
# ax.set_ylabel('Age',size=20)
# ax.legend(fontsize=25,loc='best')


# label = []
# for sex_i in ['female', 'male']:
#     for pclass_i in range(1, 4):
#         label.append('sex:%s,Pclass:%d' % (sex_i, pclass_i))
#
# pos = range(6)
# fig = plt.figure(figsize=(16, 4))
# ax = fig.add_subplot(111)
# ax.bar(pos,
#        train[train['Survived'] == 0].groupby(['Sex', 'Pclass'])['Survived'].count().values,
#        color='r',
#        alpha=0.5,
#        align='center',
#        tick_label=label,
#        label='dead')
# ax.bar(pos,
#        train[train['Survived'] == 1].groupby(['Sex', 'Pclass'])['Survived'].count().values,
#        bottom=train[train['Survived'] == 0].groupby(['Sex', 'Pclass'])['Survived'].count().values,
#        color='g',
#        alpha=0.5,
#        align='center',
#        tick_label=label,
#        label='alive')
# ax.tick_params(labelsize=15)
# ax.set_title('sex pclass survived', size=30)
# ax.legend(fontsize=15, loc='best')



# fig = plt.figure(figsize=(8, 6))
# ax = plt.subplot2grid((2,2), (0,0), colspan=2)
#
# ax.tick_params(labelsize=15)
# ax.set_title('Fare dist', size=20)
# ax.set_ylabel('dist', size=20)
# sns.kdeplot(train.Fare, ax=ax)
# # sns.distplot(train.Fare, ax=ax)
# ax.legend(fontsize=15)
# pos = range(0,400,50)
# ax.set_xticks(pos)
# ax.set_xlim([0, 200])
# ax.set_xlabel('')
#
# ax1 = plt.subplot2grid((2,2), (1,0), colspan=2)
# ax.set_title('Fare Pclass distribution', size=20)
# for i in range(1,4):
#     sns.kdeplot(train[train.Pclass==i].Fare, ax=ax1, label='Pclass %d'%(i))
# ax1.set_xlim([0,200])
# ax1.legend(fontsize=15)



# fig = plt.figure(figsize=(8,3))
# ax1 = fig.add_subplot(111)
# sns.kdeplot(train[train.Survived==0].Fare, ax=ax1, label='dead', color='r')
# sns.kdeplot(train[train.Survived==1].Fare, ax=ax1, label='alive', color='g')
# #sns.distplot(train[train.Survived==0].Fare, ax=ax1, color='r')
# #sns.distplot(train[train.Survived==1].Fare, ax=ax1, color='g')
# ax1.set_xlim([0,300])
# ax1.legend(fontsize=15)
# ax1.set_title('Fare survived', size=20)
# ax1.set_xlabel('Fare', size=15)


# fig = plt.figure(figsize=(8,4))
# ax1 = fig.add_subplot(211)
# sns.countplot(train.SibSp)
# ax1.set_title('SibSp', size=20)
# ax2 = fig.add_subplot(212, sharex=ax1)
# sns.countplot(train.Parch)
# ax2.set_title('Parch', size=20)



# fig = plt.figure(figsize=(10,6))
# ax1 = fig.add_subplot(311)
# train.groupby('SibSp')['Survived'].mean().plot(kind='bar', ax=ax1)
# ax1.set_title('Sibsp Survived Rate', size=16)
# ax1.set_xlabel('')
#
# ax2 = fig.add_subplot(312)
# train.groupby('Parch')['Survived'].mean().plot(kind='bar', ax=ax2)
# ax2.set_title('Parch Survived Rate', size=16)
# ax2.set_xlabel('')
#
# ax3 = fig.add_subplot(313)
# train.groupby(train.SibSp+train.Parch)['Survived'].mean().plot(kind='bar', ax=ax3)
# ax3.set_title('Parch+Sibsp Survived Rate', size=16)



# plt.style.use('ggplot')
# ax = plt.figure(figsize=(8,3)).add_subplot(111)
# pos = [1, 2, 3]
# y1 = train[train.Survived==0].groupby('Embarked')['Survived'].count().sort_index().values
# y2 = train[train.Survived==1].groupby('Embarked')['Survived'].count().sort_index().values
# ax.bar(pos, y1, color='r', alpha=0.4, align='center', label='dead')
# ax.bar(pos, y2, color='g', alpha=0.4, align='center', label='alive', bottom=y1)
# ax.set_xticks(pos)
# ax.set_xticklabels(['C','Q','S'])
# ax.legend(fontsize=15, loc='best')
# ax.set_title('Embarked survived count', size=18)


# ax = plt.figure(figsize=(8,3)).add_subplot(111)
# ax.set_xlim([-20, 80])
# sns.kdeplot(train[train.Embarked=='C'].Age.fillna(-10), ax=ax, label='C')
# sns.kdeplot(train[train.Embarked=='Q'].Age.fillna(-10), ax=ax, label='Q')
# sns.kdeplot(train[train.Embarked=='S'].Age.fillna(-10), ax=ax, label='S')
# ax.legend(fontsize=18)
# ax.set_title('Embarked Age Dist ', size=18)
train.groupby(train.Name.apply(lambda x: len(x)))['Survived'].mean().plot()
plt.show()