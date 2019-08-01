import math
import os
import random
import re
import sys

def almostSorted(arr):
    diff, diffs, diffe = 0, -1, -1
    test = arr.copy()
    test.sort()
    if arr==test:
        print('yes')
    for i in range(len(arr)):
        if arr[i]!=test[i]:
            diff+=1
            if diffs == -1:
                diffs = i
            elif diff > 1:
                diffe = i 
    if diff==2:
        temp = arr[diffs]
        arr[diffs] = arr[diffe]
        arr[diffe] = temp
        if arr==test:
            print('yes')
            print('swap', diffs+1, diffe+1)
            quit() 
    if diff>2:
        x = arr[diffs:diffe+1]
        x = x[::-1]
        y = test[diffs:diffe+1]
        if x==y:
            print('yes')
            print('reverse', diffs+1, diffe+1)
            quit()
    print('no')
