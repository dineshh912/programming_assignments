#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 21T3 Assignment 1 

Template file for calc_log_prob_ratio()

@author: 
"""

def calc_log_prob_ratio(measurement, conc_range, conc_var):
        '''
        This Function calcualtes log prob ratio c for single
        measurement
        Input : measurement c
                conc_range list
                conc_var
        output : log prob ratio c 

        formula : log-prob-ratio c = ((conc_range[1] - conc_range[0])/2*v)\
                  (2c-conc_range[0]-conc_range[1])
        '''
        # difference between conc_range
        numerator_calc  = conc_range[1] - conc_range[0]
        denaminator_calc = 2* conc_var
        # calculate log_prob_ratio c
        log_prob_ratio = (numerator_calc / denaminator_calc)*\
                         (2 * measurement - conc_range[0] - conc_range[1])
        # Return result round with 2 digit
        return round(log_prob_ratio, 2)