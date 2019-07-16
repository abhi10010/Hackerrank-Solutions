import math
import os
import random
import re
import sys

def minimumDistances(a):
    dist = list()
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i]==a[j]:
                dist.append(abs(i-j))
    if len(dist)==0:
        return -1
    else:
        return min(dist)
