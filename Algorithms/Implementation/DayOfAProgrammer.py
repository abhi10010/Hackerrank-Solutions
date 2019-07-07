import math
import os
import random
import re
import sys

def dayOfProgrammer(year):
    leap_list=[31,29,31,30,31,30,31,31]
    n=0
    usual_list=[31,28,31,30,31,30,31,31]
    trans_list=[31,15,31,30,31,30,31,31]
    if year<1918:
        if year%4==0:
            n = sum(leap_list)
            n = 256-n
            date = str(n)+(".09.")+str(year)
        else:
            n = sum(usual_list)
            n = 256-n
            date = str(n)+(".09.")+str(year)
    elif year==1918:
        n = sum(trans_list)
        n = 256-n
        date = str(n)+(".09.")+str(year)
    else:
        if year%400==0 or year%4==0 and year%100!=0:
            n = sum(leap_list)
            n = 256-n
            date = str(n)+(".09.")+str(year)
        else:
            n = sum(usual_list)
            n = 256-n
            date = str(n)+(".09.")+str(year)
    return date
