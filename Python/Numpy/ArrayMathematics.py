import numpy

n, m = map(int, input().split())

arrA = numpy.array([input().split() for _ in range(n)],int)
arrB = numpy.array([input().split() for _ in range(n)],int)

print(arrA + arrB)
print(arrA - arrB)
print(arrA * arrB)
print(arrA // arrB)
print(arrA % arrB)
print(arrA ** arrB)
