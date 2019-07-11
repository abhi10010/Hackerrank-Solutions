import math
import os
import random
import re
import sys

def saveThePrisoner(n, m, s):
    last = (s-1+m)%n
    if last == 0:
        last = n
    return last
