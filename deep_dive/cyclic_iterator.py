
'''
concatenates two list like:
1,2,3,4,5,6,7 ...
N,S,E,W

to:
1N, 2S, 3E, 4W, 5N, 6S, 7E ...
'''

class CyclicIter():
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.lst[self.i % len(self.lst)]
        self.i += 1
        return result

iterCycle = CyclicIter('NSWE')
numbers = range(1,11)

# CyclicIter is infinit iterator, it cant be exausted. Index % len(lst) cant exausted interaor.
# Zip will be exausted by numbers list.
# To restar iterator of iterCycle, call CyclicIter again
#if not in followed list 'NSWE' will be used continously.

final_list = zip(numbers, iterCycle)
print(list(final_list))
#Result: [(1, 'N'), (2, 'S'), (3, 'W'), (4, 'E'), (5, 'N'), (6, 'S'), (7, 'W'), (8, 'E'), (9, 'N'), (10, 'S')]

for i in  range(1,11):
    direction = next(iterCycle)
    print(f'{direction}{i}')

#Result:
#W1
#E2
#N3
#S4
#W5
#E6
#N7
#S8
#W9
#E10

list_ = [f'{next(iterCycle)}{i}' for i in range(1,11)]
print(list_)
#Result: ['N1', 'S2', 'W3', 'E4', 'N5', 'S6', 'W7', 'E8', 'N9', 'S10']

