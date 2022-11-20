from itertools import chain

composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}

def dict_sort(dict):
    return {k: v for k,v in sorted(dict.items(), key=lambda dict: dict[1])}

print(dict_sort(composers))

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 20, 'c': 30, 'y': 40, 'z': 50}

def cat_dict(x, z):
    d1_k = x.keys()
    d2_k = z.keys()
    keys = d1_k & d2_k
    return {k: (x[k], z[k]) for k in keys}

#print(cat_dict(d1, d2))

da1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
da2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
da3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}

def xxx(*dicts):
    unsorted = {}
    for d in dicts:
        for k,v in d.items():
            unsorted[k] = unsorted.get(k, 0) + v
    _sorted = dict(sorted(unsorted.items(), key=lambda unsorted: unsorted[v], reverse=True))
    return _sorted

print(xxx(da1, da2, da3))

def count_dict(a,b,c):
    d1, d2, d3 = a.keys(), b.keys(), c.keys()
    keys = d1 | d2 | d3

    combined = {k: (a.get(k, 0), b.get(k, 0), c.get(k, 0)) for k in keys}
    final_dict = {k: sum(v) for k,v in combined.items()}
    sorted_dict = {k: v for k, v in sorted(final_dict.items(), key=lambda final_dict: final_dict[1], reverse=True)}
    return sorted_dict

#print(count_dict(da1, da2, da3))

n1 = {'employees': 100, 'employee': 5000, 'users': 10, 'user': 100}
n2 = {'employees': 250, 'users': 23, 'user': 230}
n3 = {'employees': 150, 'users': 4, 'login': 1000}

def ex4(*dicts):
    unsorted_dict = {}
    for d in dicts:
        for k,v in d.items():
            unsorted_dict[k] = (v,)
    print(unsorted_dict)

ex4(n1, n2, n3)