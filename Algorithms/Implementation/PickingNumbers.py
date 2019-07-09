import math
import os
import random
import re
import sys

def pickingNumbers(a):
    a.sort()
    print(a)
    new2 = list()
    for i in range(len(a)):
        new1 = list()
        for j in range(i+1,len(a)):
            if abs(a[j]-a[i])>1:
                break
            if a[i]-a[j]==0 or abs(a[i]-a[j])==1:
                new1.append(a[i])
        if len(new1)>len(new2):
            new2=new1
        else:
            continue
    return len(new2)+1
