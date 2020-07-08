import re

for i in range(int(input())):
    x = re.findall(r'(?<!^)(#(?:[\dA-Fa-f]{3}){1,2})', input())
    
    if len(x)>0:
        for i in x:
            print(i)
