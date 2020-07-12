import numpy
import math

n = int(input())

arr = numpy.array([input().split() for _ in range(n)], float)

print(round(numpy.linalg.det(arr), 2))
