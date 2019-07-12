import math
import os
import random
import re
import sys

def permutationEquation(p):
    s = list()
    n = list()
    ans = list()
    for i in range(len(p)):
        s.append(i+1)
    for j in range(len(p)):
        for k in range(len(p)):
            if s[j]==p[k]:
                n.append(k+1)
    for l in range(len(p)):
        for m in range(len(p)):
            if n[l]==p[m]:
                ans.append(m+1)
    return ans
