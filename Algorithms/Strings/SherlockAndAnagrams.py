import math
import os
import random
import re
import sys

def sherlockAndAnagrams(s):
    count = 0
    for k in range(1, len(s)):
        for i in range(0, len(s)-k):
            for j in range(i+1, len(s)-k+1):
                if sorted(s[i:i+k]) == sorted(s[j:j+k]):
                    count+=1
    return count
