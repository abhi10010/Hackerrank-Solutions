import math
import os
import random
import re
import sys

def bomberMan(n, grid):
    grids = []
    if n==1:
        return grid
    if n%2==0:
        grid = ['O'*len(grid[0])]*len(grid)
        return grid
    for k in range(2):
        bombpos = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='O':
                    bombpos.append([i,j])       
        grid = ['O'*len(grid[0])]*len(grid)
        for i,j in bombpos:
            grid[i]=grid[i][:j]+'.'+grid[i][j+1:]
            if i-1>=0:    
                grid[i-1]=grid[i-1][:j]+'.'+grid[i-1][j+1:]
            if i+1<len(grid):    
                grid[i+1]=grid[i+1][:j]+'.'+grid[i+1][j+1:]
            if j-1>=0:    
                grid[i]=grid[i][:j-1]+'.'+grid[i][j:]
            if j+1<len(grid[0]):   
                grid[i]=grid[i][:j+1]+'.'+grid[i][j+2:]
        grids.append(grid)
    if n%4==1:
        return grids[1]  
    else:
        return grids[0]          
