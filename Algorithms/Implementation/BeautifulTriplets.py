import math
import os
import random
import re
import sys

def beautifulTriplets(d, arr):
    count, i = 0, 1
    for i in range(len(arr)):
        if arr[i]+d in arr and arr[i]+2*d in arr:
            count+=1
    return count
