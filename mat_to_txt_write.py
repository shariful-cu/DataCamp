#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 16:16:09 2019

Read sequences (int numbers) from a mat file and write it into text file

@author: Shariful
"""

import scipy.io
import numpy as np


home_dir = '/Users/Shariful/Desktop/BugReassignedProject/PreparedData'
path = home_dir + '/Eclipse/OriginalSeqDataset/Component/CompntNotReAsgnd.mat'

seqs = scipy.io.loadmat(path) # seqs is a dict and data in index[3]

#dict does not allow indexing, so convert it into list of objects
seqs = list(seqs.values())[3] 

write_path = home_dir + '/Eclipse/test.txt'
with open(write_path, 'w') as f:
    for item in seqs:
        item = np.array(list(item)) 
        item = item.reshape(item.shape[2])
        print(str(item)[1:-1], file = f) #use index range to avoaid writing brackets
#        f.write("{}\n".format(item)) #write with bracket
#        f.write("%s\n" % str(item)[1:-1]) #write with bracket

