#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 21T3 Assignment 1 

Template file for detect_fault_in_conc

@author: 
"""
import math

def detect_fault_in_conc(conc_cusum, conc_cusum_limit):
    '''
        This function detects fault in the list of cusum values. 
        count the total no of fault and time first fault occured. 

        input: conc_cusum - list of cusum values
        output : fault_detected_time, cusum_limit_total
    '''
    # Initialize variables to store the data
    cusum_limit_total = 0
    fault_detected_time = 0
    fault_index = []

    # loop through cusum list to check the cusum limit
    for i in range(len(conc_cusum)):
        if conc_cusum[i] >= conc_cusum_limit:
            cusum_limit_total +=1
            fault_index.append(i)
    
    # If there is no fault detected
    if cusum_limit_total == 0:
        fault_detected_time = math.inf
    else:
        fault_detected_time = fault_index[0]

    return fault_detected_time, cusum_limit_total