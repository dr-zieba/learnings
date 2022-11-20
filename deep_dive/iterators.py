from itertools import cycle, islice
from collections import namedtuple

l = range(10)
print(list(l))

c = cycle(range(3))
print(list(islice(c, 10)))

print(list(zip(cycle(range(3)), range(10))))

print("#####################")

Card = namedtuple('Card', 'rank suit')

def card_deck():
    ranks = tuple(str(num) for num in range(2,11)) + tuple('JQKA')
    suits = ('spades', 'hearts', 'diamonds', 'clubs')

    for suit in suits:
        for rank in ranks:
            yield Card(rank, suit)

hand = [list() for  _ in range(4)]

index = 0
for card in card_deck():
    index = index % 4
    hand[index].append(card)
    index += 1
print(hand)

hand2 = [list() for _ in range(4)]
index2 = cycle(range(4))
for card in card_deck():
    hand2[next(index2)].append(card)
print(hand2)

hand3 = [list() for _ in range(4)]
hand_cycle = cycle(hand3)
for card in card_deck():
    next(hand_cycle).append(card)
print(hand3)