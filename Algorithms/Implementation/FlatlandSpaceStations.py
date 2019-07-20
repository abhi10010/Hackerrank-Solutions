import math
import os
import random
import re
import sys

def flatlandSpaceStations(n, c):    
    a = list()
    if n==len(c):
        return 0
    for i in range(n):
            a.append(min((abs(i-c[k]) for k in range(len(c)))))
    return max(a)
