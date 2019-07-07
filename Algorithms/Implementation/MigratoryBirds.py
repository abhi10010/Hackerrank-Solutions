import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    a=arr.count(1)
    b=arr.count(2)
    c=arr.count(3)
    d=arr.count(4)
    e=arr.count(5)
    li=[a,b,c,d,e]
    ans = 1+li.index(max(li))
    return ans
