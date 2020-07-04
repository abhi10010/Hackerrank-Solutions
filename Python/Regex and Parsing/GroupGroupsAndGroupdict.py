import re

pattern = re.compile(r"([A-Za-z0-9])\1+")
matches = pattern.search(input())

if matches is None:
    print(-1)

else:
    print(matches.group(1))
