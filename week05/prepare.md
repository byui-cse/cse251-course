![](../site/banner.png)


# 05 Prepare: Process Communication and Barriers

## Overview

When sharing information between processes in Python, there are limits on what we can do.  We will cover those issues here as well as understanding barriers.

## Preparation Material

## Issues with sharing data between processes

It was easy to create shared data structures that work between threads.  This is because there is only one GIL running and all threads can share the program's memory.

Processes in Python are different since when you create a process, you create a new GIL.  Each process/GIL has it's own memory, stack, registers.  The `multiprocessing` module supplies us with a few options for sharing data between processes.

First, lets review the problem in a few examples. In the following example from last lesson, we have three threads all sharing the same list.  This list contains three values `[0, 0, 0]` before the threads are started and it is passed to each thread.

```python
import threading

def thread_function(thread_id, lock, data):
    # Only change the value in the list based on thread_id
    for i in range(10):
        data[thread_id] += 1
    print(f'Process {thread_id}: {data}')

def main():    
    lock = threading.Lock()

    # Create a value with each thread
    data = [0] * 3

    # Create 3 threads, pass a "thread_id" for each thread
    threads = [threading.Thread(target=thread_function, args=(i, lock, data)) for i in range(3)]

    for i in range(3):
        threads[i].start()

    for i in range(3):
        threads[i].join()

    print(f'All work completed: {sum(data)}')

if __name__ == '__main__':
    main()
```
The program generates the following output.  The thread order might be different if you run this program on your computer, but the results are the same.  Each thread only changes the value in the list based on thread_id.

```
Process 0: [10, 0, 0]
Process 1: [10, 10, 0]
Process 2: [10, 10, 10]
All work completed: 30
```

Here is the same program using processes from the `multiprocessing` module.

```python
import multiprocessing as mp 

def process_function(process_id, data):
    # only change the value based on process_id
    for i in range(10):
        data[process_id] += 1
    print(f'Process {process_id}: {data}')

def main():    
    # Create a value with each thread
    data = [0] * 3

    # Create 3 processes, pass a "process_id" for each thread
    processes = [mp.Process(target=process_function, args=(i, data)) for i in range(3)]

    for i in range(3):
        processes[i].start()

    for i in range(3):
        processes[i].join()

    print(f'All work completed: {sum(data)}')

if __name__ == '__main__':
    main()
```
The results of this program are very different from the thread version.  When each process was created, a new GIL was created for each.  In this case, each process has their own version of the list `data`.  After each process changes their version of the data list, the main code calls `join()` to wait until they are finished.  Then, main's version of the list `data` is used in the finial print() statement.  It's empty, because the processes changed a different `data` list.

In should be clear that global variables would be handled in the same method using processes, where each process has a copy of the global variables.

```
Process 0: [10, 0, 0]
Process 1: [0, 10, 0]
Process 2: [0, 0, 10]
All work completed: 0
```

### Solution to the processes sharing

The `multiprocessing` module provides a few mechanisms to help with sharing data between processes.

**mp.Queue**

A Queue from the `multiprocessing` module allows you to share a queue between processes.  Here is the code example from last lesson using processes and `mp.Queue`

```python
import multiprocessing as mp 

MAX_COUNT = 10

def read_thread(shared_q):
    for i in range(MAX_COUNT):
        # read from queue
        print(shared_q.get())

def write_thread(shared_q):
    for i in range(MAX_COUNT):
        # place value onto queue
        shared_q.put(i)

def main():
    """ Main function """

    # This queue will be shared between the processes
    shared_q = mp.Queue()

    write = mp.Process(target=write_thread, args=(shared_q,))
    read = mp.Process(target=read_thread, args=(shared_q,))

    read.start()        # doesn't matter which starts first
    write.start()

    write.join()
    read.join()

if __name__ == '__main__':
    main()
```


**mp.Pipe**

