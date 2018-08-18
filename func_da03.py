#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 10:59:19 2018

********* Function with variable-length keyword arguments (**kwargs) **********

in this exercise to define a function that accepts a variable number of keyword
 arguments. The function simulates a simple status report system that prints
 out the status of a character in a movie.

@author: Shariful
"""

# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)

    print("\nEND REPORT")

# First call to report_status()
report_status(name="luke", affiliation="jedi", status="missing")

# Second call to report_status()
report_status(name="anakin", affiliation="sith lord", status="deceased")
