import math
import os
import random
import re
import sys

def repeatedString(s, n):
    if s=='a':
        return n
    slicer = n%len(s)
    count = s.count('a')
    strings = int(n/len(s))
    additional = s[:slicer].count('a')
    total = count*strings + additional 
    return total
