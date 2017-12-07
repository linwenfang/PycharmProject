from sklearn.externals import joblib
from sklearn import datasets
from sklearn import svm
from sklearn import random_projection
import time
import numpy as np
if __name__ == '__main__':

    clf=svm.SVC()
    iris=datasets.load_iris()
    digit=datasets.load_digits()

    iris_X,iris_y=iris.data,iris.target
    digit_X,digit_y=digit.data,digit.target


    # print(y)
    # start=time.time()
    # end=time.time()
    #
    # joblib.dump(clf,'model.txt')
    # clf2=joblib.load('model.txt')
    # start=time.time()
    #
    # print(clf2.predict(X))


