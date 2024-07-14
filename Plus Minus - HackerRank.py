import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n = len(arr)
    pos_count = sum(1 for x in arr if x > 0)
    neg_count = sum(1 for x in arr if x < 0)
    zero_count = sum(1 for x in arr if x == 0)
    
    pos_ratio = pos_count / n
    neg_ratio = neg_count / n
    zero_ratio = zero_count / n
    
    # Print the results with 6 decimal places
    print(f"{pos_ratio:.6f}")
    print(f"{neg_ratio:.6f}")
    print(f"{zero_ratio:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
