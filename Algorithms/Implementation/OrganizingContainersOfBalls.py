import math
import os
import random
import re
import sys

def organizingContainers(container):
    countType=[0]* len(container[0])
    print(countType)
    countContainer=[sum(x) for x in container]
    print(countContainer)
    for i in container:
        for j in range(len(i)):
            print(j)
            countType[j]+=i[j]
    countContainer.sort()
    countType.sort()
    print('Count By Types:',countType)
    print('Count By Container:',countContainer)
    if countContainer==countType:
        return 'Possible'  
    else:
        return 'Impossible'
