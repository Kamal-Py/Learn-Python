#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs


def median(arr):
    middle_index = (len(arr) -1 )/ 2
    if len(arr) % 2 == 0:
        mid_value = (arr[int(middle_index-0.5)]+arr[int(middle_index+0.5)])/2
        return math.ceil(mid_value)
    else:
        mid_value = arr[int(middle_index)]
        return math.ceil(mid_value)




def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    arr = []
    for i in range(len(values)):
        for _ in range(freqs[i]):
            arr.append(values[i])

    sorted_array = sorted(arr)
    middle_index = len(sorted_array) // 2

    lower_quad = []
    for i in range(middle_index):
        lower_quad.append(sorted_array[i])
    Q1 = median(lower_quad)
    upper_quad = []
    for j in range(middle_index + 1, len(sorted_array)):
        upper_quad.append(sorted_array[j])
    Q3 = median(upper_quad)
    inter_quartile = Q3 - Q1

    print("{:.1f}".format(inter_quartile))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
