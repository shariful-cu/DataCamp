#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 22:48:23 2018

building a dictionary with keys the names of languages and values the number of
tweets in the given language

@author: Shariful
"""

# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
df = pd.read_csv('tweets.csv')

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in DataFrame
for entry in col :

    # If the language is in langs_count, add 1
    if entry in langs_count.keys():
        langs_count[entry] = langs_count[entry] + 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1

# Print the populated dictionary
print(langs_count)