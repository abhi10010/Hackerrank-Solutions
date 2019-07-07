import math
import os
import random
import re
import sys

def divisibleSumPairs(n, k, ar):
    q=1
    ans=0
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
            if (ar[i]+ar[j])%k == 0:
                ans+=1
    return ans
