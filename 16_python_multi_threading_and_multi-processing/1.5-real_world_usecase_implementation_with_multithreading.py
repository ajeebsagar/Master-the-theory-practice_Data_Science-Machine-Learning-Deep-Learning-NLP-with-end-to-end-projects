import multiprocessing
import math
import sys
import time
sys.set_int_max_str_digits(100000)

## function to compute factorials of a given number
def compute_factorial(number):
    sys.set_int_max_str_digits(0)  # Disable limit in worker process
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result


if __name__ == "__main__":
    numbers=[50000,60000,70000,80000,90000]

    start_time=time.time()

    ## create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results=pool.map(compute_factorial,numbers)


    end_time=time.time()
    print(f"Computed {len(results)} factorials successfully")
    print(f"Time taken: {end_time - start_time} seconds")