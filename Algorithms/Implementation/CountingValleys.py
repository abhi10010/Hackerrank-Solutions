import math
import os
import random
import re
import sys

def countingValleys(n, s):
    count = 0
    sealevel = 0
    for i in range(0,n):
        if s[i]=='D':
            sealevel-=1
        else:
            sealevel+=1
        if sealevel>0:
            continue     
        if sealevel==0 and s[i]=='U':
            count+=1
    return count
