import math
import os
import random
import re
import sys

def kaprekarNumbers(p, q):
    flag=0
    for i in range(p,q+1):
        n2 = i**2
        s2 = str(n2)
        if len(s2)%2==0:
            a=len(s2)/2
            l=int(n2/(10**a))
            r=n2%(10**a)
        else:
            a=int(len(s2)/2)
            b=len(s2)-a
            l=int(n2/(10**b))
            r=n2%(10**b)
        if l+r==i:
            flag=1
            print(i, end=' ')
    if flag==0:
        print("INVALID RANGE")
