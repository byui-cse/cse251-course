"""
Course: CSE 251
Lesson Week: 10
File: assignment.py
Author: <your name>

Purpose: assignment for week 10 - reader writer problem

Instructions:

- Review TODO comments
- writer: a process that will "write"/send numbers to the reader.  
  To keep things simple, have the writer send consecutive numbers starting at 1.
- reader: a process that receive numbers sent by the writer.
- You don't need any sleep() statements for either process.
- You are able to use lock(s) and semaphores(s).
- You must use shared_memory block between the two processes.  
  This shared memory must be at least BUFFER_SIZE in size, but
  can be larger if you need to store other values.
- Not allowed to use Queue(), Pipe(), or any other data structure.
- Not allowed to use Value() or Array() from the multiprocessing package.

Add any comments for me:



"""
import random
from multiprocessing import shared_memory
import multiprocessing as mp

BUFFER_SIZE = 10

def main():

    # This is the number of values that the writer will send to the reader
    items_to_send = random.randint(100000, 1000000)

    # TODO - Create shared_memory block to be used between the processes

    # TODO - Create any lock(s) or semaphore(s) that you feel you need

    # TODO - create reader and writer processes

    # TODO - Start the processes and wait for them to finish

    print(f'{items_to_send} sent by the writer')

    # TODO - Display the number of numbers/items received by the reader.

    pass

if __name__ == '__main__':
    main()
