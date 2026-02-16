## multithreading with ThreadPoolExecutor

from concurrent.futures import ThreadPoolExecutor
import time
def print_numbers(n):
    for i in range(5):
        time.sleep(1)
        print(f"Number {n}: {i}")

numbers=[1,2,3,4,5]

with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_numbers,numbers)

for result in results:
    print(result)