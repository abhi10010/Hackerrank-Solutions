import math
import os
import random
import re
import sys

def cutTheSticks(arr):
    
    ans=list()
    n=len(arr)
    while n>0:
        count, zero = 0,0
        smallest = min(arr)
        arr[:] = [x - smallest for x in arr]
        for i in range (len(arr)):
            if arr[i]>=0:
                count+=1
            if arr[i]==0:
                zero+=1
        ans.append(count)
        for i in range(0,zero):
            arr.remove(0)
        n=len(arr)
    return ans
