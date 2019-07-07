import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    actual = 0
    diff = 0
    for i in range(len(bill)):
        if i==k:
            continue
        else:
            actual= actual +  bill[i]
    actual = actual/2
    if actual == b:
        print("Bon Appetit")
    else:
        diff = int(b-actual)
        print(diff)
