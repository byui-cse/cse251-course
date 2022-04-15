"""
Course: CSE 251
Lesson Week: 14
File: assignment.py
Author: <your name>
Purpose: Assignment 14 - Family Search
"""
import time
import threading
import json
import requests
from common import *
from functions import depth_fs_pedigree, breadth_fs_pedigree, breadth_fs_pedigree_limit5

# Include cse 251 common Python files - Dont change
from cse251 import *

DFS = 'Depth First Search'
BFS = 'Breadth First Search'
BFS5 = 'Breadth First Search limit 5'

def run_part(log, start_id, generations, title, func):
    tree = Tree(start_id)

    req = Request_thread(f'{TOP_API_URL}/start/{generations}')
    req.start()
    req.join()

    log.write('\n')
    log.write('#' * 60)
    log.start_timer(f'{title}: {generations} generations')
    log.write('#' * 60)
    func(start_id, tree)
    total_time = log.stop_timer()

    req = Request_thread(f'{TOP_API_URL}/end')
    req.start()
    req.join()

    tree.display(log)
    log.write('')
    log.write(f'total_time                          : {total_time:.5f}')
    log.write(f'Generations                         : {generations}')
    log.write(f'People % Families / second          : {(tree.get_person_count()  + tree.get_family_count()) / total_time:.5f}')
    log.write('')


def main():
    log = Log(show_terminal=True, filename_log='assignment.log')

    # starting family
    req = Request_thread(TOP_API_URL)
    req.start()
    req.join()

    print(f'Starting Family id: {req.response["start_family_id"]}')
    start_id = req.response['start_family_id']

    # load runs.txt
    # part number, number of generations

    with open('runs.txt') as runs:
        for line in runs:
            parts = line.split(',')
            part_to_run = int(parts[0])
            generations = int(parts[1])

            if part_to_run == 1:
                run_part(log, start_id, generations, DFS, depth_fs_pedigree)
            elif part_to_run == 2:
                run_part(log, start_id, generations, BFS, breadth_fs_pedigree)
            elif part_to_run == 3:
                run_part(log, start_id, generations, BFS5, breadth_fs_pedigree_limit5)


if __name__ == '__main__':
    main()

