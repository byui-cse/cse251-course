![](../site/banner.png)

# 04 Prepare: Queues, Lock and Semaphores

## Overview

This week's lesson is on thread synchronization and sharing of data between threads


> **Hint from Instructor**
> 
> Please take the time to copy these code samples in the reading material to try them on your computer.


## Review of what is shared between threads

The definition of a process is a program that has been loaded into memory.  All processes contain a main thread.  Once the main thread finishes, the process is also finished.  

On the left side of the figure below, this process has the main thread running.  This thread has full access to data, files, registers and stack.

The right hand side of the figure shows three threads running in a process.  Nore that they all shared the common data and files of the process.  However, each thread has their own regstiers and stack.

Any global variables created before threads are created are shared with each thread.  Although, we don't like to use global variables, they are used in multi-threaded and multi-processor programs.  They will be used sparingly in the course.

![](single-and-multithreaded-process.png)
-- https://www.studytonight.com/operating-system/multithreading

The `threading` module in Python contains data structures to help with the sharing of data and synchronization.

## Thread queues

One data structure that is used is called a queue.  It is a FIFO structure (First-In First-Out).  Items are added to the queue at one end. (This is the Python put() function).  Then items are removed from the other end. (Python uses the get() function)

It is called a FIFO because the first items placed into the queue are the first one removed.

![](queue.png)


