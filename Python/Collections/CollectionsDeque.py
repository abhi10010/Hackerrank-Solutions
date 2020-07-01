from collections import deque

d = deque()

for i in range(int(input())):
    x = input().split()
    o, n = x[0], x[-1]
    
    if o == 'append':
        d.extend(n)
    elif o == 'appendleft':
        d.appendleft(n)
    elif o == 'pop':
        d.pop()
    elif o == 'popleft':
        d.popleft()

for i in d:
    print(int(i), end=' ')
