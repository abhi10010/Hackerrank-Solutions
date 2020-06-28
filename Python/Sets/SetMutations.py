n = int(input())
set1 = set(map(int, input().split()))
o = int(input())

for i in range(o):
    t, v = input().split()
    set2 = set(map(int, input().split()))
    
    if t == 'intersection_update':
        set1 &= set2
    elif t == 'update':
        set1 |= set2
    elif t == 'symmetric_difference_update':
        set1 ^= set2
    elif t == 'difference_update':
        set1 -= set2

print(sum(set1))
