import math
import os
import random
import re
import sys

def strangeCounter(t):
    x = math.ceil(t/3)
    n = math.floor(math.log(x,10)/math.log(2,10))+1
    s = 4
    print(n)
    for i in range(1,n):
        s+=3*(2**i)
    return(s-t)
