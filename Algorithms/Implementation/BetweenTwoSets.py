import math
import os
import random
import re
import sys

def getTotalX(a, b):
    bel = min(b)
    new = list()
    lcm = a[0]
    ans =  0
    for i in a[1:]:
        lcm = int(lcm*i/math.gcd(lcm, i))
    for i in range(lcm, bel+1, lcm):
        new.append(i)
    for i in new:
        flag=0
        for x in b:
            if x%i!=0:
                flag=1
        if flag==0:
            ans+=1
    return ans
