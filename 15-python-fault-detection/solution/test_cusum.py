#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (21T3) 

You can use this file to test your cusum().

This file containing three test cases which you can choose by
adjusting the variable test_index in Line 18. 

You can use this file to come out with additional tests. 
"""

# %% import 
import cusum as cs

# %% Tests 
test_index = 0 # Can be 0, 1 or 2 

if test_index == 0:
    conc_lpr = [1, 3, 2, 4]
    expected_answer = [1, 4, 6, 10]
elif test_index == 1: 
    conc_lpr = [2, -1, 3, -8, -1, -2, 3, 4]
    expected_answer = [2, 1, 4, 0, 0, 0, 3, 7]
elif test_index == 2: 
    conc_lpr = [-1.6, -1.3, 2.5, -3.1, -1.7, 4.2, 3.6, -1.2, -0.4, 0.7]
    expected_answer = [0, 0, 2.5, 0, 0, 4.2, 7.8, 6.6, 6.2, 6.9]

# %% Run the function and check the answers     
    
your_answer = cs.cusum(conc_lpr)

print('Your function returns',your_answer)
print('The expected answer is',expected_answer)

TOL = 1e-5

try:
    if len(your_answer) == len(expected_answer):

        comparison_output = [True if abs(y-e) <= TOL else False for 
                             y,e in zip(your_answer,expected_answer)]
        
        if all(comparison_output):
            print('Your answer is correct')
        else:
            print('Your answer is NOT correct')  
    else:
        print('The number of list entries in your answer is different from expected.')        
except:
    print('Your answer is NOT correct.')
    print('Probably because your answer is not a list but can be other problems.')
    
        
