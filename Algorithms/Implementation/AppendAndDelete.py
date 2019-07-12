import math
import os
import random
import re
import sys

def appendAndDelete(s, t, k):
    similar=0
    for i in range(min(len(s),len(t))):
        if i<min(len(t),len(s)) and s[i]==t[i]:
            similar+=1
        else:
            break
    if (len(s)+len(t)-2*similar)>k:
        return('No')
    elif (len(s)+len(t)-2*similar)%2==k%2:
        return('Yes')
    elif (len(s)+len(t)-k)<0:
        return('Yes')
    else:
        return('No')
