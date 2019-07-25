import math
import os
import random
import re
import sys

def surfaceArea(A):
    ans = 2*(len(A)*len(A[0]))
    x, y = len(A), len(A[0])
    ar = [[0] * (len(A[0]) + 2)]
    for row in A:
        ar.append([0] + row + [0])
    ar.append([0] * (len(A[0]) + 2))
    print(ar)
    for i in range(1,x+1):
        for j in range(1, y+1):
            ans+=max(0, ar[i][j]-ar[i-1][j])
            ans+=max(0, ar[i][j]-ar[i][j-1])
            ans+=max(0, ar[i][j]-ar[i+1][j])
            ans+=max(0, ar[i][j]-ar[i][j+1])
    return ans
