#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    add = 0
    for i in arr:
        add += i
    mean = add/len(arr)

    squared_distance = []
    for i in range(len(arr)):
        squared_distance.append((arr[i]-mean)**2)
    
    sum_of_squared_distance = 0
    for i in squared_distance:
        sum_of_squared_distance += i
    
    SD = (sum_of_squared_distance/len(arr)) ** 0.5
    print("{:.1f}".format(SD))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
