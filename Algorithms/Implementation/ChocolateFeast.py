import math
import os
import random
import re
import sys

def chocolateFeast(n, c, m):
    wrappers = int(n/c)
    chocolates = int(n/c)
    more = 0
    while wrappers>=m:
        more=int(wrappers/m)
        chocolates+=more
        wrappers=wrappers%m+more
    return chocolates
