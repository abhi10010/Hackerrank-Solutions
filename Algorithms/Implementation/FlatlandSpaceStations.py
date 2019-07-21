import math
import os
import random
import re
import sys

def flatlandSpaceStations(n, c):
    a = list()
    if n==len(c):
        return 0
    else:
        if len(c)>1:
            c.sort()
            for i in range(len(c)-1):
                a.append(int(abs(c[i]-c[i+1])/2))
            a.append(c[0])
            a.append(int(abs(c[-1]-n+1)))
            print(a)
            return max(a)
        else:
            for i in range(n):
                a.append(int(abs(c[0]-i)))
            return max(a)
