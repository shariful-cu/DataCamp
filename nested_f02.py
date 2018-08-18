#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 10:31:39 2018

In this exercise, you will use the keyword nonlocal within a nested function
 to alter the value of a variable defined in the enclosing scope.

@author: Shariful
"""

# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""
    
    # Concatenate word with itself: echo_word
    echo_word = word + word
    
    #Print echo_word
    print(echo_word)
    
    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""    
        #Use echo_word in nonlocal scope
        nonlocal echo_word
        
        #Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'
    
    # Call function shout()
    shout()
    
    #Print echo_word
    print(echo_word)

#Call function echo_shout() with argument 'hello'    
echo_shout('hello')
