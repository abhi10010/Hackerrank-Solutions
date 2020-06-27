import math
import os
import random
import re
import sys

if __name__ == '__main__':
    
    grades, marks= list(), list()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marks+=[[name, score]]
        grades+=[score]
    
    x = sorted(set(grades))[1]
    
    for k,v in sorted(marks):
        if v==x:
            print(k)
