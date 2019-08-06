import math
import os
import random
import re
import sys

def alternatingCharacters(s):
    count=0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count+=1
    return count
