import math
import os
import random
import re
import sys

def separateNumbers(s):
    i=1
    if len(s)==1:
        print('NO')
    else:
        while i<=math.ceil(len(s)/2):
            x=[s[:i]]
            j=i
            while j<len(s):
                flag=0
                l = len(str(int(x[-1])+1))
                x.append(str(int(x[-1])+1))
                j+=l
                chk=''
                for k in range(len(x)):
                    chk+=x[k] 
                if chk!=s[:j]:
                    flag=1
                    break
            if flag==0: 
                print('YES '+ str(x[0]))
                break
            i+=1
        if chk!=s:
            print('NO')
    
