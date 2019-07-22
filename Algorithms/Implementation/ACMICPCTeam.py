import math
import os
import random
import re
import sys

def acmTeam(topic, n, m):
    x, ans_count = list(), list()
    k=0
    for i in topic:
        x.append(list(i))
    for i in range(n):
        for j in range(i+1,n):
            tcount=0
            for itr in range(m): 
                if x[i][itr] == '1' or x[j][itr] == '1':
                    tcount+=1
            ans_count.append(tcount)
    ans1 = max(ans_count)
    ans2 = ans_count.count(ans1)
    return(ans1, ans2)
