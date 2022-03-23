![](../site/banner.png)

# 09 Prepare: Pickling, Conditions and Python Packages

## Pickling

The goal of introducing Python pickling module is that pickling is used to pass objects and functions to threads/processes.  

Please read the following links:

[Python Documentation on Pickling (Read up to 'Data stream format')](https://docs.python.org/3/library/pickle.html#:~:text=%E2%80%9CPickling%E2%80%9D%20is%20the%20process%20whereby,back%20into%20an%20object%20hierarchy.)

> The pickle module implements binary protocols for serializing and de-serializing a Python object structure. “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” 1 or “flattening”; however, to avoid confusion, the terms used here are “pickling” and “unpickling”.


[Why is pickle needed for multiprocessing module in python](https://stackoverflow.com/questions/52600240/why-is-pickle-needed-for-multiprocessing-module-in-python)


> We don't need pickle, but we do need to communicate between processes, and pickle happens to be a very convenient, fast, and general serialization method for Python. Serialization is one way to communicate between processes. Memory sharing is the other. Unlike memory sharing, the processes don't even need to be on the same machine to communicate. For example, PySpark using serialization very heavily to communicate between executors (which are typically different machines).

Here is an example of pickling a dictionary and unpickling it

```python
# Taken from:
# https://www.geeksforgeeks.org/understanding-python-pickling-example/

import pickle 

# initializing data to be stored in db 
Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak', 'age' : 21, 'pay' : 40000} 
Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak', 'age' : 50, 'pay' : 50000} 
  
# database 
db = {} 
db['Omkar'] = Omkar 
db['Jagdish'] = Jagdish 

print('Before:')
print(db) 

# For storing 
b = pickle.dumps(db)       # type(b) gives <class 'bytes'> 
print()
print(type(b))

# For loading 
print('\nAfter:')
myEntry = pickle.loads(b) 
print(myEntry) 
```

output:

```
Before:
{'Omkar': {'key': 'Omkar', 'name': 'Omkar Pathak', 'age': 21, 'pay': 40000}, 'Jagdish': {'key': 'Jagdish', 'name': 'Jagdish Pathak', 'age': 50, 'pay': 50000}}

<class 'bytes'>

After:
{'Omkar': {'key': 'Omkar', 'name': 'Omkar Pathak', 'age': 21, 'pay': 40000}, 'Jagdish': {'key': 'Jagdish', 'name': 'Jagdish Pathak', 'age': 50, 'pay': 50000}}
```

## Conditions

Please read the following links on Conditions.

[Python Documentation on Conditions](https://docs.python.org/3/library/threading.html#condition-objects)
[Condition Object - Thread Synchronization in Python](https://www.studytonight.com/python/python-threading-condition-object)


A condition is like a lock but with a list or queue of threads waiting on that lock.  After a thread acquires a condition and is finished with it, it has the choice to notify the waiting threads.  It can notify one to N of them or all of them. The notified thread is not awakened until the thread that acquired the condition releases it.

### Condition Example

In the example below, there are two consumer threads and one producer.  The main code will start 1 consumer, sleep a little to allow it to start running before the others.  Then it will start the other consumer and sleep again. 

This example is not using `acquire()` and `release()`.  Instead, it uses `wait()` and `nofity()`.

Each consumer waits on the condition.  Here because of the sleep() statements in the main function, both consumers will wait to be notified.

The producer can notify one or all of the threads waiting on the condition.  Here, it notifies all of them.  You could imagine you could use a condition to act like a barrier between threads. 


Example from [Website link](https://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_Condition_Objects_Producer_Consumer.php)

```python
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def consumer(cv):
    logging.debug('Consumer thread started ...')
    with cv:
        logging.debug('Consumer waiting ...')
        cv.wait()
        logging.debug('Consumer consumed the resource')

def producer(cv):
    logging.debug('Producer thread started ...')
    with cv:
        logging.debug('Making resource available')
        logging.debug('Notifying to all consumers')
        cv.notifyAll()

if __name__ == '__main__':
    condition = threading.Condition()
    cs1 = threading.Thread(name='consumer1', target=consumer, args=(condition,))
    cs2 = threading.Thread(name='consumer2', target=consumer, args=(condition,))
    pd = threading.Thread(name='producer', target=producer, args=(condition,))

    cs1.start()
    time.sleep(2)
    cs2.start()
    time.sleep(2)
    pd.start()
```

output:

```
(consumer1) Consumer thread started ...
(consumer1) Consumer waiting ...
(consumer2) Consumer thread started ...
(consumer2) Consumer waiting ...
(producer ) Producer thread started ...
(producer ) Making resource available
(producer ) Notifying to all consumers
(consumer2) Consumer consumed the resource
(consumer1) Consumer consumed the resource
```

## Python Packages

There are a number of packages included in Python or can be installed to handle concurrency and parallelism.  There are packages for computer clusters and cloud computing. Here are just a few.  A more complete list can be [found here](https://wiki.python.org/moin/ParallelProcessing)

### Single System Computing

#### threading

Package used to add threads.

> CPython implementation detail: In CPython, due to the Global Interpreter Lock, only one thread can execute Python code at once (even though certain performance-oriented libraries might overcome this limitation). If you want your application to make better use of the computational resources of multi-core machines, you are advised to use `multiprocessing` or `concurrent.futures.ProcessPoolExecutor`. However, threading is still an appropriate model if you want to run multiple I/O-bound tasks simultaneously.


#### multiprocessing

> `multiprocessing` is a package that supports spawning processes using an API similar to the threading module. The multiprocessing package offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. Due to this, the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine. It runs on both Unix and Windows.

#### subprocess

> The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. 

This is a low-level package, more control of threads, but more work for the programmer.


#### Ray

Parallel (and distributed) process-based execution framework which uses a lightweight API based on dynamic task graphs and actors to flexibly express a wide range of applications. Uses shared-memory and zero-copy serialization for efficient data handling within a single machine. Supports low-latency and high-throughput task scheduling. Includes higher-level libraries for machine learning and AI applications. Supports Python 2 and 3. (Linux, Mac)


#### Joblib

Joblib is a set of tools to provide lightweight pipelining in Python. In particular: 1) transparent disk-caching of functions and lazy re-evaluation (memoize pattern). 2) easy simple parallel computing (single computer)


### Cluster Computing

#### Celery

Celery is a simple, flexible, and reliable distributed system to process vast amounts of messages, while providing operations with the tools required to maintain such a system.

It’s a task queue with focus on real-time processing, while also supporting task scheduling.

Celery is Open Source and licensed under the BSD License.


#### Dask

Dask is a flexible library for parallel computing in Python. It offers

Dynamic task scheduling optimized for computation. This is similar to Airflow, Luigi, Celery, or Make, but optimized for interactive computational workloads.

"Big Data" collections like parallel arrays, dataframes, and lists that extend common interfaces like NumPy, Pandas, or Python iterators to larger-than-memory or distributed environments. These parallel collections run on top of dynamic task schedulers.

It extends Numpy/Pandas data structures allowing computing on many cores, many servers and managing data that does not fit in memory

#### Ray

(See `Ray` description above)

### Cloud Computing


#### Goggle App Engine

Key features

**Popular programming languages**

Build your application in Node.js, Java, Ruby, C#, Go, Python, or PHP—or bring your own language runtime.

**Open and flexible**

Custom runtimes allow you to bring any library and framework to App Engine by supplying a Docker container.

**Fully managed**

A fully managed environment lets you focus on code while App Engine manages infrastructure concerns.

#### pycompss

PyCOMPSs is a framework which aims to ease the development and execution of Python parallel applications for distributed infrastructures, such as Clusters and Clouds.

#### StarCluster

StarCluster is an open source cluster-computing toolkit for Amazon’s Elastic Compute Cloud (EC2) released under the LGPL license.

StarCluster has been designed to automate and simplify the process of building, configuring, and managing clusters of virtual machines on Amazon’s EC2 cloud. StarCluster allows anyone to easily create a cluster computing environment in the cloud suited for distributed and parallel computing applications and systems.


### Links to Articles

- [Python libraries for parallel processing](https://aaltoscicomp.github.io/python-for-scicomp/parallel/)
- [Parallel Processing and Multiprocessing in Python](https://wiki.python.org/moin/ParallelProcessing))
