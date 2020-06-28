n1 = input()
arr1 = set(map(int, input().split()))
n2 = input()
arr2 = set(map(int, input().split()))

print(len(arr1.union(arr2)))
