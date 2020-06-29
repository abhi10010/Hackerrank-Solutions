import math

ab = int(input())
bc = int(input())

print(str(int(round(math.degrees(math.atan2(ab,bc)))))+'°')
