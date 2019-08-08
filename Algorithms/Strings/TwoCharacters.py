import math
import os
import random
import re
import sys

def alternate(s):
    x = list(set(s))
    l = []
    print(x)
    act = []
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            act.append([x[i],x[j]])
    flag=0
    for i,j in act:
        t=[]
        for k in range(len(s)):
            if i==s[k] or j==s[k]:
                t.append(s[k])
        flag=0
        for k in range(len(t)-1):
            if t[k]==t[k+1]:
                flag=1
                break
        if flag==0:
            l.append(len(t))
    if len(l)==0:
        return 0
    return max(l)
