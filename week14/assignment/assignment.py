"""
Course: CSE 251
Lesson Week: 14
File: assignment.py
Author: <your name>
Purpose: Assignment 13 - Family Search

Instructions:

Depth First Search
https://www.youtube.com/watch?v=9RHO6jU--GU

Breadth First Search
https://www.youtube.com/watch?v=86g8jAQug04


Describe how to sped up part 1

<Add your comments here>


Describe how to sped up part 2

<Add your comments here>


10% Bonus

<Add your comments here>

"""
import time
import threading
import multiprocessing as mp
import json
import random
import requests

# Include cse 251 common Python files - Dont change
import os, sys
sys.path.append('../../code')
from cse251 import *


TOP_API_URL = 'http://127.0.0.1:8123'


# ----------------------------------------------------------------------------
class Person:
    def __init__(self, data):
        super().__init__()
        self.id = data['id']
        self.name = data['name']
        self.parents = data['parent_id']
        self.family = data['family_id']
        self.birth = data['birth']

    def __str__(self):
        output  = f'id        : {self.id}\n'
        output += f'name      : {self.name}\n'
        output += f'birth     : {self.birth}\n'
        output += f'parent id : {self.parents}\n'
        output += f'family id : {self.family}\n'
        return output

# ----------------------------------------------------------------------------
class Family:

    def __init__(self, id, data):
        super().__init__()
        self.id = data['id']
        self.husband = data['husband_id']
        self.wife = data['wife_id']
        self.children = data['children']

    def children_count(self):
        return len(self.children)

    def __str__(self):
        output  = f'id         : {self.id}\n'
        output += f'husband    : {self.husband}\n'
        output += f'wife       : {self.wife}\n'
        for id in self.children:
            output += f'  Child    : {id}\n'
        return output

# -----------------------------------------------------------------------------
class Tree:

    def __init__(self):
        super().__init__()
        self.people = {}
        self.families = {}

    def add_person(self, person):
        if self.does_person_exist(person.id):
            print(f'ERROR: Person with ID = {person.id} Already exists in the tree')
        else:
            self.people[person.id] = person

    def add_family(self, family):
        if self.does_family_exist(family.id):
            print(f'ERROR: Family with ID = {family.id} Already exists in the tree')
        else:
            self.families[family.id] = family

    def get_person(self, id):
        if id in self.people:
            return self.people[id]
        else:
            return None

    def get_family(self, id):
        if id in self.families:
            return self.families[id]
        else:
            return None

    def get_person_count(self):
        return len(self.people)

    def get_family_count(self):
        return len(self.families)

    def does_person_exist(self, id):
        return id in self.people

    def does_family_exist(self, id):
        return id in self.families

    def _count_generations(self, family_id):
        max_gen = -1

        def _recurive_gen(id, gen):
            nonlocal max_gen
            if id in self.families:
                if max_gen < gen:
                    max_gen = gen

                fam = self.families[id]

                husband = self.get_person(fam.husband)
                if husband != None:
                    _recurive_gen(husband.parents, gen + 1)
                
                wife = self.get_person(fam.wife)
                if wife != None:
                    _recurive_gen(wife.parents, gen + 1)

        _recurive_gen(1, 1)
        return max_gen + 1

    def __str__(self):
        out = '\nTree Stats:\n'
        out += f'Number of people  : {len(self.people)}\n'
        out += f'Number of families: {len(self.families)}\n'
        out += f'Max generations   : {self._count_generations(1)}\n'
        return out


# ----------------------------------------------------------------------------
# Do not change
class Request_thread(threading.Thread):

    def __init__(self, url):
        # Call the Thread class's init function
        threading.Thread.__init__(self)
        self.url = url
        self.response = {}

    def run(self):
        response = requests.get(self.url)
        # Check the status code to see if the request succeeded.
        if response.status_code == 200:
            self.response = response.json()
        else:
            print('RESPONSE = ', response.status_code)


# -----------------------------------------------------------------------------
def depth_fs_pedigree(family_id, tree):
    if family_id == None:
        return

    print(f'Retrieving Family: {family_id}')

    req_family = Request_thread(f'{TOP_API_URL}/family/{family_id}')
    req_family.start()
    req_family.join()

    new_family = Family(family_id, req_family.response)
    tree.add_family(new_family)

    husband = None
    wife = None

    # Get husband details
    husband_id = new_family.husband
    print(f'   Retrieving Husband : {husband_id}')
    req_person = Request_thread(f'{TOP_API_URL}/person/{husband_id}')
    req_person.start()
    req_person.join()
    husband = Person(req_person.response)

    # Get wife details
    wife_id = new_family.wife
    print(f'   Retrieving Wife    : {wife_id}')
    req_person = Request_thread(f'{TOP_API_URL}/person/{wife_id}')
    req_person.start()
    req_person.join()
    wife = Person(req_person.response)

    # Retrieve the children
    print(f'   Retrieving children: {str(new_family.children)[1:-1]}')
    for child_id in new_family.children:
        # Don't request a person if that person is in the tree already
        if not tree.does_person_exist(child_id):
            req_child = Request_thread(f'{TOP_API_URL}/person/{child_id}')
            req_child.start()
            req_child.join()
            child = Person(req_child.response)
            tree.add_person(child)
        
    # go up the path of the husband's parents
    if husband != None:
        tree.add_person(husband)
        depth_fs_pedigree(husband.parents, tree)

    # go up the path of the wife's parents
    if wife != None:
        tree.add_person(wife)
        depth_fs_pedigree(wife.parents, tree)

# -----------------------------------------------------------------------------
# You should not change this function
def part1(log, start_id, generations):
    tree = Tree()

    req = Request_thread(f'{TOP_API_URL}/start/{generations}')
    req.start()
    req.join()

    log.start_timer('Depth-First')
    depth_fs_pedigree(start_id, tree)
    log.stop_timer('Time for Depth-Frist')

    req = Request_thread(f'{TOP_API_URL}/end')
    req.start()
    req.join()

    log.write(tree)

# -----------------------------------------------------------------------------
def breadth_fs_pedigree(start_id, tree):
    # TODO - implement breadth first retrieval
    #      - Limit number of concurrent connections to the FS server to 5
    # This video might help understand BFS
    # https://www.youtube.com/watch?v=86g8jAQug04

    print('WARNING: BFS function not written')

    pass

# -----------------------------------------------------------------------------
# You should not change this function
def part2(log, start_id, generations):
    tree = Tree()

    req = Request_thread(f'{TOP_API_URL}/start/{generations}')
    req.start()
    req.join()

    log.start_timer('Breadth-First')
    breadth_fs_pedigree(start_id, tree)
    log.stop_timer('Time for Breadth-Frist')

    req = Request_thread(f'{TOP_API_URL}/end')
    req.start()
    req.join()

    log.write(tree)


# -----------------------------------------------------------------------------
def main():
    log = Log(show_terminal=True, filename_log='assignment.log')

    # starting family
    req = Request_thread(TOP_API_URL)
    req.start()
    req.join()

    print(f'Starting Family id: {req.response["start_family_id"]}')
    start_id = req.response['start_family_id']

    part1(log, start_id, 6)

    part2(log, start_id, 6)


if __name__ == '__main__':
    main()

