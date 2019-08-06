import math
import os
import random
import re
import sys

def gameOfThrones(s):
    x = set(s)
    l = []
    for i in x:
        l.append(s.count(i)%2)
    if l.count(1)>1:
        return 'NO'
    return 'YES'
