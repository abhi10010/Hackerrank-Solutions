from itertools import combinations

n = input()
s = input()
s = s.replace(' ', '')
count, l = 0, 0
c = combinations(s, int(input()))

for i in c:
    if 'a' in i:
        count += 1
    l += 1

print(count/l)
