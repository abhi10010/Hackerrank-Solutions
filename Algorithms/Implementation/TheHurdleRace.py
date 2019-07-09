import math
import os
import random
import re
import sys

def hurdleRace(k, height):
    maximum = max(height)
    if k-maximum<0:
        return abs(k-maximum)
    else:
        return 0
