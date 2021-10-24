#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Asssignment 1 (21T3) 

You can use this file to test your detect_fault_main().

This file contains only one test case which is the same as the sample
test code in the project specifications. 

You can use this file to come out with additional tests. 
"""

# %% Test data and parameters 

# The conc signal 
conc_signal = [6.55, 6.40, 6.76, 6.45, 6.87, 6.92, 6.45, 7.36, 7.41, 6.67]

# Parameters used to detect whether there is a fault in the conc_signal
conc_range = [6.1, 6.9]
conc_var = 0.5 
conc_cusum_limit = 1.55 

# The flow_signal
flow_signal = [22.94, 23.07, 23.97, 23.9, 24.05, 23.65, 23.78, 23.78, 23.94, 23.91]

# The parameters used to detect whether there is a fault in the flow_signal
flow_range = [22.5, 23.5]
flow_control_window = 3

# %% Call the fault detection function     
import detect_fault_main as df    
fault_type_your = df.detect_fault_main(conc_signal,conc_range,conc_var,
                         conc_cusum_limit,flow_signal,flow_range,flow_control_window)

# The fault type 
fault_type_expected = 'flow and conc faults'

print('Your function returns:',fault_type_your)
print('The expected answer is:',fault_type_expected)

comparison_output = fault_type_your == fault_type_expected

if comparison_output:
    print('Your answer is correct')
else:
    print('Your answer is NOT correct')        
        
