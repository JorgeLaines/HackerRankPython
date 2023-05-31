# https://www.hackerrank.com/challenges/strange-advertising/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def viralAdvertisingRecursive(n):
    if(n > 1):
        previousLiked, previousCumulative = viralAdvertisingRecursive(n - 1)
        currentLiked = math.floor(previousLiked * 3 / 2)
        return currentLiked, previousCumulative + currentLiked
    else:
        return 2, 2
    
def viralAdvertising(n):
    liked, cumulative = viralAdvertisingRecursive(n)
    return cumulative

if __name__ == '__main__':
    fptr = open('viralAdvertising.txt', 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()