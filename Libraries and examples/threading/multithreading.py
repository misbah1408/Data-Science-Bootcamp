# Multithreading
# Running multiple threads at the same time inside one process.
# Useful for tasks like waiting for web requests, downloading files, or anything I/O-bound.

import threading
import time

def print_numbers(n=5):
    for i in range(n):
        time.sleep(2)
        print(f"Number :{i}")

def print_letters(letters='abcde'):
    for letter in letters:
        time.sleep(2)
        print(f"Letter :{letter}")

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t = time.time()

# start the thread
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()

finished_time = time.time() - t
print("finished_time :", finished_time)