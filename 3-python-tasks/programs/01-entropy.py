import math
from collections import Counter


def log_2(n):
    """
        This function calculates log base 2 of the integer
        --input
            n - interger
        -- output
            log base 2 value

        we can use either math.log(number, 2) or math.log2(number)
        to calculate log base 2
    """
    return math.log(n, 2)


def makeProbability(xlst):
    """
        This function will calculate probability distribution of each unique element
        in the list
        -- input 
            xlst - list of immutable objects
        -- output
            prod - list of probablity of each unique element
    """
    value_count = Counter(xlst)
    probd = []

    for el, count in value_count.items():
        val = count / len(xlst)
        probd.append(val)

    return probd


def entropy(xlst):
    """
        This fuction will calculate entropy based on the probablity distrubution list.

        --input
            xlst - list of immutable object probablity distribution

        -- output
            entropy - as a value
    """
    ent  = 0
    for i in xlst:
        ent -= i * log_2(i)
    return ent


if __name__ == '__main__':

    x = ["a","b","a","c","c","a"]
    print(entropy(makeProbability(x)))