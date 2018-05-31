#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 19:08:50 2018

@author: Shariful
"""

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
file_path = '/Users/Shariful/Documents/SysCallDataset/PreparedData/ADFA-LD/tf.idf_vector/3gram/normal.csv'
adfa_ld = pd.read_csv(file_path)
subset = adfa_ld.iloc[:1,0:5]
subset1 = adfa_ld[:1,0:5]
# Print out cars
