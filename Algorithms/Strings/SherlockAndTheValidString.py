import math
import os
import random
import re
import sys
from collections import Counter

def isValid(s):
    a=Counter(s)
    l= [i for i in a.values()]
    c = l.count(a[s[0]])
    print(c)
    if c==len(set(s)) or c+1==len(set(s)):
        return 'YES'
    else:    
        return 'NO'
