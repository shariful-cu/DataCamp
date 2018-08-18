#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 20:47:04 2018

@author: Shariful
"""
import numpy as np
from keras.layers import Dense
from keras.models import Sequential


predictors = np.array([[3, 5], [1, -1], [0, 0], [8, 4]])
target = np.array([5, 7, 0, 9])

# Save the number of columns in predictors: n_cols
n_cols = predictors.shape[1]

# Set up the model: model
model = Sequential()

# Add the first layer
model.add(Dense(10, activation='relu', input_shape=(n_cols,)))

# Add the second layer
model.add(Dense(10, activation='relu'))

# Add the output layer
model.add(Dense(1))


# Compile the model
model.compile(optimizer = 'adam', loss = 'mean_squared_error')

# Verify that model contains information from compiling
print("Loss function: " + model.loss)

# Fit the model
model.fit(predictors, target)