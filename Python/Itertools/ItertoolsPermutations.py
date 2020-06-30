from itertools import permutations

s, n = input().split()

for i in sorted(list(permutations(list(s), int(n)))):
    print(''.join(i))
