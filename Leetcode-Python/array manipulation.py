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
    arr = []
    for i in range(n):
        arr.append(0)
    #print(arr)
    for a,b,k in queries:
        a1 = a-1
        b1 = b-1
        #print('a1',a1)
        #print('b1',b1)
        for i in range(a1,b1+1,1):
            #print(i)
            arr[i] = arr[i] + k
            #print(arr[i])
            
    sorted_arr = sorted(arr, reverse=True)
    
    return sorted_arr[0]

    
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

