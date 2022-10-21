"""
Course: CSE 251
Lesson Week: 06
File: team.py
Author: Brother Comeau

Purpose: Team Activity

Instructions:

- Implement the process functions to copy a text file exactly using a pipe

After you can copy a text file word by word exactly
- Change the program to be faster (Still using the processes)

"""

import multiprocessing as mp
from multiprocessing import Value, Process
import filecmp

# Include cse 251 common Python files
from cse251 import *

SENDER_END_MESSAGE = "*****THE_END*****"


def sender(conn, filename, total_items_items_list):
    """ function to send messages to other end of pipe """
    '''
    open the file
    send all contents of the file over a pipe to the other process
    Note: you must break each line in the file into words and
          send those words through the pipe
    '''
    with open(filename) as f:
        for line in f:
            split_line = line.split()
            for i, word in enumerate(split_line):
                conn.send(word)
                total_items_items_list[0] += 1
                if i != (len(split_line) - 1):
                    conn.send(" ")
                    total_items_items_list[0] += 1
            conn.send("\n")

    conn.send(SENDER_END_MESSAGE)
    conn.close()


def receiver(conn, filename):
    """ function to print the messages received from other end of pipe """
    ''' 
    open the file for writing
    receive all content through the shared pipe and write to the file
    Keep track of the number of items sent over the pipe
    '''
    received = ""
    while True:
        received_word = conn.recv()
        if received_word == SENDER_END_MESSAGE:
            break
        received += received_word

    with open(filename, 'w') as f:
        f.write(received)

    conn.close()


def are_files_same(filename1, filename2):
    """ Return True if two files are the same """
    return filecmp.cmp(filename1, filename2, shallow=False)


def copy_file(log, filename1, filename2):
    # TODO create a pipe
    parent_conn, child_conn = mp.Pipe()

    # TODO create variable to count items sent over the pipe
    TOTAL_WORDS_ITEMS_LIST = mp.Manager().list([0] * 1)

    # TODO create processes
    sender_process = mp.Process(target=sender, args=(parent_conn, filename1, TOTAL_WORDS_ITEMS_LIST))
    receiver_process = mp.Process(target=receiver, args=(child_conn, filename2))

    log.start_timer()
    start_time = log.get_time()

    # TODO start processes
    sender_process.start()
    receiver_process.start()

    # TODO wait for processes to finish
    sender_process.join()
    receiver_process.join()

    total_words_sent = TOTAL_WORDS_ITEMS_LIST[0]

    stop_time = log.get_time()

    log.stop_timer(f'Total time to transfer content')
    log.write(f'Total items sent = {total_words_sent}')
    log.write(f'items / second = {total_words_sent / (stop_time - start_time)}')

    if are_files_same(filename1, filename2):
        log.write(f'{filename1} - Files are the same')
    else:
        log.write(f'{filename1} - Files are different')


if __name__ == "__main__":
    log = Log(show_terminal=True)

    # copy_file(log, 'gettysburg.txt', 'gettysburg-copy.txt')
    
    # After you get the gettysburg.txt file working, uncomment this statement
    copy_file(log, 'bom.txt', 'bom-copy.txt')
