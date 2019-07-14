import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    da, db = list(), list()
    ca, cb = 0, 0
    for i in apples:
        if a+i>=s and a+i<=t:
            ca+=1
    for i in oranges:
        if b+i>=s and b+i<=t:
            cb+=1
    print(ca)
    print(cb)
