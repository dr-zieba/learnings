import threading
import time

def my_function():
    print("Start\n")
    time.sleep(3)
    print("End\n")

threads = []

for i in range(5):
    th = threading.Thread(target = my_function)
    th.start()
    threads.append(th)

for th in threads:
    th.join()
