cube = lambda x: pow(x,3)# complete the lambda function 

def fibonacci(n):
    
    res = [0, 1, 1]
    
    if n==0:
        return []
    elif n == 1:
        return res[0:1]
    elif n == 2:
        return res[0:2]
    elif n == 3:
        return res[0:]
    else:
        for i in range(3, n):
            res.append(res[i-1] + res[i-2])
        return res

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
