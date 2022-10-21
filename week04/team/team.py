"""
Course: CSE 251
Lesson Week: 04
File: team.py
Author: Brother Comeau

Purpose: Team Activity

Instructions:

- See in I-Learn

"""

import threading
import queue
import requests
import json

# Include cse 251 common Python files
from cse251 import *

RETRIEVE_THREADS = 4        # Number of retrieve_threads
NO_MORE_VALUES = 'No more'  # Special value to indicate no more items in the queue

def retrieve_thread():  # TODO add arguments
    """ Process values from the data_queue """

    while True:
        # TODO check to see if anything is in the queue
        number_in_quue

        # TODO process the value retrieved from the queue

        # TODO make Internet call to get characters name and log it
        pass



def file_reader(filename, queue, log): # TODO add arguments
    """ This thread reading the data file and places the values in the data_queue """
    # TODO Open the data file "urls.txt" and place items into a queue
    with open(filename) as file:
        lines = file.readlines()

    lines = [line.rstrip() for line in lines]

    for line in lines:
        queue.put(line)

    log.write('finished reading file')
    # TODO signal the retrieve threads one more time that there are "no more values"


def main():
    """ Main function """

    log = Log(show_terminal=True)
    url_filename = "urls.txt"

    # TODO create queue
    shared_queue = queue.Queue()
    file_reader(url_filename, shared_queue)
    print(list(shared_queue.queue))
    # TODO create semaphore (if needed)
    sem = threading.Semaphore()

    # TODO create the threads. 1 filereader() and RETRIEVE_THREADS retrieve_thread()s
    # Pass any arguments to these thread need to do their job

    log.start_timer()

    # TODO Get them going - start the retrieve_threads first, then file_reader

    # TODO Wait for them to finish - The order doesn't matter

    log.stop_timer('Time to process all URLS')


if __name__ == '__main__':
    main()




