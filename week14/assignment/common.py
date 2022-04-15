"""
Course: CSE 251, week 14
File: common.py
Author: <your name>
"""
import time
import threading
import json
import requests


# Include cse 251 common Python files - Dont change
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

    def __init__(self, start_family_id):
        super().__init__()
        self.people = {}
        self.families = {}
        self.start_family_id = start_family_id

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

    def display(self, log):
        log.write('\n\n')
        log.write(f'{" TREE DISPLAY ":*^40}')
        for family_id in self.families:
            fam = self.families[family_id]

            log.write(f'Family id: {family_id}')

            # Husband
            husband = self.get_person(fam.husband)
            if husband == None:
                log.write(f'  Husband: None')
            else:
                log.write(f'  Husband: {husband.name}, {husband.birth}')

            # wife
            wife = self.get_person(fam.wife)
            if wife == None:
                log.write(f'  Wife: None')
            else:
                log.write(f'  Wife: {wife.name}, {wife.birth}')

            # Parents of Husband
            if husband == None:
                log.write(f'  Husband Parents: None')
            else:
                parent_fam_id = husband.parents
                if parent_fam_id in self.families:
                    parent_fam = self.get_family(parent_fam_id)
                    father = self.get_person(parent_fam.husband)
                    mother = self.get_person(parent_fam.wife)
                    log.write(f'  Husband Parents: {father.name} and {mother.name}')
                else:
                    log.write(f'  Husband Parents: None')

            # Parents of Wife
            if wife == None:
                log.write(f'  Wife Parents: None')
            else:
                parent_fam_id = wife.parents
                if parent_fam_id in self.families:
                    parent_fam = self.get_family(parent_fam_id)
                    father = self.get_person(parent_fam.husband)
                    mother = self.get_person(parent_fam.wife)
                    log.write(f'  Wife Parents: {father.name} and {mother.name}')
                else:
                    log.write(f'  Wife Parents: None')

            # children
            output = []
            for index, child_id in enumerate(fam.children):
                person = self.people[child_id]
                output.append(f'{person.name}')
            out_str = str(output).replace("'", '', 100)
            log.write(f'  Children: {out_str[1:-1]}')

        log.write('')
        log.write(f'Number of people                    : {len(self.people)}')
        log.write(f'Number of families                  : {len(self.families)}')
        log.write(f'Max generations                     : {self._count_generations(self.start_family_id)}')
        log.write(f'People connected to starting family : {self._test_number_connected_to_start()}')


    def _test_number_connected_to_start(self):
        # start with first family, how many connected to that family
        inds_seen = set()

        def _recurive(family_id):
            nonlocal inds_seen
            if family_id in self.families:
                # count people in this family
                fam = self.families[family_id]

                husband = self.get_person(fam.husband)
                if husband != None:
                    if husband.id not in inds_seen:
                        inds_seen.add(husband.id)
                    _recurive(husband.parents)
                
                wife = self.get_person(fam.wife)
                if wife != None:
                    if wife.id not in inds_seen:
                        inds_seen.add(wife.id)
                    _recurive(wife.parents)

                for child_id in fam.children:
                    if child_id not in inds_seen:
                        inds_seen.add(child_id)


        _recurive(self.start_family_id)
        return len(inds_seen)


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

        _recurive_gen(family_id, 0)
        return max_gen + 1


# ----------------------------------------------------------------------------
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

