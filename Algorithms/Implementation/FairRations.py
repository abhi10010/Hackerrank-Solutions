import math
import os
import random
import re
import sys

def fairRations(B):
    no_o=0
    tot=0
    index=[]
    flag=1
    for i in range(len(B)) :
        if B[i]%2!=0:
            no_o+=1
            index.append(i)
            flag=0
    if no_o%2!=0:
        return 'NO'
    else:
        if flag==0:
            i=0
            while i < len(index)-1:
                dist = abs(index[i]- index[i+1])
                i+=2
                tot+= 2*dist
            return tot
        else: 
            return 0
