"""
Course: CSE 251
Lesson Week: 07
File: assingnment.py
Author: <Your name here>

Purpose: Process Task Files

Instructions:

- run the Python program "create_tasks.py" to create the task files.
- There are 5 different tasks that need to be processed.  Each task needs to
  have it's own process pool.  The number of processes in each pool is up to
  you.  However, your goal is to process all of the tasks as quicky as possible
  using these pools.  You will need to try out different pool sizes.
- The program will load a task one at a time and add it to the pool that is used
  to process that task.  You can't load all of the tasks into memory/list and
  then pass them to a pool.
- You are required to use the function apply_async() for these 5 pools. You can't
  use map(), or any other pool function.
- Each pool will collect that results of their tasks into a global list.
  (ie. result_primes, result_words, result_upper, result_sums, result_names)
- the task_* functions contain general logic of what needs to happen
"""

from datetime import datetime, timedelta
import requests
import multiprocessing as mp
from matplotlib.pylab import plt
import numpy as np
import glob
import math 

# Include cse 251 common Python files - Dont change
import os, sys
sys.path.append('../../code')
from cse251 import *

TYPE_PRIME  = 'prime'
TYPE_WORD   = 'word'
TYPE_UPPER  = 'upper'
TYPE_SUM    = 'sum'
TYPE_NAME   = 'name'

# Global lists to collect the task results
# Note: Global variables work here because as are using threads and not processes
result_primes = []
result_words = []
result_upper = []
result_sums = []
result_names = []

def is_prime(n: int):
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
 
def task_prime(value):
    """
    Add the following to the global list:
        {value} is prime
            - or -
        {value} is not prime
    """
    pass

def task_word(word):
    """
    search in file 'words.txt'
    Add the following to the global list:
        {word} Found
            - or -
        {word} not found *****
    """
    pass

def task_upper(text):
    """
    Add the following to the global list:
        {text} ==>  uppercase version of {text}
    """
    pass

def task_sum(start_value, end_value):
    """
    Add the following to the global list:
        sum of {start_value:,} to {end_value:,} = {total:,}
    """
    pass

def task_name(url):
    """
    use requests module
    Add the following to the global list:
        {url} has name <name>
            - or -
        {url} had an error receiving the information
    """
    pass

def log_list(lst, log):
    for item in lst:
        log.write(item)
    log.write(' ')

def main():
    log = Log(show_terminal=True)
    log.start_timer()

    # TODO Create process pools

    count = 0
    task_files = glob.glob("*.task")
    for filename in task_files:
        # print()
        # print(filename)
        task = load_json_file(filename)
        print(task)
        count += 1
        task_type = task['task']
        if task_type == TYPE_PRIME:
            task_prime(task['value'])
        elif task_type == TYPE_WORD:
            task_word(task['word'])
        elif task_type == TYPE_UPPER:
            task_upper(task['text'])
        elif task_type == TYPE_SUM:
            task_sum(task['start'], task['end'])
        elif task_type == TYPE_NAME:
            task_name(task['url'])
        else:
            log.write(f'Error: unknown task type {task_type}')


    # TODO start and wait pools

    log.write('-' * 80)
    log.write(f'Primes: {len(result_primes)}')
    log_list(result_primes, log)

    log.write('-' * 80)
    log.write(f'Words: {len(result_words)}')
    log_list(result_words, log)

    log.write('-' * 80)
    log.write(f'Uppercase: {len(result_upper)}')
    log_list(result_upper, log)

    log.write('-' * 80)
    log.write(f'Sums: {len(result_sums)}')
    log_list(result_sums, log)

    log.write('-' * 80)
    log.write(f'Names: {len(result_names)}')
    log_list(result_names, log)

    log.write(f'Primes: {len(result_primes)}')
    log.write(f'Words: {len(result_words)}')
    log.write(f'Uppercase: {len(result_upper)}')
    log.write(f'Sums: {len(result_sums)}')
    log.write(f'Names: {len(result_names)}')
    log.stop_timer(f'Finished processes {count} tasks')

if __name__ == '__main__':
    main()
