import math
import os
import random
import re
import sys

def plusMinus(arr):
    r_neg = 0
    r_pos = 0
    r_zer = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            r_zer += 1
            continue
        if arr[i] > 0:
            r_pos += 1
            continue
        if arr[i] < 0:
            r_neg += 1
            continue
    print("%.6f" %float(r_pos/len(arr)))
    print("%.6f" %float(r_neg/len(arr)))
    print("%.6f" %float(r_zer/len(arr)))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
