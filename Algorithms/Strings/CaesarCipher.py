import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    ans = ''
    if k>26:
        k=k%26
    for i in s:
        if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
            if (ord(i)>=97 and ord(i)+k<=122) or (ord(i)>=65 and ord(i)+k<=90):
                ans+=chr(ord(i)+k)
            else:
                ans+=chr(ord(i)-(26-k))
        else:
            ans+=i
    return ans
