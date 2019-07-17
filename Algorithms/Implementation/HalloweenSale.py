import math
import os
import random
import re
import sys

def howManyGames(p, d, m, s):
    total, count = p, 0
    while total<=s:
        if p-d>m and total<=s:
            p-=d
            count+=1
            total+=p
        if p-d<=m and total<=s:
            p=m
            total+=p
            count+=1
    return count
