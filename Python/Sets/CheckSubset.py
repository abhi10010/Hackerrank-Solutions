n = int(input())

for i in range(n):
    x = input()
    setA = set(map(int, input().split()))
    y = input()
    setB = set(map(int, input().split()))

    print(setA.issubset(setB))
