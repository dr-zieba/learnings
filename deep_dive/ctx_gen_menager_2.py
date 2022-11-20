

def gen(fname, mode='r'):
    print("Opening file...")
    f = open(fname, mode)
    try:
        yield f
    finally:
        print("Closing file...")
        f.close()

class GenContextMgr:
    def __init__(self, _gen):
        self.gen = _gen

    def __enter__(self):
        return next(self.gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            next(self.gen)
        except StopIteration:
            pass
        return False

def context_decorator(f_gen):
    def inner(*args, **kwargs):
        gener = f_gen(*args, **kwargs)
        ctx = GenContextMgr(gener)
        return ctx
    return inner

@context_decorator
def gen_with_decor(fname, mode='r'):
    print("Opening file...")
    f = open(fname, mode)
    try:
        yield f
    finally:
        print("Closing file...")
        f.close()

# f_gen = gen('Project+3+-+Description/nyc_parking_tickets_extract.csv')
#
# with GenContextMgr(f_gen) as f:
#     print(type(f))
#     for l in f:
#         print(l)

with gen_with_decor('Project+3+-+Description/nyc_parking_tickets_extract.csv') as f:
    print(f)
    print(f.readlines())

from contextlib import contextmanager

@contextmanager
def open_f(fname):
    f = open(fname)
    try:
        yield f
    finally:
        f.close()

print("*-*--*---*--*-*--*")
with open_f('Project+3+-+Description/nyc_parking_tickets_extract.csv') as f:
    print(f.readlines())

enter = []
exit = []
fname = 'Project+3+-+Description/nyc_parking_tickets_extract.csv'
ctx = open_f(fname)
enter.append(ctx.__enter__)
exit.append(ctx.__exit__)
print(enter)
print(exit)


