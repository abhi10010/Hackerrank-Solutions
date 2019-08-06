import math
import os
import random
import re
import sys

def anagram(s):
    if len(s)%2!=0:
        return -1
    else:
        count = 0
        x = int(len(s)/2)
        s1 = s[:x]
        s2 = s[x:]
        for i in s1:
            if i in s2:
                count+=1
                s2 = s2.replace(i,'',1)
        return len(s1)-count
