#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 10:42:36 2018

********* Functions with multiple default arguments **********

defining a function with more than one default argument and then calling this
 function in various ways.

@author: Shariful
"""

# Define shout_echo
def shout_echo(word1, echo = 1, intense = False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Capitalize echo_word if intense is True
    if intense is True:
        # Capitalize and concatenate '!!!': echo_word_new
        echo_word_new = str.upper(echo_word) + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'

    # Return echo_word_new
    return echo_word_new

# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo("Hey", echo=5, intense=True)

# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo("Hey", intense=True)

# Print values
print(with_big_echo)
print(big_no_echo)