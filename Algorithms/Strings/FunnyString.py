import math
import os
import random
import re
import sys

def funnyString(s):
    l = []
    for i in range(len(s)-1):
        l.append(abs(ord(s[i])-ord(s[i+1])))
    if l==l[::-1]:
        return 'Funny'
    else:
        return 'Not Funny'
