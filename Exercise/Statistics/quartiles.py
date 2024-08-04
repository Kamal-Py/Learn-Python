#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def median(arr):

    sorted_value = sorted(arr)
    N = len(arr)
    index_for_median = (N-1) / 2

    if N % 2 == 0:
        mid_value = (sorted_value[int(index_for_median-0.5)]+sorted_value[int(index_for_median+0.5)])/2
        return math.ceil(mid_value)
    else:
        mid_value = sorted_value[int(index_for_median)]
        return math.ceil(mid_value)





def quartiles(arr):
    # Write your code here
    INTEGER_ARRAY = []
    middle_index = len(arr) / 2
    lower_quad = []
    sorted_array = sorted(arr)

    for i in range(int(middle_index)):
            lower_quad.append(sorted_array[i])
    
    lower_quad_value = median(lower_quad)


    median_value = median(sorted_array)


    upper_quad = []
    for i in range(math.ceil(middle_index), len(arr)):
         upper_quad.append(sorted_array[i])

    upper_quad_value = median(upper_quad)


    INTEGER_ARRAY.append(lower_quad_value)
    INTEGER_ARRAY.append(median_value)
    INTEGER_ARRAY.append(upper_quad_value)
    return INTEGER_ARRAY

if __name__ == '__main__':
    # fptr = open(os.environ["text_files\\quartiles.txt"], 'w')
    with open("text_files\\quartiles.txt", mode="w") as file:
        n = int(input().strip())

        data = list(map(int, input().rstrip().split()))

        res = quartiles(data)
        file.write('\n'.join(map(str, res)))
        file.write('\n')
