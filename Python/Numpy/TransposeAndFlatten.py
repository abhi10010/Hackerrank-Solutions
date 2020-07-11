import numpy

n, m = list(map(int, input().split()))
x = []

for _ in range(n):
    x.append(list(map(int, input().split())))

print(numpy.transpose(numpy.array(x, int)))
print(numpy.array(x, int).flatten())
