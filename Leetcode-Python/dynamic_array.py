#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    arr = []
    answer = []
    last_ans = 0
    for i in range(n):
        arr.append([])
    
    for query in queries:
        #print('q1',query)
        app_or_ass = query[0]
        #print('ap',app_or_ass)
        x = query[1]
        y = query[2]
        
        if app_or_ass == 1:
            index1 = (x ^ last_ans) % n
            #print('i', index1)
            arr[index1].append(y) 
            #print('arr',arr[index1])
        elif app_or_ass == 2:
            index1 = (x ^ last_ans) % n
            #print('i2', index1)
            #print('arr2',arr[index1])
            last_ans = arr[index1][y % len(arr[index1])]
            #print('ans',last_ans)
            answer.append(last_ans)
    
    return answer
         
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

