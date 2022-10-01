#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):

    array = [0 for _ in range(n)]
    for query in queries:
        low = query[0] - 1
        high = query[1] -1 
        weight = query[2]
        print('low', low)
        print('high', high)
        array[low] += weight
        print('alow', array[low])
        if high < n - 1:
            array[high + 1] -= weight
            print('ahigh', array[high+1])
        print('array',array)
     
    print('array_after_all',array)
    maximum = array[0]
    sum = array[0]
    for i in range(1,n):
        sum += array[i]
        maximum = max(maximum,sum)
        print(maximum)
        
    return maximum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

