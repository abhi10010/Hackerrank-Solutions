import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    res = [0,0]
    for i in range(len(a)):
        if a[i]>b[i]:
            res[0] += 1
        if b[i]>a[i]:
            res[1] += 1
    return res
