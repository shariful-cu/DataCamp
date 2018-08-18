#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 23:13:02 2018

@author: Shariful
"""

#===============read_all_seq()==================
def read_all_seq (hm_path):
    
    """
    Input: 
        hm_path: path or directory
    
    Descritption:
        read all the text files located at the given directory (var: hm_path)
    
    Output: 
        return a list of numpy array (var: all_seq)
    """
    
    import glob
    
    txt_files = glob.glob(hm_path)
    all_seq = []
    for i in txt_files:
        infile=open(i)
        one_seq=infile.readline()
        one_seq = str.split(one_seq, ' ')
        one_seq = one_seq[: len(one_seq)-1]
        one_seq = list(map(int, one_seq))
        all_seq.append(np.array(one_seq))
        infile.close()
    return all_seq
#===============end of read_all_seq()==================

#===============reading train, test(normal), and test(attack) sequences=====
import glob
import numpy as np
import csv

trn_path = '/Users/Shariful/Documents/SysCallDataset/ADFA-LD/Training_Data_Master/*.txt'
train_seqs = read_all_seq(trn_path)

test_normal_path = '/Users/Shariful/Documents/SysCallDataset/ADFA-LD/Validation_Data_Master/*.txt'
test_normal_seqs = read_all_seq(test_normal_path)


test_attack_path = '/Users/Shariful/Documents/SysCallDataset/ADFA-LD/Attack_Data_Master'
list_dir = glob.os.listdir(test_attack_path)

test_attack_seqs = []
for a_dir in list_dir:
    one_seq = [];
    if a_dir.find('.mat') != -1 or a_dir.find('_Store') != -1:
        continue
    else:
        dir_path = test_attack_path + '/' + a_dir + '/*.txt'
        list_seqs = read_all_seq(dir_path)
        one_seq = np.concatenate(list_seqs, axis=0 )
        test_attack_seqs.append(one_seq)
        
#===============end of reading==================
        
        
#==creating dictionary (key, value) where value is the document frequency ()===
all_doc = train_seqs + test_normal_seqs + test_attack_seqs

dict_df = {}
for doc in all_doc:
    temp_dict = {}
    for symbol in doc:
        if not symbol in temp_dict.keys():
            temp_dict[symbol] = 1
        if not symbol in dict_df.keys():
            dict_df[symbol] = 1
    dict_df.update({key: dict_df[key] + 1 for key in temp_dict.keys()})
dict_df.update({key: len(all_doc) / dict_df[key] for key in dict_df.keys()})

# writing dict_df
filePath = '/Users/Shariful/Documents/DataCamp/ADFA-LD(tf-idf)/adfa_df.csv'
with open(filePath, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = dict_df.keys())
    writer.writeheader()
    writer.writerow(dict_df)
    csvfile.close()
print("Writing df is completed") 
#==Ebd of creating dictionary=========

#===========use dict_df for computing and writing tf_idf (TRAINING SET)======
filePath = '/Users/Shariful/Documents/DataCamp/ADFA-LD(tf-idf)/train_normal.csv'
with open(filePath, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = dict_df.keys())
    writer.writeheader() 
    for seq in train_seqs:
        vec_trn = dict_df.fromkeys(dict_df, 0)
        for symbol in seq:
            vec_trn[symbol] = vec_trn[symbol] + 1
        vec_trn.update({key: dict_df[key] * (vec_trn[key] / len(seq))  for key in vec_trn.keys()})
        writer.writerow(vec_trn)
    csvfile.close()  
print("Writing tf-idf for training set is completed")

#===========use dict_df for computing and writing tf_idf (TESTING Normal SET)==
filePath = '/Users/Shariful/Documents/DataCamp/ADFA-LD(tf-idf)/test_normal.csv'
with open(filePath, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = dict_df.keys())
    writer.writeheader() 
    for seq in test_normal_seqs:
        vec_trn = dict_df.fromkeys(dict_df, 0)
        for symbol in seq:
            vec_trn[symbol] = vec_trn[symbol] + 1
        vec_trn.update({key: dict_df[key] * (vec_trn[key] / len(seq))  for key in vec_trn.keys()})
        writer.writerow(vec_trn)
    csvfile.close()  
print("Writing tf-idf for testing normal set is completed")    


#===========use dict_df for computing and writing tf_idf (TESTING Attack SET)==
filePath = '/Users/Shariful/Documents/DataCamp/ADFA-LD(tf-idf)/test_attack.csv'
with open(filePath, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = dict_df.keys())
    writer.writeheader() 
    for seq in test_attack_seqs:
        vec_trn = dict_df.fromkeys(dict_df, 0)
        for symbol in seq:
            vec_trn[symbol] = vec_trn[symbol] + 1
        vec_trn.update({key: dict_df[key] * (vec_trn[key] / len(seq))  for key in vec_trn.keys()})
        writer.writerow(vec_trn)
    csvfile.close()  
print("Writing tf-idf for testing attack set is completed")