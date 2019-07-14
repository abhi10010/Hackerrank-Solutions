import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    if v1 == v2 and x1 == x2:
        return 'YES'
    elif v1 == v2:
        return 'NO' 
    x = (x2-x1) / (v1-v2)    
    if (x == round(x) and x > 0):
        return 'YES'
    else:
        return 'NO' 
