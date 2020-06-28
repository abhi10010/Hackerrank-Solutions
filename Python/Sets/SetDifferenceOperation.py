n1 = input()
set1 = set(map(int, input().split()))
n2 = input()
set2 = set(map(int, input().split()))

print(len(set1.difference(set2)))
