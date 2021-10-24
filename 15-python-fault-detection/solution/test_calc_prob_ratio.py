#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (21T3) 

You can use this file to test your calc_log_prob_ratio().

This file containing three test cases which you can choose by
adjusting the variable test_index in Line 18. 

You can use this file to come out with additional tests. 
"""

# %% import 
import calc_log_prob_ratio as clpr

# %% Tests 
test_index = 0 # Can be 0, 1 or 2

if test_index == 0:
    measurement = 6
    conc_range = [3, 7]
    conc_var = 2
    expected_answer = 2.0
elif test_index == 1: 
    measurement = 6.2
    conc_range = [6.1, 6.8]
    conc_var = 0.3
    expected_answer = -0.58333
elif test_index == 2: 
    measurement = 6.9
    conc_range = [6.0, 7.1]
    conc_var = 0.4
    expected_answer = 0.9625

# %% Run the function and check the answers     
    
your_answer = clpr.calc_log_prob_ratio(measurement, conc_range, conc_var)

print('Your function returns',your_answer)
print('The expected answer is',expected_answer)

TOL = 1e-5
comparison_output = abs(your_answer-expected_answer) <= TOL 

if comparison_output:
    print('Your answer is correct')
else:
    print('Your answer is NOT correct')        
        
