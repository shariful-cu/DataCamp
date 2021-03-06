#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 02:02:44 2018

@author: Shariful
"""

# =============================================================================
# -*- Important message -*-
"""
Great! Notice that the order of the printouts doesn't correspond with the
order used when defining europe. Remember: dictionaries are inherently 
unordered!
"""
# =============================================================================


world = {"afganistan":30.55,
         "albania":2.77,
         "algeria":39.21
        }

for key, value, in world.items() :
    print(key + " -- " + str(value))
    
    
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe (dictionaries )
for key, value, in europe.items() :
    print("the capital of " + key + " is " + value)

