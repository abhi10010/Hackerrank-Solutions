import numpy

n, m = map(int, input().split())

print(numpy.prod(numpy.sum(numpy.array([input().split() for _ in range(n)], int), axis = 0)))
