#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (21T3) 

You can use this file to test your detect_fault_main().
All the cases in this file have valid parameters and the function should 
determine the fault type. 

This file containing three test cases which you can choose by
adjusting the variable test_index in Line 20. 

You can use this file to come out with additional tests. 
"""

# %% import 
import detect_fault_main as df

# %% Tests 
test_index = 2 # Choose 0, 1 or 2 

# Both conc_signal and flow_signal have 100 entries each. 
# They will be loaded from files rather than listed here.  
# 
# load conc_signal and flow_signal from files
with open('conc_signal_'+str(test_index)+'.txt','r') as f:
    conc_signal = f.readlines()       
conc_signal = [float(d) for d in conc_signal]  

with open('flow_signal_'+str(test_index)+'.txt','r') as f:
    flow_signal = f.readlines()       
flow_signal = [float(d) for d in flow_signal] 

# The algorithm parameters - the same all tests  
conc_range = [5.9, 6.1]
conc_var = 0.5         
conc_cusum_limit = 3.1

flow_range = [22.5, 23.5]
flow_control_window = 10

# The expected answer 
if test_index == 0:
    expected_answer = 'conc fault only'
elif test_index == 1: 
    expected_answer = 'no faults'
elif test_index == 2:
    expected_answer = 'flow and conc faults'
    
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
        
# %% Code for plotting
"""
Since the signals are long, you can use the code below to visualise them.
The signals that you can plot are: 
      conc_signal
      conc_signal_cusum
      flow_signal

A point of interest is that if you look at the conc_singal when there is a 
fault and there isn't, you don't see much difference. The fault in the 
conc_signal is in fact very small and is not perceptible by eyes. However, 
if you look at their corresponding conc_signal_cusum, you will see that 
the cusum drifts upwards steadily later on. This is an indication of fault.
We have included this example to demonstrate how powerful it can be if you
can combine computing and maths to achieve a task which is beyond our 
visual perception. 

If you would like to see plot of the above signals, comment out the 
appropriate lines in the code below.
"""

# import matplotlib.pyplot as plt

# # conc_signal
# plt.figure(0)
# plt.plot(conc_signal)  
# plt.title('conc signal for test case'+str(test_index))

# # conc_signal_cusum (Need to load the pre-computed data from file)
# plt.figure(1)
# with open('conc_signal_cusum_'+str(test_index)+'.txt','r') as f:
#     conc_signal_cusum = f.readlines()       
# conc_signal_cusum = [float(d) for d in conc_signal_cusum]  
# plt.plot(conc_signal_cusum)
# plt.axhline(conc_cusum_limit,linestyle='--',color='r')
# plt.title('conc cusum for test case'+str(test_index)) 

# # flow_signal
# plt.figure(2)
# plt.plot(flow_signal)  
# plt.title('flow signal for test case'+str(test_index))


