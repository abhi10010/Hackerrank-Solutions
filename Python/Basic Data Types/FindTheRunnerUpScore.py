import math
import os
import random
import re
import sys

def sec_small(arr):
    
    diff=list()
    smallest = None
    
    for i in arr:
        diff.append(abs(i-max(arr)))
    
    for i in diff:
        if (smallest == None or smallest>i) and i!=0:
            smallest=i
    
    pos = diff.index(smallest)
    print(arr[pos])

if __name__ == '__main__':
    
    n = int(input())
    arr = list(map(int, input().split()))
    sec_small(arr)
    
