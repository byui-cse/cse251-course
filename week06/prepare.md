![](../site/banner.png)

# 06 Prepare: Multiprocessing Module and Pipes

## Overview

We will be covering two parts of the multiprocessing module - Pipe and Value.  They are used to allow processes to shared information between them.

## Preparation Material

Please read the following information found in the links below.

### Links to Articles

- [Python Documentation](https://docs.python.org/3/library/multiprocessing.html#pipes-and-queues)
- [StackOverFlow: Pipe vs Queue](https://stackoverflow.com/questions/8463008/multiprocessing-pipe-vs-queue)
- [Python Shared Memory Between Processes](https://www.geeksforgeeks.org/multiprocessing-python-set-2/)
- [Pool, Process, Queue, and Pipe code examples](http://www.kasimte.com/multiprocessing-in-python-pool-process-queue-and-pipe)

## Pipe

Pipes are used to send messages (ie., data) between processes.  The following is from the Python documentation on pipes.  Note, that a pipe removes the need for a lock.  The more locks in a program, the potential of it slowing down.

> When using multiple processes, one generally uses message passing for communication between processes and avoids having to use any synchronization primitives like locks.

### Creating a pipe

When you create a pipe from the multiprocessing module, you receive both ends of the pipe.  They are called the parent and child connections in most programming languages.  (ie., the parent will send information using their connection and the child will receive information using their connection).  You can send information in both directions.  Just be careful that you don't have both processes waiting for information at the same time (ie., deadlock)

```python
import multiprocessing 

parent_connection, child_connection = multiprocessing.Pipe()
```

Here is an example of creating a pipe and passing the parent connection to the `sender` process and the child connection to the `receiver` process.  Note that if a process tries to read from a pipe using `recv()` and there is nothing to read, then the process will wait.  If nothing ever is send on that pipe, you have a deadlock situation.

```python
import multiprocessing 

def sender(conn): 
    """ function to send messages to other end of pipe """
    conn.send('Hello')
    conn.send('World')
    conn.close() 			# Close this connection when done

def receiver(conn): 
    """ function to print the messages received from other end of pipe  """
    print(f'Received: {conn.recv()}')
    print(f'Received: {conn.recv()}')

if __name__ == "__main__": 

    # creating a pipe 
    parent_conn, child_conn = multiprocessing.Pipe() 

    # creating new processes 
    p1 = multiprocessing.Process(target=sender, args=(parent_conn,)) 
    p2 = multiprocessing.Process(target=receiver, args=(child_conn,)) 

    # running processes 
    p1.start() 
    p2.start() 

    # wait until processes finish 
    p1.join() 
    p2.join() 

```

Output:

```
Received: Hello
Received: World
```


## Sharing data between processes

Normally variables can't be shared between processes because each process has a complete copy of the program - their own GIL.  However, there is a method for sharing data. We will need to use the `multiprocessing` module for this.

Here is an example from [the Python documentation website](https://docs.python.org/3/library/multiprocessing.html#sharing-state-between-processes)

[Data types for Value() function](https://docs.python.org/3/library/array.html#module-array)

```python
from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
```

Output:

```
3.1415927
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
```

Break down of the above example:

We need to import **Value** and/or **Array**. (There are other methods of sharing data, but will wait later in the course to talk about them.)

```python
from multiprocessing import Process, Value, Array
```

Next, we can use **Value** and/or **Array** to create the shared variables that will be used between processes.

For both Value and Array, they take two arguments. 

- The first one is the data type. `d` indicates a double precision float and `i` indicates a signed integer.

- The second is the initial value for Value() and for Array, it is the list of values.


```python
num = Value('d', 0.0)
arr = Array('i', range(10))
```

For other examples:

```python
count = Value('i', 0)   			   # create a shared integer count
counts = Array('i', [0, 0, 0, 0, 0])   # Create shared array of 5 values
```


Here we just pass them to the process using the `args` argument.

```python
p = Process(target=f, args=(num, arr))
```

Using these shared variables is a little different.  For shared Value() variables, you need to use `.value` to use them.  For the shared Array() variable, you use them normally using `[]`.

```python
def f(n, a):
	n.value = 3.1415927
	for i in range(len(a)):
	    a[i] = -a[i]
```

When using shared variables, remember that if there are processes writing and reading them, when you need to stop a race condition by using a shared lock.