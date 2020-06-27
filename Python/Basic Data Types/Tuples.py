if __name__ == '__main__':
    
    n = int(input())
    integer_list = map(int, input().split())
    a  = list(integer_list)
    t = tuple(a)
    print(hash(t))

