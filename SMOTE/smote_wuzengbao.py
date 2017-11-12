# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 18:11:17 2017

@author: Administrator
"""

import random #导入random库
from sklearn.neighbors import NearestNeighbors #加载最近邻算法
import numpy as np
import csv

class Smote:  
    #samples的最后一列是类标，都是1
    def __init__(self,samples,N=10,k=5):
    	self.n_samples,self.n_attrs=np.array(samples).shape
    	self.N=N
    	self.k=k
    	self.samples=samples
    	self.new_index=0
    
    #过采样
    def over_sampling(self):
    	if self.N<100:  ######################################
    		old_n_sample=self.n_samples
    		print('old_n_sample',old_n_sample)
    		self.n_samples=int(float(self.N)/100*old_n_samples)
    		print ('n_samples', self.n_samples)
    		keep=np.random.permutation(old_n_samples)[:self.n_samples]  #permutation:返回一个序列的随机排列或返回一个随机排列的范围
    		print ('keep', keep)
    		new_samples=self.samples[keep]
    		print ('new_samples', new_samples)
    		self.samples=new_samples
    		print ('self.samples', self.samples)
    		self.N=100


    	N=int(self.N/100)
    	self.synthetic = np.zeros((self.n_samples * N, self.n_attrs))             #创建一个二维零数组
    	neighbors=NearestNeighbors(n_neighbors=self.k).fit(self.samples)
    	print ('neighbors',neighbors)

    	for i in range(len(self.samples)):
            nnarray=neighbors.kneighbors(self.samples[i].reshape(1,-1),return_distance=False)[0]
            #存储k个近邻的下标
            self._populate(N,i,nnarray)
    	return self.synthetic


    # 对于每一个少数类样本，选择k最近邻中的N个并产生N个合成样本
    def _populate(self,N,i,nnarray):
        for j in range(N):
            nn=random.randint(0,self.k-1)
            dif=self.samples[nnarray[nn]]-self.samples[i]  #少数类样本与最近邻样本之间的差异
            gap=random.random()   #产生一个随机数gap
            self.synthetic[self.new_index]=self.samples[i]+gap*dif  #生成新合成的样本到synthetic数组中
            self.new_index+=1
            csvfile = open('a.csv','w',newline='')
            writer = csv.writer(csvfile)
            writer.writerows(self.synthetic)
            csvfile.close()
#a=np.array([[6,148,72,35,0,33.6,0.627,50],[1,85,66,29,0,26.6,0.351,31],[8,183,64,0,0,23.3,0.672,32],[1,89,66,23,94,28.1,0.167,21],[0,137,40,35,168,43.1,2.288,33],[5,116,74,0,0,25.6,0.201,30]])

a = np.loadtxt('yeast05679vs4(0.15).txt',delimiter=',')
s=Smote(a,N=400)
print (s.over_sampling())