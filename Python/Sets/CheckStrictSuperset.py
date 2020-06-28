setA = set(map(int, input().split()))
n = int(input())

flag = 0

for i in range(n):
    set_ = set(map(int, input().split()))
    
    if set_.issubset(setA) == False:
        flag -= 1
    elif set_.issubset(setA) == True and len(setA) > len(set_):
        flag += 1
    else:
        flag -= 1

if flag <= 0:
    print(False)
else:
    print(True)
