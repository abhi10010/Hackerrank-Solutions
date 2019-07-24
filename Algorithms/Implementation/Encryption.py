import math
import os
import random
import re
import sys

def encryption(s):
    x = math.ceil(math.sqrt(len(s)))
    itr, ans = 0, ''
    for i in range(x):
        for i in range(itr,len(s),x):
            ans+=s[i]
        itr+=1
        ans+=' '
    return ans
