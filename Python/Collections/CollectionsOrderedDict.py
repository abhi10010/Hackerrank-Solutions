from collections import OrderedDict

price = OrderedDict()

for i in range(int(input())):
    x = input().split()
    item, cost = ' '.join(x[:-1]), x[-1]
    
    if item not in price:
        price[item] = int(cost)
    else:
        price[item] += int(cost)

for i,j in price.items():
    print(i,j)
