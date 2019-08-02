import math
import os
import random
import re
import sys

def camelcase(s):
    count=0
    for i in s:
        if ord(i)>=65 and ord(i)<=91:
            count+=1 
    return count+1
