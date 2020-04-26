# 6x6 materix max hourglass sum
#!/bin/python3

import os
import sys
import re
import random

def hourglass_sum(arr,i,j):

    a = arr[i][j]
    b = arr[i][j+1]
    c = arr[i][j+2]
    d = arr[i+1][j+1]
    e = arr[i+2][j]
    f = arr[i+2][j+1]
    g = arr[i+2][j+2]

    return (a+b+c+d+e+f+g)

if __name__ == '__main__':

    arr =[]
    for _ in range(6):

        arr.append(list(map(int,input().rstrip().split())))

    res = []
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):

            summ = hourglass_sum(arr,i,j)
            res.append(summ)

    print(max(res))
    
            

