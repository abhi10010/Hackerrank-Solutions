import math
import os
import random
import re
import sys

def viralAdvertising(n):
    shared = 5
    current_liked = 2
    total = 2
    for i in range(n-1):
        shared=current_liked*3
        current_liked=math.floor(shared/2)
        total+=current_liked
    return total
