#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 00:01:00 2018

@author: Shariful
"""

import glob
import numpy as np
hm_path = '/Users/Shariful/Documents/SysCallDataset/ADFA-LD/Training_Data_Master/*.txt'
txt_files = glob.glob(hm_path)

all_seq = []
 

for i in txt_files:
    infile=open(i)
    one_seq=infile.readline()
    all_seq.append(np.array(one_seq))
    infile.close()
    
    
dd_int = np.array(a)


nums = [3, 4, 5]

square_all = map(lambda num: num ** 2, nums)

print(list(square_all))


for i in range(8,13):
    print(i)