import math
import os
import random
import re
import sys

def birthday(s, d, m):
    count = 0
    t=m
    k=1
    ans=0
    for i in range(len(s)):
        ans = s[i]
        for j in range(k,t):
            ans+=s[j]
        if ans == d:
            count += 1
        k+=1
        if t < len(s):
            t+=1
        
    return count
