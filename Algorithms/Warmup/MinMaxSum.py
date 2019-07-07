import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    largest = None
    smallest = None
    for i in range(len(arr)):
        if smallest == None:
            smallest = arr[i]
        if smallest > arr[i]:
            smallest = arr[i]
        if largest == None:
            largest = arr[i]
        if largest < arr[i]:
            largest = arr[i]
    print(sum-largest, sum-smallest)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
