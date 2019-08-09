import math
import os
import random
import re
import sys

def palindromeIndex(s):
    if s==s[::-1]:
        return -1
    else:
        for i in range(int(len(s)/2)):
            if s[i]!=s[len(s)-1-i]:
                if (s[:i]+s[i+1:])==(s[:i]+s[i+1:])[::-1]:
                    return i
                    break
                else:
                    return len(s)-1-i
                    break
