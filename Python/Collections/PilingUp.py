from collections import deque


for i in range(int(input())):
    n = int(input())
    d = deque(map(int, input().split()))
    mx = max(d[0], d[-1])
    
    for i in range(n):
        
        if mx < d[0] or mx < d[-1]:
            print('No')
            break
        elif len(d) <= 2:
            print('Yes')
            break
        else:
            mx = max(d[0], d[-1])
            d.pop()
            d.popleft()
            
