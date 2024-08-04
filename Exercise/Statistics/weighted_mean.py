#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    # Write your code here
    # X -> List  
    # W -> List --> Sum of W
    # weighted_value -> Loops --> index multiply -> list append
    weighted_value = []

    for i in range(len(X)):
        weighted_value.append(int(X[i]*W[i]))

    sum_of_w = sum(W)
    sum_of_xw = sum(weighted_value)
    mean = sum_of_xw/sum_of_w
    print("{:.1f}".format(mean))


    

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
