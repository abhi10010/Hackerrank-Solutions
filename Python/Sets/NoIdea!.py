happiness = 0

n, m = list(map(int, input().split()))
set_ = list(map(int, input().split()))
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

for i in set_:

    if i in setA:
        happiness += 1
    elif i in setB:
        happiness -= 1

print(happiness)
