import math
import os
import random
import re
import sys

def gridSearch(G, P):
    x,y,flag=0,0,0
    R,C,r,c = len(G),len(G[0]),len(P),len(P[0])
    for i in range(0,R-r+1):
        for j in range(0,C-c+1):
            if G[i][j]==P[0][0]:
                for row in G[i:i+r]:
                    if P[x]==row[j:j+c]:
                        x+=1
                        if r==x:
                            flag=1
                            break
                    else:
                        flag=0
                        x=0
                        break
            if flag==1:
                return 'YES'
    if flag==0:
        return 'NO'
