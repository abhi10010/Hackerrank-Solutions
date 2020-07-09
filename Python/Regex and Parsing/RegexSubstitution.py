import re

for _ in range(int(input())):
    x = input()
    x = re.sub(r' \&\&(?= )', ' and', x)
    x = re.sub(r' \|\|(?= )', ' or', x)
    print(x)
