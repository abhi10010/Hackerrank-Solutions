import os
import sys

def timeConversion(s):
    if s[8:] == "AM" and s[0:2] == "12":
        return "00"+s[2:8]
    elif s[8:] == "AM":
        return s[0:8]
    elif s[8:] == "PM" and s[0:2]== "12":
        return s[:8]
    else:
        return str(int(s[0:2])+12)+s[2:8]
