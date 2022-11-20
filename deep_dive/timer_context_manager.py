from time import perf_counter, sleep

class Timer:
    def __init__(self):
        self.timer = 0

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.timer = perf_counter() - self.start
        return False


with Timer() as t:
    print("asdlasldasld")
    sleep(1)

print(t.timer)