#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 19:00:56 2018

Problem Statement:
    What's the estimated chance (porbability) that you'll reach 60 steps high if you play
    this Empire State Building game? 
    
@author: Shariful
"""

# Initialization
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

# Initialize all_walks
all_walks = []

# Simulate random walk 250 times
for i in range(250) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        
        # Implement clumsiness
        if (np.random.rand() <= 0.001) :
            step = 0
        
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)


# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
#plt.plot(np_aw_t)
#plt.show()

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()

#compute chance (porbability) that you'll reach 60 steps high
ends_60 = np.sum(ends >= 60) / 250

