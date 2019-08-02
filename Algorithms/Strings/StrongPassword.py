import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    count, flagn, flagl, flagu, flags = 0, 0, 0, 0, 0
    
    for char in password:
        if char in numbers:
            flagn = 1
            continue
        elif char in lower_case:
            flagl = 1
            continue
        elif char in upper_case:
            flagu = 1
            continue
        elif char in special_characters:
            flags = 1
            continue
    
    if (flagn+flagl+flagu+flags)<4:
        count = 4-(flagn+flagl+flagu+flags)
    
    return max(6-n, count)
