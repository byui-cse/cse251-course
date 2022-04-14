"""
Course: CSE 251
Lesson Week: 08
File: team.py
Instructions:
- Look for TODO comments
"""

import time
import random
import threading
import multiprocessing as mp

# Include cse 251 common Python files - Dont change
from cse251 import *

# -----------------------------------------------------------------------------
# Python program for implementation of MergeSort
# https://www.geeksforgeeks.org/merge-sort/
def merge_sort(arr):

    # base case of the recursion - must have at least 2+ items
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr) // 2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        merge_sort(L)
 
        # Sorting the second half
        merge_sort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# -----------------------------------------------------------------------------
def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))


# -----------------------------------------------------------------------------
def merge_normal(arr):
    merge_sort(arr)


# -----------------------------------------------------------------------------
def merge_sort_thread(arr):
    # TODO - Add your code here to use threads.  Each time the merge algorithm does a recursive
    #        call, you need to create a thread to handle that call
    pass


# -----------------------------------------------------------------------------
def merge_sort_process(arr):
    # TODO - Add your code here to use threads.  Each time the merge algorithm does a recursive
    #        call, you need to create a process to handle that call
    pass


# -----------------------------------------------------------------------------
def main():
    merges = [
        (merge_sort, ' Normal Merge Sort '), 
        (merge_sort_thread, ' Threaded Merge Sort '), 
        (merge_sort_process, ' Processes Merge Sort ')
    ]

    for merge_function, desc in merges:
        # Create list of random values to sort
        arr = [random.randint(1, 10_000_000) for _ in range(1_000_000)]

        print(f'\n{desc:-^70}')
        print(f'Before: {str(arr[:5])[1:-1]} ... {str(arr[-5:])[1:-1]}')
        start_time = time.perf_counter()

        merge_function(arr)

        end_time = time.perf_counter()
        print(f'Sorted: {str(arr[:5])[1:-1]} ... {str(arr[-5:])[1:-1]}')

        print('Array is sorted' if is_sorted(arr) else 'Array is NOT sorted')
        print(f'Time to sort = {end_time - start_time:.14f}')


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    main()

