import math
import os
import random
import re
import sys
.
def jumpingOnClouds(c, k):
    e=100
    for i in range(0,len(c),k):
        if c[i]==0:
            e-=1
        else:
            e-=3
        if i>=len(c) and c[0]==0:
            e-=1
            break
        if i>len(c) and c[0]==1:
            e-=3
            break
    return e
