## multithreading 
## when to use multithreading in python
## 1. I/O-bound tasks: Multithreading is beneficial for tasks that involve a lot of waiting for I/O operations, such as reading/writing files, making network requests, or interacting with databases. Threads can continue executing while waiting for I/O operations to complete, improving overall efficiency.
## 2. GUI applications: In graphical user interface (GUI) applications, multithreading

import threading
import time
def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Number: {i}")


def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        time.sleep(1)
        print(f"Letter: {letter}")


## create  2 threads

te=threading.Thread(target=print_numbers)
tl=threading.Thread(target=print_letters)        

t=time.time()
te.start()
tl.start()
te.join()
tl.join()
finished_time=time.time()-t
print(f"Finished in {finished_time}")