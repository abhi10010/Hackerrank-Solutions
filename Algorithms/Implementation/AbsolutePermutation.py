import math
import os
import random
import re
import sys

def absolutePermutation(n, k):
    a = []
    for i in range(1, n+1):
        a.append(i)
    if k ==0:
        return a
    elif (n/k)%2!=0:
        return [-1]
    else:
        for i in range(0,n,2*k):
                temp = a[i:i+k]
                a[i:i+k]=a[i+k:i+(2*k)]
                a[i+k:i+(2*k)] = temp
        return a
