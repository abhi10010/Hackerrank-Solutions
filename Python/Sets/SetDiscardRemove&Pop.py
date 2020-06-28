n = int(input())
s = set(map(int, input().split()))
o = int(input())

for i in range(o):
    t = input().split()
    
    if t[0] == 'pop':
        s.pop()
    elif t[0] == 'remove':
        s.remove(int(t[1]))
    elif t[0] == 'discard':
        s.discard(int(t[1]))

print(sum(s))
