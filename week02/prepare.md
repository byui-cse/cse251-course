![](../site/banner.png)

# 02 Prepare: Class Threads and Communication

## Overview

Last week, we learned to create threads that are considered "stand alone" or independent -- meaning that when that thread is running, it doesn't effect other threads. Also, there was no communication between threads.  This week, we are learning about the communication tools that allow threads to work together.

## States of a Thread

The operating system (Windows, Mac, Linux, etc.) is in control of managing threads.  The following diagram outlines the different states of a thread.

![](process_states.png)

**Created**

When a thread is first started, it is in the created state.  This is where the operating system creates the thread's memory and resources for managing the thread.

**Waiting**

This state is where the thread is waiting to run on the computer's CPU.  There can be many threads in this state and they are in a queue.

**Running**

This is the state where the thread is running on a CPU.  There are three ways that a thread can be removed from this state:

1. The thread finishes.  It goes to the `terminated` state.
1. The thread makes an I/O (input / output) call.  Examples of I/O calls are reading/writing to a file, making an Internet request, printing to a terminal window, etc.  Because these I/O calls take time, that thread is placed on the blocked queue and has state of `blocked`.
1. Each thread is given only a short amount of time to run on the CPU.  This time is called a time slice.  If the time on the CPU is finished, the thread is placed back to the waiting queue to be run again (in turn) on the CPU.

**Blocked**

Here the thread is waiting for an I/O request to be completed.  When the operating system completes the I/O request, that thread is moved to the waiting queue.

**Terminated**

When the thread is finished, it moves to the terminated state.  Here the operating system can free any resources used by the thread.

### I/O bound and CPU Bound code

- CPU bound code will bounce between `running` and `waiting` states.
- I/O bound code will cycle between `running` -> `blocked` -> `waiting` states.


## Thread Objects

Python allows the creation of threaded classes.  Instead of just having a function that is a thread, a threaded class allows for more complex code.

[Review of classes in Python](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)

There are two methods that you must implement for a threaded class (You can create others if your class needs them)

**`__init__()`**

This method is used to initialize the instance of the object you just created and to call the parent class' constructor.  You are free to add any number of arguments that you require.  This method needs to call the parent or super class's \_\_init\_\_ method.

**`run()`**

After you create an instance of this class, when you call the start() method, this `run()` method will be executed.  The only method this argument has is `self`. When the `run()` exits, then the thread is finished.  Within the  `run()` method, you can call other methods in your class if you have them.

```python
import threading
import time

class Display_Hello(threading.Thread):

    # constructor
    def __init__(self, number, message):
        # calling parent class constructor
        super().__init__()

        # Create or assign any variables that you need
        self.number = number
        self.message = message
    
    # This is the method that is run when start() is called
    def run(self):
        time.sleep(self.number)
        print(f'Message: {self.message}')
    

if __name__ == '__main__':
	hello1 = Display_Hello(2, 'Hello from thread 2')
	hello2 = Display_Hello(1, 'Hello from thread 1')

	hello1.start()
	hello2.start()

	hello1.join()
	hello2.join()
```

Output:

```text
Message: Hello from thread 1
Message: Hello from thread 2
```

Here is an example of a threaded class "returning" a value.  After the thread is finished, any variables in the instance object can be accessed.

```python
import threading

class Add_Two(threading.Thread):

    # constructor
    def __init__(self, number):
        # calling parent class constructor
        threading.Thread.__init__(self)
        self.number = number
    
    # This is the method that is run when start() is called
    def run(self):
    	# Create a new variable to hold the answer/results
    	# This variable is public and can be used in the
    	# main function.
    	self.results = self.number + 2
   

if __name__ == '__main__':
	add1 = Add_Two(100)
	add2 = Add_Two(200)

	add1.start()
	add2.start()

	add1.join()
	add2.join()

	print(f'Add_Two(100) returns {add1.results}')
	print(f'Add_Two(200) returns {add2.results}')

```

Output:

```text
Add_Two(100) returns 102
Add_Two(200) returns 202
```

## What is shared between Threads?

You can easily share resources between threads. Any global variables are shared.  As programmers, we don't like global variables because of the side-effects that can happen with them.  The shared data doesn't have to be a global variable, if you pass the same list or dictionary to threads, then they are sharing that object.

Each thread has its own function stack.  This means that local variables that are created in a thread are unique to that thread.

We will learn about other data elements that are used for sharing data between threads and processes later in the course.

## Race Conditions and Deadlock

First, we need to understand issues with when threads share resources such as memory, or files.

### Race Condition

