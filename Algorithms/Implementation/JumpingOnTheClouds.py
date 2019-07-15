import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    jump, i = 0, 0
    while i<len(c):
        if i+2<len(c) and (c[i+2]==0 or c[i+1]==1):
            jump+=1
            i+=2
        else:
            jump+=1
            i+=1
    return jump-1
