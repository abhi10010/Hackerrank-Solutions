from collections import Counter, OrderedDict

if __name__ == '__main__':
    
    class OrderedCounter(Counter, OrderedDict):
        pass
    
    for i in Counter(sorted(input())).most_common(3):
        print(*i)
