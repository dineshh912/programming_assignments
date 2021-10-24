#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 21T3 Assignment 1 

Template file for classify_fault()

@author: 
"""
import math

def classify_fault(conc_signal,conc_range,conc_var,conc_cusum_limit, 
                   flow_signal,flow_range,flow_control_window):

    """ 
        Function helps to calculate whether signal is fault or not. 
        
        input : conc_signal [list]
                conc_range [list]
                conc_var [Positive value]
                conc_cusum_limit [Positive value]
                flow signal [list]
                flow range [list]
                flow_control_window [positive values]
        
        output: return string


    """

    
    import calc_signal_log_prob_ratio as cslpr
    import cusum as cs
    import detect_fault_in_conc as detect

    # calculating signal log prob ratio
    conc_lpr = cslpr.calc_signal_log_prob_ratio(conc_signal,
                                                conc_range,
                                                conc_var)
    # Calaculating cusum for the log prob ratio
    conc_cusum = cs.cusum(conc_lpr)

    # Detecting fault
    time_fault_detected, total_fault_time = \
        detect.detect_fault_in_conc(conc_cusum, conc_cusum_limit)

    # Check if there is fault in conc
    if time_fault_detected != math.inf:

        # Get all the values in flow signal upto first detectd fault
        values_upto_time_fault_detected = flow_signal[:time_fault_detected+1]

        # Get values based on flow control window
        flow_control_window_values = values_upto_time_fault_detected[-flow_control_window:]

        # Find avergae of the flow control window values
        avg_fcw_values = round(sum(flow_control_window_values) /\
                            len(flow_control_window_values), 2)
        
        # Check whether average with in range
        if flow_range[0] <= avg_fcw_values <= flow_range[1]:
            return "conc fault only"
        else:
            return "flow and conc faults"
    else:
        return "no faults"