import math
import os
import random
import re
import sys

def equalizeArray(arr):
    ans=0
    x=max(arr,key=arr.count)
    for i in arr:
        if i-x!=0:
            ans+=1
    return ans
