import math
import os
import random
import re
import sys

def weightedUniformStrings(s, queries):
    d = set()
    p, l = -1, 0
    ans = []
    for x in s:
        d.add(ord(x)-96)
        if x==p:
            l+=1
            d.add((ord(x)-96)*l)
        else:
            p = x
            l = 1
    for i in queries:
        if i in d:
            ans.append('Yes')
        else:
            ans.append('No')
    return ans
