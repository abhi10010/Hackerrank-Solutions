import math
import os
import random
import re
import sys

def happyLadybugs(b):
    keys = dict.fromkeys(b)
    for i in keys.keys():
        c = b.count(i)
        keys.update({i:c})
    flag=0
    if len(b)==1:
        return 'NO'
    if len(b)==2 and b[0]!=b[1]:
        return 'NO'

    if '_' in keys.keys():
        cdash = keys['_']
        del keys['_']
    else:
        for i in range(1,len(b)-1):
            if (b[i]==b[i+1] or b[i]==b[i-1]) and (b[0]==b[1] and b[-1]==b[-2]):
                continue
            else:
                flag=1
                break
        if flag==1:
            return 'NO'
        elif flag==0:
            return 'YES'
    print(keys)
    flag1=0
    for i in keys.keys():
        if keys[i]!=1 and cdash>=1:
            continue
        else:
            flag1=1
            break
    if flag1==1:
        return 'NO'
    else:
        return 'YES'
