#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Jan  7 16:16:09 2019

BOOK NAME: A Practical Guide for Machine Learning in Python

====================Topics With High Level View==============================
    TRANSFORMING SEQUENCES INTO FIXED LENGTH SEQUENCES BY PADDING ZEROS:
        Lines: 37 to 49
    
    READ .MAT (MATLAB) FILE AND ACCESS ITS ELEMENTS:
        Lines: 37 to 49

====================Topics With Low Level View==============================
    TRANSFORMING SEQUENCES INTO FIXED LENGTH SEQUENCES BY PADDING ZEROS:
        Description:
            input : a = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
            output: b = [[1, 2, 3, 0], [4, 5, 0, 0], [6, 7, 8, 9]]
            
    READ .MAT (MATLAB) FILE AND ACCESS ITS ELEMENTS:
        Description:
            -use scipy.io.loadmat(path)
            
@author: Shariful
"""

#-----converting mat file inot txt file-----

#import necessary modules
import scipy.io
import numpy as np
import os

#loading data
home_dir = '/Users/Shariful/Documents/SysCallDataset/PreparedData/Canali_dataset'

for filename in os.listdir(home_dir):
    
    file_path = home_dir + '/' + filename
    
    if not os.path.isfile(file_path) or filename == '.DS_Store':
        continue
    
    seqs = scipy.io.loadmat(file_path) # seqs is a dict and data in index[3]
    
    #dict does not allow indexing, so convert it into list of objects
    seqs = list(seqs.values()[0])
    
    for item in seqs:
        item = np.array(list(item)) 
        item = list(item.reshape(item.shape[2]))



#path = home_dir + '/Gnome/OriginalSeqDataset/Version/VersionReAsgnd.mat'
#seqs = scipy.io.loadmat(path) # seqs is a dict and data in index[3]
#
##dict does not allow indexing, so convert it into list of objects
#seqs = list(seqs.values())[3]
#seqs_lists = []
#for item in seqs:
#    item = np.array(list(item)) 
#    item = list(item.reshape(item.shape[2]))
#    seqs_lists.append(item)
#
#fixed_size_array = np.zeros([len(seqs_lists),len(max(seqs_lists, \
#                            key = lambda x: len(x)))])
#   
#for idx, seq in enumerate(seqs_lists):
#    fixed_size_array[idx][0:len(seq)] = seq
#    
#fixed_size_array_unq = np.unique(fixed_size_array, axis=0)

#--------------------------------------END OF----------------------------------

##-----TRANSFORMING SEQUENCES INTO FIXED LENGTH SEQUENCES BY PADDING ZEROS-----
#
##import necessary modules
#import scipy.io
#import numpy as np
#
##loading data
#home_dir = '/Users/Shariful/Desktop/BugReassignedProject/PreparedData'
#path = home_dir + '/Gnome/OriginalSeqDataset/Version/VersionReAsgnd.mat'
#seqs = scipy.io.loadmat(path) # seqs is a dict and data in index[3]
#
##dict does not allow indexing, so convert it into list of objects
#seqs = list(seqs.values())[3]
#seqs_lists = []
#for item in seqs:
#    item = np.array(list(item)) 
#    item = list(item.reshape(item.shape[2]))
#    seqs_lists.append(item)
#
#fixed_size_array = np.zeros([len(seqs_lists),len(max(seqs_lists, \
#                            key = lambda x: len(x)))])
#   
#for idx, seq in enumerate(seqs_lists):
#    fixed_size_array[idx][0:len(seq)] = seq
#    
#fixed_size_array_unq = np.unique(fixed_size_array, axis=0)
#
##--------------------------------------END OF----------------------------------

#-----READ .MAT (MATLAB) FILE AND ACCESS ITS ELEMENTS-----

#write_path = home_dir + '/Eclipse/test.txt'
#
#with open(write_path, 'w') as f:
#    for item in seqs:
#        item = np.array(list(item)) 
#        item = item.reshape(item.shape[2])
#        all_seq.append(item)
#        print(str(item)[1:-1], file = f) #use index range to avoaid writing brackets
##        f.write("{}\n".format(item)) #write with bracket
##        f.write("%s\n" % str(item)[1:-1]) #write with bracket
#--------------------------------------END OF----------------------------------
