#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 02:16:00 2018

@author: Shariful
"""

import pandas as pd

# Import the cars.csv data: cars
file_path = '/Users/Shariful/Documents/CyberAttackDatasets/PowerSystemData/binaryAllNaturalPlusNormalVsAttacks/data1.csv'
powerdb = pd.read_csv(file_path)

#accessing subset from the whole powerdb dataset
powerdb = powerdb.iloc[:1,:]

##accessing all column names
#for colname in powerdb :
#    print(colname)
#
##accessing each row
#for lab, row in powerdb.iterrows() :
#    print(lab)
#    print(row)
    
#    
## Adapt for loop
#for lab, row in powerdb.iterrows() :
#    print(str(lab) + ': ' + str(row['R1-PA1:VH']))    
#    
    
# Adding new column using .apply(apply_function name)
for lab, row in powerdb.iterrows() :
    powerdb['R1-PA1:VH_Int'] = powerdb['R1-PA1:VH'].apply(int)
    
print(powerdb)       


