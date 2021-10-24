#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (21T3) 

You can use this file to test your detect_fault_main().
All the cases in this file are expected to return the output 'invalid parameters'

This file containing three test cases which you can choose by
adjusting the variable test_index in Line 19. 

You can use this file to come out with additional tests. 
"""

# %% import 
import detect_fault_main as df

# %% Tests 
test_index = 2 # Can be 0, 1 or 2 

if test_index == 0:
    conc_signal = [6.87, 7.06, 6.96, 5.87, 7.2, 7.04, 6.93, 7.36, 7.41, 6.67]
    conc_range = [6.8, 6.1] # invalid 
    conc_var = 0.5    
    conc_cusum_limit = 3.1
    flow_signal = [22.94, 23.07, 22.97, 22.9, 23.05, 22.65, 22.78, 22.78, 22.94, 22.91]
    flow_range = [22.5, 23.5]
    flow_control_window = 3
    expected_answer = 'invalid parameters'
elif test_index == 1: 
    conc_signal = [6.24, 5.66, 6.12, 5.15, 6.38, 6.43, 7.2, 7.14, 6.8, 8.64]
    conc_range = [6.1, 6.9]
    conc_var = 0.5 
    conc_cusum_limit = 2.5 
    flow_signal = [22.94, 23.07, 23.97, 23.9, 24.05, 23.65, 23.78, 23.78, 23.94, 23.91]
    flow_range = [22.5, 23.5]
    flow_control_window = 5.2 # invalid
    expected_answer = 'invalid parameters'
elif test_index == 2: 
    conc_signal = [6.78, 6.04, 6.09, 5.96, 5.0, 6.07, 5.25, 6.11, 5.72, 6.54, 5.91, 6.01]
    conc_range = [5.3, 6.8]
    conc_var = 0.5 
    conc_cusum_limit = 2.6 
    flow_signal = [23.27, 23.14, 22.69, 23.0, 23.12, 22.86, 23.05, 23.02, 23.0, 22.97, 23.09, 23.24]
    flow_range = [22.5, 23.5, 24.5] # invalid 
    flow_control_window = 3
    expected_answer = 'invalid parameters'

# %% Run the function and check the answers     
    
your_answer = df.detect_fault_main(conc_signal,conc_range,conc_var,conc_cusum_limit, 
                   flow_signal,flow_range,flow_control_window)

print('Your function returns:',your_answer)
print('The expected answer is:',expected_answer)

comparison_output = your_answer == expected_answer

if comparison_output:
    print('Your answer is correct')
else:
    print('Your answer is NOT correct')        
        
