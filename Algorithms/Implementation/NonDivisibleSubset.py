import math
import os
import random
import re
import sys
from collections import Counter

def nonDivisibleSubset(k, S):
    a, x, count = [], [], [0]*(k)
    for i in S:
        a.append(i%k)
    print(a)
    for i in a:
        count[i]+=1
    print(count)
    ans = min(count[0], 1)
    for i in range(1, (k//2)+1):
        if i!=k-i:
            ans+=max(count[i], count[k-i])
    if k%2==0:
        ans+=1
    return ans
