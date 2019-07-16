import math
import os
import random
import re
import sys

def serviceLane(width, cases):
    ans = list()
    for x,y in cases:
        w = None
        for i in range(x,y+1):
            if w==None or w>width[i]:
                w=width[i]
        ans.append(w)
    return ans
