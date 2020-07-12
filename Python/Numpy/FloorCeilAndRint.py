import numpy

numpy.set_printoptions(sign=' ')

x = numpy.array(input().split(), float)

print(numpy.floor(x))
print(numpy.ceil(x))
print(numpy.rint(x))
