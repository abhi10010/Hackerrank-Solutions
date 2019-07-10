import math
import os
import random
import re
import sys

def angryProfessor(k, a):
    count=0
    for i in range(len(a)):
        if a[i]<=0:
            count+=1
    if count>=k:
        return 'NO'
    else:
        return 'YES'
