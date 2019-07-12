import math
import os
import random
import re
import sys

def findDigits(n):
    s=str(n)
    count=0
    for i in range(len(s)):
        if int(s[i])==0:
            continue
        if n%int(s[i])==0:
            count+=1
    return count
