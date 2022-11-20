

def my_gen():
    try:
        print('creting ...')
        yield [1,2,3]
    finally:
        print('exiting gen ...')

#Generator approach
# f = my_gen()
# l = next(f)
# print(l)
# try:
#     next(f)
# except StopIteration as e:
#     print(e)

#Cotext manager approach
class MyCtx:
    def __init__(self, genn):
        self.gen = genn()

    def __enter__(self):
        return next(self.gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            return next(self.gen)
        except StopIteration:
            pass

        return False

print("********")

with MyCtx(my_gen) as obj:
    print(obj)