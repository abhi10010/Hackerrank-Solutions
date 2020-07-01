from collections import OrderedDict, Counter

class OrderedCounter(Counter, OrderedDict):
    pass

d = OrderedCounter(input() for _ in range(int(input())))

print(len(d))
print(*d.values())
