#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 21T3 Assignment 1 

Template file for detect_fault_main

@author: 
"""

def detect_fault_main(conc_signal,conc_range,conc_var,conc_cusum_limit, 
                  flow_signal,flow_range,flow_control_window):
    
    import classify_fault as classify
    
    # If all below cnonditions satisfied procced to calculate fault
    if len(conc_range) == 2 and conc_range[0] < conc_range[1] \
        and len(flow_range) == 2 and flow_range[0] < flow_range[1] \
        and conc_var > 0 and conc_cusum_limit > 0 and \
        isinstance(flow_control_window, int):

        result = classify.classify_fault(conc_signal,conc_range,conc_var,conc_cusum_limit, 
                                        flow_signal,flow_range,flow_control_window)
    else:
        result = "invalid parameters"
    
    return result
    
