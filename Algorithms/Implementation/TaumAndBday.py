import math
import os
import random
import re
import sys

def taumBday(b, w, bc, wc, z):
    cost=0
    if bc>wc+z:
        cost=(b+w)*wc + b*z
    elif wc>bc+z:
        cost = (b+w)*bc + w*z
    else:
        cost = b*bc + w*wc
    return cost
