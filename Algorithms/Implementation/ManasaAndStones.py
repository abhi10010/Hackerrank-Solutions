import math
import os
import random
import re
import sys

def stones(n, a, b):
    z = []
    for i in range(n):
        z.append(a*i+b*(n-i-1))
    return sorted(set(z))
