#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 11:07:02 2018

********* Twitter language analysis with default argument **********

in the previous chapter where you did a simple Twitter analysis by developing
 a function that counts how many tweets are in certain languages. The output
 of your function was a dictionary that had the language as the keys and the
 counts of tweets in that language as the value.

In this exercise, we will generalize the Twitter language analysis that you did
 in the previous chapter. You will do that by including a default argument that
 takes a column name.

@author: Shariful
"""

# ===== Define count_entries() ======
def count_entries(df, col_name = 'lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1

        # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count
# =====End of Define count_entries() ======

import pandas as pd

tweets_df = pd.read_csv('tweets.csv')

# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'source')

# Print result1 and result2
print(result1)
print(result2)
