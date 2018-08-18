#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 11:02:11 2018

@author: Shariful
"""
#import os, sys
import numpy as np


#dir_path = os.path.abspath(os.path.dirname(sys.argv[0]))
#idx = dir_path.rfind('/')
#if idx == -1:
#    idx = dir_path.rfind('\\')
#sys.path.append(dir_path[: -(len(dir_path) - idx)])

#sys.path.remove(dir_path[: -(len(dir_path) - idx)])

#from DataCamp.deep_ln import relu
from DataCamp import deep_ln

 
#one hidden layer
input_data = np.array([[3, 5], [1, -1], [0, 0], [8, 4]])
weights = {'node_0': np.array([2, 4]), 
           'node_1': np.array([ 4, -5]), 
           'output': np.array([2, 7])}


# Create empty list to store prediction results
results = []
for input_data_row in input_data:
    # Append prediction to results
    results.append(deep_ln.predict_with_network(input_data_row, weights))

# Print results
print(results)


#two hidden layer

