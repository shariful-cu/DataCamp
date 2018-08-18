#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 03:53:09 2018

@author: Shariful
"""

import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
meas = [np_height, np_weight]

# printing values same as like in 2d array
#for var in meas :
#    print(var)
    
    
# printing values based on order of index in 2d array
for var in np.nditer(meas) :
    print(var)
    print(var, end = 'builtins')