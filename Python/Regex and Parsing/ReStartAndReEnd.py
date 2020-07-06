import re

s = input()
regex = input()
pattern = re.compile(regex)
r = pattern.search(s)
if not r: 
    print("(-1, -1)")
while r:
    print("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(s, r.start() + 1)
