import math

nm = input().split()
n = int(nm[0])
m = int(nm[1])
x, y = '.|.', '.|.'

for i in range(1,math.floor(n/2)+1):
    print(y.center(m,'-'))
    y =  y + x*2

print("WELCOME".center(m,'-'))
z = y.replace('.', '', 4)
w = z.replace('|', '', 2)

for i in range(math.floor(n/2)+1,1,-1):
    print(w.center(m,'-'))
    w = w.replace('.', '', 4)
    w = w.replace('|','',2)
