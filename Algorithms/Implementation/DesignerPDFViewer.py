import math
import os
import random
import re
import sys

def designerPdfViewer(h, word):
    height=list()
    char=list(word)
    for i in range(len(char)):
        char[i]=ord(char[i])
        char[i]-=97
    for i in char:
        height.append(h[i])
    max_height = max(height)
    area = len(char)*max_height
    return area
