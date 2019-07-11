import math
import os
import random
import re
import sys

def circularArrayRotation(a, k, queries):
    from collections import deque 
    items = deque(a) 
    items.rotate(k)
    ret_list = []
    for q in queries:
        ret_list.append(items[q])
    return ret_list
