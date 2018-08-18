#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 00:46:34 2018

*********  writing a simple lambda function and calling this function **********


@author: Shariful
"""

add_bangs = lambda a: a + '!!!'

add_bangs('hello')

"""
*********  convert this simple function into a lambda function **********
def echo_word(word1, echo):
    words = word1 * echo
    return words

@author: Shariful
"""

# Define echo_word as a lambda function: echo_word
echo_word = lambda word, echo: word * echo

# Call echo_word: result
result = echo_word('hey', 5)

# Print result
print(result)


""" 
**   Map() and lambda functions **
map the functionality of the add_bangs() function you defined in previous
exercises over a list of strings
"""

# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda spell: spell * '!!!', spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list = shout_spells.

# Convert shout_spells into a list and print it
print(list(shout_spells_list))

nums = [3, 4, 5]

square_all = map(lambda num: num ** 2, nums)

print(list(square_all))



























