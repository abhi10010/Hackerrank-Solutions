import math
import os
import random
import re
import sys

def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 < y2 or (m1 < m2 and y1 == y2) or (d1 <= d2 and m1 == m2 and y1 == y2):
        return 0
    elif d1 > d2 and m1 == m2 and y1 == y2:
        return (d1 - d2) * 15
    elif m1 > m2 and y1 == y2:
        return (m1 - m2) * 500
    else:
        return 10000
