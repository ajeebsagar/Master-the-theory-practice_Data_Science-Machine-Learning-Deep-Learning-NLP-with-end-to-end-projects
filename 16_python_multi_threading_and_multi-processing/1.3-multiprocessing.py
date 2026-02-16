## process that run is parallel
## cpu-Bound Tasks
## parallel execution- multiple cpu cores

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i * i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i * i * i}")        


if __name__ == "__main__":

    ## create  2 processes
    pe=multiprocessing.Process(target=square_numbers)
    pc=multiprocessing.Process(target=cube_numbers)
    t=time.time()

    ## start the processes
    pe.start()
    pc.start()
    t=time.time()
    pe.join()
    pc.join()
    finished_time=time.time()-t
    print(f"Finished in {finished_time}")