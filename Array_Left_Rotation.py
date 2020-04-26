#!/bin/python3
import math
import os
import random 
import re
import sys

# this function push each element of the array to the left!

def rot_left(a,n,d):
    for i in range(d):
        temp = a[0]
        a.remove(a[0])
        a.append(temp)
    return a
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'W')
    nd  = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int,input().rstrip().split()))
    result = rot_left(a,d,n)
    fptr.write(' '.join(map(str,result)))
    fptr.write('\n')
    fptr.close()


