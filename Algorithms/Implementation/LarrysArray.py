import math
import os
import random
import re
import sys
from collections import deque

def larrysArray(A):
    count = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                    count+=1
    if count%2==0:
        return "YES"
    else:
        return "NO"
