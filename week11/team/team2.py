"""
Course: CSE 251
Lesson Week: 11
File: team2.py
Author: Brother Comeau

Purpose: Team Activity 2: Queue, Stack

Instructions:

Part 1:
- Create classes for Queue_t and Stack_t that are thread safe.
- You can use the List() data structure in your classes.
- Once written, test them using multiple threads.

Part 2
- Create classes for Queue_p and Stack_p that are process safe.
- You can use the List() data structure in your classes.
- Once written, test them using multiple processes.

Queue methods:
    - constructor(<no arguments>)
    - size()
    - get()
    - put(item)

Stack methods:
    - constructor(<no arguments>)
    - push(item)
    - pop()

Steps:
1) write the Queue_t and test it with threads.
2) write the Queue_p and test it with processes.
3) Implement Stack_t and test it 
4) Implement Stack_p and test it 

Note: Testing means having lots of concurrency/parallelism happening.  Also
some methods for lists are thread safe - some are not.

"""
import time
import threading
import multiprocessing as mp

# -------------------------------------------------------------------
class Queue_t:
	pass

# -------------------------------------------------------------------
class Stack_t:
	pass

# -------------------------------------------------------------------
class Queue_p:
	pass

# -------------------------------------------------------------------
class Stack_p:
	pass


def main():
    pass

if __name__ == '__main__':
    main()
