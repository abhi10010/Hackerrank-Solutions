n = int(input())
arr = list(map(int, input().split()))

print(((sum(set(arr))*n)-(sum(arr)))//(n-1))
    
