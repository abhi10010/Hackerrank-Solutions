n1 = input()
set1 = set(map(int, input().split()))
n2 = input()
set2 = set(map(int, input().split()))

for i in sorted(set1.symmetric_difference(set2)):
    print(i)
