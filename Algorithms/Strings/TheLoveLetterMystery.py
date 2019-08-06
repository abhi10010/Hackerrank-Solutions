import math
import os
import random
import re
import sys

def theLoveLetterMystery(s):
    x=s[:int(len(s)/2)]
    y=s[math.ceil(len(s)/2):]
    c1, c2 = [],[]
    ans = 0
    for i in x:
        c1.append(ord(i))
    for i in y:
        c2.append(ord(i))
    c2 = c2[::-1]
    for i in range(len(c1)):
        if c1[i]!=c2[i]:
            ans+=abs(c1[i]-c2[i])
    return ans