[Race Condition Wikipedia](https://en.wikipedia.org/wiki/Race_condition)

> A race condition arises in software when a computer program, to operate properly, depends on the sequence or timing of the program's processes or threads. Critical race conditions cause invalid execution and software bugs. Critical race conditions often happen when the processes or threads depend on some shared state. Operations upon shared states are done in critical sections that must be mutually exclusive. Failure to obey this rule can corrupt the shared state.

> A race condition can be difficult to reproduce and debug because the end result is nondeterministic and depends on the relative timing between interfering threads. Problems of this nature can therefore disappear when running in debug mode, adding extra logging, or attaching a debugger. Bugs that disappear like this during debugging attempts are often referred to as a "Heisenbug". It is therefore better to avoid race conditions by careful software design.

(The following is from the Wikipedia page on race conditions)

Assume that two threads each increment the value of a global integer variable by 1. Ideally, the following sequence of operations would take place: (Note that read and write below refers to reading the value from memory into the CPU and writing the value back to memory.  This is also true when using CPU registers)

![](race1.png)

In the case shown above, the final value is 2, as expected. However, if the two threads run simultaneously without locking or synchronization, the outcome of the operation could be wrong. The alternative sequence of operations below demonstrates this scenario:

![](race2.png)

In this case, the final value is 1 instead of the correct result of 2. This occurs because here the increment operations are not mutually exclusive. Each thread can be removed from the `running` state and placed in the `waiting` state at any time. Mutually exclusive operations are those that cannot be interrupted while accessing some resource such as a memory location.

### Deadlock

[Deadlock Wikipedia](https://en.wikipedia.org/wiki/Deadlock)

> In concurrent computing, a deadlock is a state in which each member of a group waits for another member, including itself, to take action, such as sending a message or more commonly releasing a lock. Deadlock is a common problem in multiprocessing systems, parallel computing, and distributed systems, where software and hardware locks are used to arbitrate shared resources and implement process synchronization.

> In an operating system, a deadlock occurs when a process or thread enters a waiting state because a requested system resource is held by another waiting process, which in turn is waiting for another resource held by another waiting process. If a process is unable to change its state indefinitely because the resources requested by it are being used by another waiting process, then the system is said to be in a deadlock.

For example:  Lets have two threads with two locks.  The thread `thread1` will acquire lock `a` then `b`.  Where, `thread2` will acquire lock `b` then `a`.  Both threads will wait forever when causing a deadlock as each thread locks a lock that the other needs.

```python
a = Lock()
b = Lock()

def thread1(data):
    a.acquire()
    b.acquire()

    # do something

    b.release()
    a.release()

def thread2(data):
    b.acquire()
    a.acquire()

    # do something

    a.release()
    b.release()
```

## Synchronization Tools

In order to control access to shared resources between threads, you can use `locks` and `semphores`.

### Lock

We saw last lesson that a lock can be used to protect a critical section. (ie., you need to ensure that only 1 thread accesses a block of code as a time).  Below is the coding example from last lesson.  The lock in this case is global to the thread function.  This lock can be passed to the function as an argument.


```python
lock = threading.Lock()

def thread_func(filename, count):
    # acquire the lock before entering the critical section
    # If another thread has the lock, this thread will wait
    # until it's released.
    lock.acquire()
    
    # Do your stuff.  Only 1 thread is running this code
    f = open(filename, 'w')
    f.write(count)
    f.close()

    # release the lock.  If you fail to release the lock,
    # the next thread that tried to acquire the lock will
    # wait forever since the release will never happen.
    lock.release()
```

**Rules when using locks**

1. Don't over do it.  The more locks you add to a program, the less parallel and concurrent it becomes.  If you do need to use locks in your code, just use the minimum required.  Remember that you don't lock threads, just shared data.
2. Try to keep the code in the critical section as small and fast as possible.  Since only one thread can enter a critical section at a time, all others are waiting.  If you have a critical section that takes a long time to execute, then your program will be slow.
3. Try to limit any I/O statements. (ie., file access, print() statements). The reason for this, it that the thread making the I/O request will be placed on the `blocked` queue.   **NEVER** put an `input()` statement in a critical section unless you have a really good reason (And I would like to hear it).


## Thread Safe

> Thread safety is a computer programming concept applicable to multi-threaded code. Thread-safe code only manipulates shared data structures in a manner that ensures that all threads behave properly and fulfill their design specifications without unintended interaction. There are various strategies for making thread-safe data structures.

> A program may execute code in several threads simultaneously in a shared address space where each of those threads has access to virtually all of the memory of every other thread. Thread safety is a property that allows code to run in multithreaded environments by re-establishing some of the correspondences between the actual flow of control and the text of the program, by means of synchronization.

Modern concurrent and parallel programming languages will list which functions and data structures are "thread safe".  This means that the function/data structure can be used in threads.  

For example: in the language C++, the `rand()` function is not thread safe.  If `rand()` is called in threads, the values returned by the `rand()` function will not be random.

Note that individual methods such as `append()` for list/set are thread safe in that if you call this method, you can be sure that the item was appended to the list/set.  However, in most cases, you are doing more to a list/set/dict than just one method call. You can still have a race condition "between" the method statements.
