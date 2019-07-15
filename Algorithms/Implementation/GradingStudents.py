import math
import os
import random
import re
import sys

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i]<38:
            continue
        else:
            x=math.floor(grades[i]/5)
            x=(x+1)*5
            if x-grades[i]<3:
                grades[i]=x
    return grades
