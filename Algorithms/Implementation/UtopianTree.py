import math
import os
import random
import re
import sys

def utopianTree(n):
    height = 1
    if n==0:
        return 1
    for i in range(1,n+1):
        print(i)
        if i%2==0:
            height+=1
        else:
            height*=2
    return height
