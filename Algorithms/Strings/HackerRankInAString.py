import math
import os
import random
import re
import sys

def hackerrankInString(s):
    x=list('hackerrank')
    j=0
    y=-1
    while len(x)>0:
        flag=1
        for i in range(len(s)):
            if x[j]==s[i]:
                if i > y:
                    y=i
                    del(x[j])
                    flag=0
                    break
            else:
                continue
        if flag==1:
            return 'NO'
    return 'YES'
