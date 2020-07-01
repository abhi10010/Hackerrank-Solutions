from collections import namedtuple

n = int(input())
x = input().split()
sum_ = 0

for i in range(n):
    student = namedtuple('student' , x)
    a, b, c, d = input().split()
    student = student(a, b, c, d)
    sum_ += int(student.MARKS)

print('{:.2f}'.format(sum_ / n))
