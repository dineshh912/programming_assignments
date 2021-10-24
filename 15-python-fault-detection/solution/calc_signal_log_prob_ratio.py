#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 21T3 Assignment 1 

Template file for calc_signal_log_prob_ratio()

@author: 
"""

def calc_signal_log_prob_ratio(conc_signal,conc_range,conc_var):
    '''
        Function to calculate log_prob_ratio of list values
        Input : conc_signal - list of conc_signal
                conc_range - list of range
                conc_var
        output: log-prob-ratio
    '''
    import calc_log_prob_ratio as clpr

    # Save result of each signal value in this list
    conc_lpr = []

    # loop through list to calculate log_prob_ratio
    for i in conc_signal:
        log_prob_ratio = clpr.calc_log_prob_ratio(i, conc_range, conc_var)

        conc_lpr.append(log_prob_ratio)
    
    # Return list of calc_log_prob_ratio
    return conc_lpr
 