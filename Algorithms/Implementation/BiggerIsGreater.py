import math
import os
import random
import re
import sys

def biggerIsGreater(w):
    l, ans=[], ''
    for i in range(len(w)):
        l.append(ord(w[i]))
    i = len(l) - 1
    while i>0 and l[i-1] >= l[i]:
        i -= 1
    if i <= 0:
        return 'no answer'
    j = len(l)-1
    while l[j]<=l[i-1]:
        j-=1
    l[i-1],l[j]=l[j],l[i-1]
    l[i:] = l[len(l)-1:i-1:-1]
    for i in range(len(l)):
        ans+=chr(l[i])
    return ans
