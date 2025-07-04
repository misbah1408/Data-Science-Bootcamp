# multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(n):
    time.sleep(1)
    return f"Number: {n*n}"

if __name__ == "__main__":
    numbers = [1,2,3,4,5,6,7,8,9,10]

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)

    for result in results:
        print(result)
