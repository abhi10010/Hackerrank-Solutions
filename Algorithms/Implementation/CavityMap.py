import math
import os
import random
import re
import sys

def cavityMap(grid):
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid)-1):
            if grid[i][j]>grid[i-1][j] and grid[i][j]>grid[i+1][j] and grid[i][j]>grid[i][j+1] and grid[i][j]>grid[i][j-1]:
                grid[i]=grid[i][:j]+'X'+grid[i][j+1:]
            else:
                continue
    return grid
