"""
Course: CSE 251
Lesson Week: 01 - Team Acvitiy
File: team-solution.py
Author: Brother Comeau

Purpose: Find prime numbers

"""

from datetime import datetime, timedelta
import threading


# Include cse 251 common Python files
from cse251 import *

prime_count = 0
numbers_processed = 0

def is_prime(n: int):
    global numbers_processed
    numbers_processed += 1

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


def process_range(start, end):
    global prime_count
    for i in range(start, end):
        if is_prime(i):
            prime_count += 1
            print(i, end=', ', flush=True)


if __name__ == '__main__':
    log = Log(show_terminal=True)
    log.start_timer()

    start = 10000000000
    range_count = 100000

    number_threads = 10
    threads = []
    thread_range = range_count // number_threads

    # Create threads and give each one a range to test
    for i in range(10):
        thread_start = start + (thread_range * i)
        thread_end = thread_start + thread_range
        t = threading.Thread(target=process_range, args=(thread_start, thread_end))
        threads.append(t)

    # Start all threads
    for t in threads:
        t.start()

    # Wait for them to finish
    for t in threads:
        t.join()

    # Should find 4306 primes
    log.write(f'Numbers processed = {numbers_processed}')
    log.write(f'Primes found = {prime_count}')
    log.stop_timer('Total time')

