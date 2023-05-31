# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if(abs(x-z) == abs(y-z)):
        result = 'Mouse C'
    elif(abs(x-z) < abs(y-z)):
        result = 'Cat A'
    else:
        result = 'Cat B'  
    return result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = 1
    # myinput = '1 2 3'
    myinput = '1 3 2'

    for q_itr in range(q):
        xyz = myinput.split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        # fptr.write(result + '\n')
        print(result)

    # fptr.close()
    print('fin')
