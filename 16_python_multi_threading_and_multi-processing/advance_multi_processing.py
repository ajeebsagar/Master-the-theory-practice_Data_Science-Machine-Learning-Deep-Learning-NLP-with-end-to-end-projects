## multiprocessing with process pool Executer

from concurrent.futures import ProcessPoolExecutor
import time
def square_numbers(n):
    for i in range(5):
        time.sleep(1)
        print(f"Square {n}: {i * i}")

if __name__ == '__main__':
    numbers=[1,2,3,4,5]
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(square_numbers,numbers)
    
    for result in results:
        print(result)

