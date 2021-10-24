#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (21T3) 

You can use this file to test your calc_signal_log_prob_ratio().

This file containing three test cases which you can choose by
adjusting the variable test_index in Line 18. 

You can use this file to come out with additional tests. 
"""

# %% import 
import calc_signal_log_prob_ratio as cslpr

# %% Tests 
test_index = 0 # Can be 0, 1 or 2 

if test_index == 0:
    conc_signal = [6, 5, 4, 7]
    conc_range = [3, 7]
    conc_var = 2
    expected_answer = [2.0, 0.0, -2.0, 4.0]
elif test_index == 1: 
    conc_signal = [15.62, 8.8, 11.69, 18.0, 16.14]
    conc_range = [6.1, 6.8]
    conc_var = 0.5
    expected_answer = [12.838, 3.29, 7.336, 16.17, 13.566]
elif test_index == 2: 
    conc_signal = [5.55, 6.63, 0.39, 9.38, 2.51, 4.42, 7.11]
    conc_range = [6.1, 6.8]
    conc_var = 2.5
    expected_answer = [-0.252, 0.0504, -1.6968, 0.8204, -1.1032, -0.5684, 0.1848]

# %% Run the function and check the answers     
    
your_answer = cslpr.calc_signal_log_prob_ratio(conc_signal, conc_range, conc_var)

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

      
        
