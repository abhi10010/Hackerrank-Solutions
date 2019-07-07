import os
import sys
import math

def pageCount(n, p):
    #
    # Write your code here.
    #
    if n%2==1:
        e1 = n-1
        e1 = e1-p
        e1 = e1/2
    else:
        e1 = n-p
        e1 = e1/2
    s1 = p-1
    s1 = s1/2
    end = math.ceil(e1)
    start = math.ceil(s1)
    if end>start:
        return int(start)
    else:
        return int(end)
