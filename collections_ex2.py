
''' 
Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

Explanation

BANANA FRIES: Quantity bought:
, Price:
Net Price:
POTATO CHIPS: Quantity bought: , Price:
Net Price:
APPLE JUICE: Quantity bought: , Price:
Net Price:
CANDY: Quantity bought: , Price:
Net Price: 

''' 

from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
    print(item, quantity)

# Second solutions 
from collections import OrderedDict
dct = OrderedDict()
for _ in range(int(input())):
    i = input().rpartition(" ")
    dct[i[0]] = int(i[-1]) + dct[i[0]] if i[0] in dct else int(i[-1])
for l in dct:
    print(l, dct[l])

# Third Solutions 
from collections import OrderedDict
D = OrderedDict()
for _ in range(int(input())):
    item, space, price = input().rpartition(' ')
    D[item] = D.get(item, 0) + int(price)
print(*[" ".join([item, str(price)]) for item, price in D.items()], sep="\n")

