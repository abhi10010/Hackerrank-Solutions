import numpy

n = int(input())
arrA = numpy.array([input().split() for _ in range(n)], int)
arrB = numpy.array([input().split() for _ in range(n)], int)

print(numpy.matmul(arrA, arrB))
