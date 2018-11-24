#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 20:08:42 2018

@author: Shariful
"""

# Import necessary modules
import pandas as pd
import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical
from keras.models import load_model
# Import the SGD optimizer
from keras.optimizers import SGD
from keras.callbacks import EarlyStopping
#from keras.models import LSTM


#preparing data
trn_nml = pd.read_csv('/Users/Shariful/Documents/DataCamp/ADFA-LD(tf-idf)/train_normal.csv')
test_atk = pd.read_csv('/Users/Shariful/Documents/DataCamp/ADFA-LD(tf-idf)/test_attack.csv')
test_nml = pd.read_csv('/Users/Shariful/Documents/DataCamp/ADFA-LD(tf-idf)/test_normal.csv')

df_train = pd.concat([trn_nml, test_atk.head(40)], ignore_index=True)
lab_train = pd.concat([pd.DataFrame([0] * len(trn_nml)), pd.DataFrame([1] * 40)], ignore_index=True)

df_test = pd.concat([test_nml, test_atk.tail(20)], ignore_index=True)
lab_test = pd.concat([pd.DataFrame([0] * len(test_nml)), pd.DataFrame([1] * 20)], ignore_index=True)

predictors = df_train.as_matrix()
n_cols = predictors.shape[1]
