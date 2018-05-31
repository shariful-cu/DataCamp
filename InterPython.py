#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 17:45:11 2018

@author: Shariful
"""


# ============================Intermediate Python Practice=====================
# PLOTTING
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

#------Loading data
data = load_iris()

#-------Accessing each dimensions
sepal_len = np.array(data.data[:,0])
sepal_width = np.array(data.data[:,1])
petal_len = np.array(data.data[:,2])
petal_width = np.array(data.data[:,3])
labels = np.array(data.target)

dic = {0:'m',
       1:'y',
       2:'r'
       }

col = np.empty(labels.size, dtype = str);
for i in range(0, labels.size):
    col[i] = dic[labels[i]]
#    if labels[i] == 0:
#        col[i] = 'm'
#    elif labels[i] == 1:
#        col[i] = 'y'
#    elif labels[i] == 2:
#        col[i] = 'r'
        
#-----Ploting with different moded
#plt.plot(sepal_len, petal_len)
#plt.show()
plt.scatter(sepal_len, petal_len, s = petal_len * petal_width, c = col)
plt.grid(True)
plt.xlabel("sepal length (cm)")
plt.ylabel("petal length (cm)")
plt.title("Iris dataset")
plt.show()
plt.clf()
#plt.hist(sepal_len)
#plt.show()
#plt.clf()

#plt.hist(sepal_len, bins = 15)
#plt.show()
#plt.clf()
#print(boston.data.shape)
#print(boston.feature_names)
# =============================================================================




