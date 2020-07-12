import numpy

n, m, p = list(map(int, input().split()))

arrA = numpy.array([input().split() for _ in range(n+m)],int)

print(arrA)
