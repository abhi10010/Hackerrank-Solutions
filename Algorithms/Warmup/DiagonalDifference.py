import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    d1 = 0
    d2 = 0          
    for r in range (0,len(arr)):
        for c in range(0,len(arr)):
            if r == c:
                d1 += arr[r][c]
            if r + c == len(arr)-1:
                d2 += arr[r][c]
    if d1>d2:
        res = d1 - d2
    if d2>d1:
        res = d2 - d1
    if d1==d2:
        res = 0
    return res