[Python documentation on threading queue](https://docs.python.org/3/library/queue.html)

The threading.Queue() data structure is thread safe which means that the `get()` and `put()` when used will add or remove an item from the queue without race conditions.  These methods are sometimes called atomic.

Here is an example of creating and using a queue from the threading module

```python
import threading, queue

q = queue.Queue()

q.put('House')
q.put('tree')
q.put('Farm')
q.put('Truck')

print(f'Size of queue = {q.qsize()}')
print(q.get())

print(f'Size of queue = {q.qsize()}')
print(q.get())
```

Output:

```
Size of queue = 4
House
Size of queue = 3
tree
```

**get() method**

For the threading.Queue(), if a thread uses `get()` on a queue where there is no items in it, that thread will be suspended until there is something in the queue.  If an item is never added to the queue, this is a deadlock situation.

Example of using a queue in a thread:


```python
import threading, queue

def thread_function(q):
    item = q.get()
    print(f'Thread: {item}')

def main():
	q = queue.Queue()

	q.put('one')
	q.put('two')
	q.put('three')

	# Create 3 threads
	threads = [threading.Thread(target=thread_function, args=(q, )) for _ in range(3)]

	for i in range(3):
		threads[i].start()

	for i in range(3):
		threads[i].join()

	print('All work completed')

if __name__ == '__main__':
	main()
```

Output:

```
Thread: one
Thread: two
Thread: three
All work completed
```

## Review of Thread locks

Locks are used to protect a critical section in your program.  Critical sections can be variables, data structures, file access, database access, etc.  If locks are used too often, then the program becomes linear in execution.  The best situation in designed threaded programs is to not use locks at all.  In the vidoe processing assignment, each process was able to work without any synchronization between them.

[Threading locks](https://docs.python.org/3/library/threading.html#lock-objects)


### Lock example 1

Here is a small Python program that will create three threads where each one will update the first item in a list.  Then it will display the results.  In the code below, it displays the correct value of 30,000.

```python
import threading

def thread_function(lock, data):
    for i in range(10000):
        data[0] += 1

def main():    
    lock = threading.Lock()

    data = [0]

    # Create 3 threads
    threads = [threading.Thread(target=thread_function, args=(lock, data)) for _ in range(3)]

    for i in range(3):
        threads[i].start()

    for i in range(3):
        threads[i].join()

    print(f'All work completed: {data}')

if __name__ == '__main__':
    main()
```

Output:

```
All work completed: [30000]
```

### Lock example 2

Same program, but each thread will try to update the item in the list 1,000,000 times

```python
import threading

def thread_function(lock, data):
    for i in range(1000000):
        data[0] += 1

def main():    
    lock = threading.Lock()

    data = [0]

    # Create 3 threads
    threads = [threading.Thread(target=thread_function, args=(lock, data)) for _ in range(3)]

    for i in range(3):
        threads[i].start()

    for i in range(3):
        threads[i].join()

    print(f'All work completed: {data}')

if __name__ == '__main__':
    main()
```

Output:

```
All work completed: [2252529]
```

The results should have been 3,000,000 but it calculated a value of 2,252,529.  In fact, each time that the program is run, it displays a different results.

This is a race condition where the statement `data[0] += 1` is actually multiple CPU instructions where the thread can be suppended after any of them.

Also, the above example shows an important principal of code testing.  Just because it works for a small test doesn't mean it works for large tests. 

Here is the correct Python program with each thread updating the value 10,000,000 times.

```python
import threading

def thread_function(lock, data):
    for i in range(10000000):
        with lock:          # protect the data
            data[0] += 1
        
def main():    
    lock = threading.Lock()

    data = [0]

    # Create 3 threads
    threads = [threading.Thread(target=thread_function, args=(lock, data)) for _ in range(3)]

    for i in range(3):
        threads[i].start()

    for i in range(3):
        threads[i].join()

    print(f'All work completed: {data}')

if __name__ == '__main__':
    main()
```

Output:

```
All work completed: [30000000]
```

This correct version of the program took about 50 seconds to run.  All of the time was taken by locking and unlocking the critical section.  A better solution for this code would be to remove the lock.  Here is a version without any locks.  This version took a little over two seconds to complete.

Using `data = [0] * 3` where each thread has their own value they can update without conflicts with the other threads allows the program remove the lock.

```python
import threading

def thread_function(thread_id, lock, data):
    for i in range(10000000):
        data[thread_id] += 1

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

## Thread semaphores

- [Thread Semaphore Document](https://docs.python.org/3/library/threading.html#semaphore-objects)
- [Wikipedia page](https://en.wikipedia.org/wiki/Semaphore_(programming))

> In computer science, a semaphore is a variable or abstract data type used to control access to a common resource by multiple processes and avoid critical section problems in a concurrent system such as a multitasking operating system. A trivial semaphore is a plain variable that is changed (for example, incremented or decremented, or toggled) depending on programmer-defined conditions.

> A useful way to think of a semaphore as used in a real-world system is as a record of how many units of a particular resource are available, coupled with operations to adjust that record safely (i.e., to avoid race conditions) as units are acquired or become free, and, if necessary, wait until a unit of the resource becomes available.

> Semaphores are a useful tool in the prevention of race conditions; however, their use is by no means a guarantee that a program is free from these problems. Semaphores which allow an arbitrary resource count are called counting semaphores, while semaphores which are restricted to the values 0 and 1 (or locked/unlocked, unavailable/available) are called binary semaphores and are used to implement locks.

> The semaphore concept was invented by Dutch computer scientist Edsger Dijkstra in 1962 or 1963, when Dijkstra and his team were developing an operating system for the Electrologica X8. That system eventually became known as THE multiprogramming system.

Whereas a `Lock` is a "only allow one thread in at a time".  A `Semphore` allows multiple threads to enter an area of code.

When a sempahore is created, you can indiciate that number of concurrent threads that can be allowed "in".  They are used to control access to data not threads.

```python
sem = Semaphore(count)

sem.acquire()
# Do something
sem.release()
```


Each time `acquire()` is called, two outcomes are possible.  

1. If the semphore count is zero, then that thread will be suspended.  
2. If the count is >0, then the count is decreased by one and the thread gains access to the protected code.  
 
When a thread calls `release()` on the semaphore, the count is increased by one and the operating system will "wake up" any threads waiting on the semaphore.

Having a thread wait on a semaphore that is never `released()` is a deadlock situation.  Note that a semphore of 1 is the same thing as a lock.

Here is an example of using a shared queue between two threads.  Note that the number of `put()` calls must match the number of `get()` calls.  If this is not the case, you might/will have deadlock.

```python
import threading
import queue

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

    shared_q = queue.Queue()

    write = threading.Thread(target=write_thread, args=(shared_q,))
    read = threading.Thread(target=read_thread, args=(shared_q,))

    read.start()        # doesn't matter which starts first
    write.start()

    write.join()
    read.join()

if __name__ == '__main__':
    main()
```

Output:

```
0
1
2
3
4
5
6
7
8
9
```