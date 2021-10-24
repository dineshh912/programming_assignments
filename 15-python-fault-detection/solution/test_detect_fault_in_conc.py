#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (21T3) 

You can use this file to test your detect_fault_in_conc().

This file containing four test cases which you can choose by
adjusting the variable test_index in Line 18. 

You can use this file to come out with additional tests. 
"""

# %% import 
import detect_fault_in_conc as detect
import math 

# %% Tests 
test_index = 3 # Can be 0, 1, 2 or 3 

if test_index == 0:
    conc_cusum = [0.59, 1.44, 2.16, 1.34, 2.39, 3.22, 3.89, 5.17, 6.51, 6.82]
    conc_cusum_limit = 3.1
    time_fault_detected_expected = 5
    total_fault_time_expected = 5
elif test_index == 1: 
    conc_cusum = [0.59, 1.44, 2.16, 1.34, 2.39, 3.22, 3.89, 5.17, 6.51, 6.82]
    conc_cusum_limit = 1.9
    time_fault_detected_expected = 2
    total_fault_time_expected = 7
elif test_index == 2: 
    conc_cusum = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.12, 2.14, 2.62, 6.05]
    conc_cusum_limit = 2.5
    time_fault_detected_expected = 8
    total_fault_time_expected = 2
elif test_index == 3: 
    conc_cusum = [2.19, 2.16, 2.28, 2.01, 0.0, 0.06, 0.0, 0.18, 0.0, 1.47]
    conc_cusum_limit = 3.7
    time_fault_detected_expected = math.inf  
    total_fault_time_expected = 0

# %% Plotting
# 
# You can use the following line of code to plot what the cusim signal
# looks like respect to the threshold used for fault detection
#
# Comment the code out for plotting 
# 
# import matplotlib.pyplot as plt

# plt.plot(conc_cusum)
# plt.axhline(conc_cusum_limit,linestyle='--',color='r')
# plt.title('cusum for test case '+ str(test_index))   
# plt.show()

# %% Run the function and check the answers     
    
time_fault_detected_your, total_fault_time_your = \
    detect.detect_fault_in_conc(conc_cusum, conc_cusum_limit)

print('For the computation of the time at which fault is detected:')
print('\tYour function returns:',time_fault_detected_your)
print('\tThe expected answer is:',time_fault_detected_expected)

comparison_time_fault_detected = time_fault_detected_your == time_fault_detected_expected

if comparison_time_fault_detected:
    print('\tYour answer for the first output is correct')
else:
    print('\tour answer for the first output is NOT correct')        

print('\n') # Print a blank line         
print('For the computation of the total fault time:')
print('\tYour function returns:',total_fault_time_your)
print('\tThe expected answer is:',total_fault_time_expected)

comparison_total_fault_time_expected = total_fault_time_your == total_fault_time_expected

if comparison_total_fault_time_expected:
    print('\tYour answer for the second output is correct')
else:
    print('\tYour answer for the second output is NOT correct')        