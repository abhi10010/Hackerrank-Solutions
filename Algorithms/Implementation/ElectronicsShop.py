import os
import sys

def getMoneySpent(keyboards, drives, b):
    cost = list()
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            cost.append(keyboards[i]+drives[j])
    for i in range(len(cost)):
        if cost[i]>b:
            cost[i]=0
    if max(cost)==0:
        return -1
    else:
        return max(cost)
