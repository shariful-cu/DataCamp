#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 03:41:21 2018

@author: Shariful
"""

import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2


for var in bmi :
    print(var)
    
    
# For loop over np_height
for var in np_height :
    print(str(var) + " inches")
