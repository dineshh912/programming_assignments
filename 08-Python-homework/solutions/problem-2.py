import random as rn
import numpy as np

""" Problem 2 """
def running_average(xlist,per): 
    """
        Compute thr running average 
        Args: xlist: contain list of randomly generated number
              per : Period which need to be calculeted
        Returns: list contains moving average 
    """
    # np.convolve returns discret, linear convolution of two 1-d sequence
    '''
        Input list convolving with a sequence of np.ones. the np.ones length is equal to the period we want.
        so, the input sequence took x list and period and creates sequence of ones lenght of period.
        we choose mode is valid. so that the convolution product will give only for the values the sequence overlapping.
    '''
    result = np.convolve(xlist, np.ones(per), 'valid') / per

    # Rounding result to two digit and return as list
    return  list(np.around(result, decimals = 2))


if __name__ == "__main__":

    #Generate random data sequence
    data = [rn.randint(1, 100) for i in range(10)]
    print(data)
    period = 3 # time period for running avg (3 day average)
    run_avg = running_average(data,period)

    print(f"The {period}-day running average is: {run_avg}")
