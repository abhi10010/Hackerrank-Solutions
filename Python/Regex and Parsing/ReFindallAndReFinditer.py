import re

x = re.findall(r'(?<=[^aeiouAEIOU])[AEIOUaeiou]{2,}[^aeiouAEIOU]',input())

if len(x)==0:
    print('-1')

else:
    for i in x:
        print(i[:-1])
