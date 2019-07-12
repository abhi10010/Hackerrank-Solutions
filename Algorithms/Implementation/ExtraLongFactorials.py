import math
import os
import random
import re
import sys

def extraLongFactorials(n):
    ans=1
    for i in range(1,n+1):
        ans*=i
    print(ans)
