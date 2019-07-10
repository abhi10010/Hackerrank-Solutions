import math
import os
import random
import re
import sys

def beautifulDays(i, j, k):
    n = abs(i-j)
    difference = list()
    reverse = list()
    count = 0
    days = list()
    for p in range(0,n+1):
        days.append(p+i)
    for x in range(len(days)):
        Number = days[x]
        Reverse_Number = 0    
        while(Number > 0):    
            Remainder = Number %10    
            Reverse_Number = (Reverse_Number *10) + Remainder    
            Number = Number //10
        reverse.append(Reverse_Number)
    for r in range(len(days)):
        d = abs(reverse[r]-days[r])
        difference.append(d)
    for b in range(len(difference)):
        if difference[b]%k==0:
            count+=1
    return count
