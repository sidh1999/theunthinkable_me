#!/bin/python3

#import pow
=======
import randomness

import math
import os
import random
import re
import sys
import keras 
import numpy
import pandas

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    temp1=2
    total=2
    for i in range (1,n):
        temp=temp1*3
        temp1=math.floor(temp/2)
        total+=temp1
    return total    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
main.save( code of conduct)
