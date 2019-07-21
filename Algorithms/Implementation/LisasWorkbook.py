import math
import os
import random
import re
import sys

def workbook(n, k, arr):
    count = 0
    page_no = 1
    for i in arr:
        pages = math.ceil(i/k)
        for x in range(pages):
            if page_no>= (x * k)+1 and page_no<= min((x+1)*k, i):
                count+=1
            page_no+=1
    return(count)   
