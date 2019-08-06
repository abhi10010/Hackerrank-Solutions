import math
import os
import random
import re
import sys

def makingAnagrams(s1, s2):
    d1 = {x:s1.count(x) for x in s1}
    d2 = {x:s2.count(x) for x in s2}
    count=0
    for k in d1.keys():
        if k in d2.keys():
            count+=(2*min(d2[k],d1[k]))
    return(abs(len(s1)+len(s2)-count))
