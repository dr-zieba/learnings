import itertools
from collections import defaultdict

makes = defaultdict(int)

# with open('17+-+Grouping/cars_2014.csv') as f:
#     next(f)
#     print(f)
#     makes_group = itertools.groupby(f, key=lambda x: x.split(',')[0])
#     print(list(makes_group))
#     makes_count = ((make, sum(1 for count in group)) for make, group in makes_group)
#     #print(list(makes_count))

import matplotlib.pyplot as plt

amount = defaultdict(int)
with open('17+-+Grouping/cars_2014.csv') as f:
    for l in f:
        l = l.split(',')
        amount[l[0]] += 1

plt.bar(list(amount.keys()), amount.values(), color='g')
plt.xticks(rotation=90, ha='right')

plt.show()
