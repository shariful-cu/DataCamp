#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 23:11:04 2018

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



#analysis



# Convert the target to categorical: target
target = to_categorical(lab_train)


def get_new_model(input_shape = (n_cols,)):
    # Set up the model
    model = Sequential()
    
    # Add the first layer
    model.add(Dense(100, activation = 'relu', input_shape = input_shape))
    
    # Add the second layer
    model.add(Dense(100, activation = 'relu'))
    
    # Add the output layer
    model.add(Dense(2, activation = 'softmax'))
    return (model)



# Create list of learning rates: lr_to_test
lr_to_test = [0.000001, 0.01, 1]
#lr_to_test = [0.01]

early_stopping_monitor = EarlyStopping(patience=2)

# Loop over learning rates
for lr in lr_to_test:
    print('\n\nTesting model with learning rate: %f\n'%lr )
    
    # Build new model to test, unaffected by previous models
    model = get_new_model()
    
    # Create SGD optimizer with specified learning rate: my_optimizer
    my_optimizer = SGD(lr=lr)
    
    # Compile the model
    model.compile(optimizer = my_optimizer, loss = 'categorical_crossentropy', metrics = ['accuracy'])
    
    # Fit the model
    model.fit(predictors, target, validation_split = 0.3, callbacks = [early_stopping_monitor], epochs=10)
# =============================================================================
# =============================================================================
# =============================================================================
   #
   #
   ##compile & fit the model
   #optimiz
   ## Compile the model
#   model.compile(optimizer = 'sgd', loss = 'categorical_crossentropy', metrics = ['accuracy'])
   #
   ## Fit the model
#   model.fit(predictors, target)
   
   ##save the model
#   filePath = '/Users/Shariful/Documents/DataCamp/ADFA-LD(tf-idf)/model_dl_2hl.h5'
#   model.save(filePath)
   #
   ##load the model
#   my_model = load_model(filePath)
   #
   ## Calculate predictions: predictions
#   predictions = model.predict(df_test)
   #
   ## Calculate predicted probability of survival: predicted_prob_true
   #predicted_prob_true = predictions[:,1]
   #
   ### print predicted_prob_true
   ##print(predicted_prob_true)
   =============================================================================
# =============================================================================
# 
# =============================================================================
