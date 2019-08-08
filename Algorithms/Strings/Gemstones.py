import math
import os
import random
import re
import sys

def gemstones(arr):
    count = 0
    for i in range(len(arr)):
        arr[i]= set(arr[i])
    for i in arr[0]:
        flag = 0
        for j in range(1, len(arr)):
            if i not in arr[j]:
                flag = 1
                break
        if flag == 0:
            count+=1
    return(count)
