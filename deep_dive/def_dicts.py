from collections import defaultdict, Counter

d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}

def merge(*d):
    unsorted = {}
    for elem in d:
        for key, value in elem.items():
            unsorted[key] = unsorted.get(key, 0) + value
    return dict(sorted(unsorted.items(), key=lambda el: el[1], reverse=True))

def merge_def(*d):
    unsorted = defaultdict(int)
    for elem in d:
        for key, value in elem.items():
            unsorted[key] += value
    return dict(sorted(unsorted.items(), key=lambda el: el[1], reverse=True))

def merge_counter(*d):
    unsorted = Counter()
    for elem in d:
        for key, value in elem.items():
            unsorted[key] += value
    return unsorted

a = merge_counter(d1, d2, d3)
print(a)



