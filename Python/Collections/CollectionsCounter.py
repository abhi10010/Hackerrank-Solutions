from collections import Counter

n = int(input())
s = Counter(list(map(int, input().split())))
earn = 0

for i in range(int(input())):
    sz, price = list(map(int, input().split()))
    
    if s[sz]:
        earn += price
        s[sz] -= 1

print(earn)
