import math
import os
import random
import re
import sys

def timeInWords(h, m):
    s=["zero", "one", "two", "three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","twenty one","twenty two","twenty three","twenty four","twenty five","twenty six","twenty seven","twenty eight","twenty nine"]
    if m==0:
        return s[h] + ' o\' clock'
    elif m==1:
        return s[m] + ' minute past ' + s[h]
    elif m==15:
        return 'quarter past ' + s[h]
    elif m>1 and m<30 and m!=15:
        return s[m] + ' minutes past ' + s[h]
    elif m==30:
        return 'half past ' + s[h]
    elif m==45:
        return 'quarter to ' + s[h+1]
    elif m==59:
        return 'one minute to ' + s[h+1]
    else:
        m=60-m
        return s[m] + ' minutes to ' + s[h+1]
