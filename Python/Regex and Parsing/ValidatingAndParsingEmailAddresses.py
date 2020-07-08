import email.utils
import re

for i in range(int(input())):
    x, y = input().split()
    
    if re.match(r'^[A-Za-z]+[A-Za-z0-9-_.]*@{1}[A-Za-z]+\.{1}[A-Za-z]{1,3}$', y[1:-1]):    
        print(email.utils.formataddr((x, y[1:-1])))
