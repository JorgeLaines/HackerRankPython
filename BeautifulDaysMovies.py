# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def reverseNumber(num):
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

def beautifulDays(i, j, k):
    beautifulDaysCounter = 0
    for day in range(i, j + 1):
        if((day - reverseNumber(day)) % k == 0):
            beautifulDaysCounter += 1
    return beautifulDaysCounter

if __name__ == '__main__':
    fptr = open('BeautifulDaysMovies.txt', 'w')

    myInput = '20 23 6'

    first_multiple_input = myInput.rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
