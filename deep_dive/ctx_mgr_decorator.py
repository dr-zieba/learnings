

def context_decorator(f_gen):
    def inner(*args, **kwargs):
        gen = f_gen(*args, **kwargs)
        return gen
    return inner