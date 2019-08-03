import math
import os
import random
import re
import sys

def pangrams(s):
    s = s.lower()
    l = list(set(s))
    space = ' '
    if space in l:
        l.remove(' ')
    if len(l)==26:
        return('pangram')
    else:
        return('not pangram')
