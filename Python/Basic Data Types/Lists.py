import math
import os
import random
import re
import sys

if __name__ == '__main__':
    
    N = int(input())
    a, Cmd = list(), list()
    
    for i in range(N):
        x = input()
        Cmd.append(x.split())
    
    for i in Cmd:
        if i[0]=='insert':
            a.insert(int(i[1]), int(i[2]))
        elif i[0]=='append':
            a.append(int(i[1]))
        elif i[0]=='remove':
            a.remove(int(i[1]))
        elif i[0]=='print':
            print(a)
        elif i[0]=='sort':
            a.sort()
        elif i[0]=='reverse':
            a.reverse()
        if i[0]=='pop':
            a.pop()


    

