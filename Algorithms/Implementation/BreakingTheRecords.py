import math
import os
import random
import re
import sys

def breakingRecords(scores):
    least, maxi, cl, cm = scores[0], scores[0], 0 ,0 
    for i in scores:
        if least > i:
            least=i
            cl+=1
        if maxi < i:
            maxi=i
            cm+=1
    return(cm, cl)
