from numbers import Number

l = [i for i in range(10)]

fn = lambda x: x + 10

r = map(fn, l)
print(list(r))

q = [fn(i) for i in l]
print(q)

if all(map(lambda x: isinstance(x, Number), l)):
    print("all num")