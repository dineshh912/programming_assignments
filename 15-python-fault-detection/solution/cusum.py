#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 21T3 Assignment 1 

Template file for cusum()

@author: 
"""

def cusum(conc_lpr):
    '''
        This function calculates cumsum of given conc log_prob_ratio 
        input : conc_lpr list of conc_log_prob_ratio
        output : conc_cusum list

        formula: 

            conc_cusum[0] = conc_lpr[0] if conc_lpr >=0 else 0
            conc_cumsum[k] = conc_cumsum[k-1]+conc_lpr[k] 
                            if conc_cumsum[k-1]+conc_lpr[k] >=0 else 0

    '''
    # Result will be saved on this conc_cusum list
    conc_cusum = []

    # Check first value of conc_lpr, whether it's negative number
    if conc_lpr[0] >= 0:
        conc_cusum.append(conc_lpr[0])
    else:
        conc_cusum.append(0)

    # Loop through conc_lpr; since we proceed 0th value already need to start from 1st value
    # of conc_lpr
    for k in range(1, len(conc_lpr)):
        res = conc_cusum[k-1] + conc_lpr[k]
        # Checking if the calculated value is negative
        if(res >= 0):
            conc_cusum.append(round(res,3))
        else:
            conc_cusum.append(0)
        
    return conc_cusum