The other data structure that can be used is called a pipe.  We will be going over in detail about pipes in the next lesson.


## Managers

We have `Queue` and `Pipe` for sharing data between processes.  For all other data the `multiprocessing` module has a managers.  Managers are used for sharing between processes.  Lets go back to the process example with the shared list that didn't work.  Here is a version that does. `data = mp.Manager().list([0] * 3)` solves the data sharing issue.

```python
import multiprocessing as mp 

def process_function(process_id, data):
    for i in range(10):
        data[process_id] += 1
    print(f'Process {process_id}: {data}')

def main():    
    # Create a value with each thread
    data = mp.Manager().list([0] * 3)

    # Create 3 processes, pass a "process_id" for each thread
    processes = [mp.Process(target=process_function, args=(i, data)) for i in range(3)]

    for i in range(3):
        processes[i].start()

    for i in range(3):
        processes[i].join()

    print(f'All work completed: {sum(data)}')

if __name__ == '__main__':
    main()
```

Output from the above program.  Why was the results of the list after process 0 was finished `[10, 9, 0]` and not `[10, 10, 0]`?

```
Process 0: [10, 9, 0]
Process 1: [10, 10, 0]
Process 2: [10, 10, 10]
All work completed: 30
```

More document on managers can be [found here](https://docs.python.org/3/library/multiprocessing.html#managers).


## Barrier

We introduce a new thread and process synchronization control called a **barrier**.  Here is the [documentation](https://docs.python.org/3/library/threading.html#barrier-objects) on barriers.


> Barrier objects in python are used to wait for a fixed number of thread to complete execution before any particular thread can proceed forward with the execution of the program. Each thread calls wait() function upon reaching the barrier. The barrier is responsible for keeping track of the number of wait() calls. If this number goes beyond the number of threads for which the barrier was initialized with, then the barrier gives a way to the waiting threads to proceed on with the execution. All the threads at this point of execution, are simultaneously released.

> Barriers can even be used to synchronize access between threads. However, generally a barrier is used to combine the output of threads. A barrier object can be reused multiple times for the exact same number of threads that it was initially initialized for.

[Above quoted from geeksforgeeks.org](https://www.geeksforgeeks.org/barrier-objects-python/)

Lets say that you have three threads working on finding primes in a range of values.  Each thread will take a different amount of time to complete.  A barrier can be used to force all of the threads to wait until all of them are finished before moving on.

```python
import multiprocessing as mp 
import time

def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization.
    From: https://en.wikipedia.org/wiki/Primality_test
    """
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def process_function(process_id, barrier, start_value, end_value):
    start_time = time.perf_counter()
    primes = []
    for i in range(start_value, end_value + 1):
        if is_prime(i):
            primes.append(i)
    total_time = time.perf_counter() - start_time

    barrier.wait()  # Wait for all processes to complete the task before printing
    print(f'Process {process_id}: time = {total_time:.5f}: primes found = {len(primes)}')

def main():    

    barrier = mp.Barrier(4)         # 4 is the number of processes to wait

    # Create 4 processes, pass a "process_id" and a barrier to each thread
    processes = []
    processes.append(mp.Process(target=process_function, args=(1, barrier, 1, 1000000)))
    processes.append(mp.Process(target=process_function, args=(2, barrier, 1000000, 2000000)))
    processes.append(mp.Process(target=process_function, args=(3, barrier, 2000000, 3000000)))
    processes.append(mp.Process(target=process_function, args=(4, barrier, 3000000, 4000000)))

    for p in processes:
        p.start()

    for p in processes:
        p.join()

if __name__ == '__main__':
    main()
```

Here is the output of the program.  Notice that without the barrier, process 1 should have displayed it's results because it finished faster.

```
Process 4: time = 11.25130: primes found = 66330
Process 2: time = 8.20724: primes found = 70435
Process 3: time = 9.95771: primes found = 67883
Process 1: time = 4.23095: primes found = 78498
```


