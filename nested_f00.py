#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 10:14:37 2018

In this exercise, inside a function three_shouts(), you will define a nested
function inner() that concatenates a string object with !!!. three_shouts()
then returns a tuple of three elements, each a string concatenated with !!! 
using inner(). Go for it!

@author: Shariful
"""

# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))
