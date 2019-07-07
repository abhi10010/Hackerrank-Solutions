import math
import os
import random
import re
import sys

def birthdayCakeCandles(ar):
    count = 0
    largest = None
    for i in range(len(ar)):
        if largest == None:
            largest = ar[i]
        if largest < ar[i]:
            largest = ar[i]
    for i in range(len(ar)):
        if ar[i] == largest:
            count += 1
    return count
