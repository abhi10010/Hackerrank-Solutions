import math
import os
import random
import re
import sys

def squares(a, b):
    n = math.floor(math.sqrt(a-1))
    m = math.floor(math.sqrt(b))
    return m-n
