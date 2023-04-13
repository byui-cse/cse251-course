"""
Course: CSE 251, week 14
File: common.py
Author: <your name>

Don't change this code.  You are not submitting it with your assignment

"""
import time
import threading
import json
import requests

from cse251 import *

TOP_API_URL = 'http://127.0.0.1:8123'


# ----------------------------------------------------------------------------
class Request_thread(threading.Thread):

    def __init__(self, url):
        # Call the Thread class's init function
        threading.Thread.__init__(self)
        self.__url = url
        self.__response = None

    def get_response(self):
        """ Return the JSON of the API call """
        return self.__response

    def run(self):
        response = requests.get(self.__url)
        # Check the status code to see if the request succeeded.
        if response.status_code == 200:
            self.__response = response.json()
        else:
            self.__response = None
            print('RESPONSE = ', response.status_code)


# ----------------------------------------------------------------------------
class Person:

    def __init__(self, data):
        super().__init__()
        self.__id = data['id']
        self.__name = data['name']
        self.__parents = data['parent_id']
        self.__family = data['family_id']
        self.__birth = data['birth']

    def __str__(self):
        output  = f'id        : {self.__id}\n'
        output += f'name      : {self.__name}\n'
        output += f'birth     : {self.__birth}\n'
        output += f'parent id : {self.__parents}\n'
        output += f'family id : {self.__family}\n'
        return output

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_birth(self):
        return self.__birth

    def get_parentid(self):
        return self.__parents

    def get_familyid(self):
        return self.__family


# ----------------------------------------------------------------------------
class Family:

    def __init__(self, data):
        super().__init__()
        self.__id = data['id']
        self.__husband = data['husband_id']
        self.__wife = data['wife_id']
        self.__children = data['children']

    def children_count(self):
        return len(self.__children)

    def __str__(self):
        output  = f'id         : {self.__id}\n'
        output += f'husband    : {self.__husband}\n'
        output += f'wife       : {self.__wife}\n'
        for id in self.__children:
            output += f'  Child    : {id}\n'
        return output

    def get_id(self):
        return self.__id

    def get_husband(self):
        return self.__husband

    def get_wife(self):
        return self.__wife

    def get_children(self):
        return self.__children


# -----------------------------------------------------------------------------
class Tree:

    def __init__(self, start_family_id):
        super().__init__()
        self.__people = {}
        self.__families = {}
        self.__start_family_id = start_family_id

    def add_person(self, person):
        if self.does_person_exist(person.get_id()):
            print(f'ERROR: Person with ID = {person.get_id()} Already exists in the tree')
        else:
            self.__people[person.get_id()] = person

    def add_family(self, family):
        if self.does_family_exist(family.get_id()):
            print(f'ERROR: Family with ID = {family.get_id()} Already exists in the tree')
        else:
            self.__families[family.get_id()] = family

    def get_person(self, id):
        if id in self.__people:
            return self.__people[id]
        else:
            return None

    def get_family(self, id):
        if id in self.__families:
            return self.__families[id]
        else:
            return None

    def get_person_count(self):
        return len(self.__people)

    def get_family_count(self):
        return len(self.__families)

    def does_person_exist(self, id):
        return id in self.__people

    def does_family_exist(self, id):
        return id in self.__families

    def display(self, log):
        log.write('\n\n')
        log.write(f'{" TREE DISPLAY ":*^40}')
        for family_id in self.__families:
            fam = self.__families[family_id]

            log.write(f'Family id: {family_id}')

            # Husband
            husband = self.get_person(fam.get_husband())
            if husband == None:
                log.write(f'  Husband: None')
            else:
                log.write(f'  Husband: {husband.get_name()}, {husband.get_birth()}')

            # wife
            wife = self.get_person(fam.get_wife())
            if wife == None:
                log.write(f'  Wife: None')
            else:
                log.write(f'  Wife: {wife.get_name()}, {wife.get_birth()}')

            # Parents of Husband
            if husband == None:
                log.write(f'  Husband Parents: None')
            else:
                parent_fam_id = husband.get_parentid()
                if parent_fam_id in self.__families:
                    parent_fam = self.get_family(parent_fam_id)
                    father = self.get_person(parent_fam.get_husband())
                    mother = self.get_person(parent_fam.get_wife())
                    log.write(f'  Husband Parents: {father.get_name()} and {mother.get_name()}')
                else:
                    log.write(f'  Husband Parents: None')

            # Parents of Wife
            if wife == None:
                log.write(f'  Wife Parents: None')
            else:
                parent_fam_id = wife.get_parentid()
                if parent_fam_id in self.__families:
                    parent_fam = self.get_family(parent_fam_id)
                    father = self.get_person(parent_fam.get_husband())
                    mother = self.get_person(parent_fam.get_wife())
                    log.write(f'  Wife Parents: {father.get_name()} and {mother.get_name()}')
                else:
                    log.write(f'  Wife Parents: None')

            # children
            output = []
            for index, child_id in enumerate(fam.get_children()):
                person = self.__people[child_id]
                output.append(f'{person.get_name()}')
            out_str = str(output).replace("'", '', 100)
            log.write(f'  Children: {out_str[1:-1]}')

        log.write('')
        log.write(f'Number of people                    : {len(self.__people)}')
        log.write(f'Number of families                  : {len(self.__families)}')
        log.write(f'Max generations                     : {self._count_generations(self.__start_family_id)}')
        log.write(f'People connected to starting family : {self._test_number_connected_to_start()}')


    def _test_number_connected_to_start(self):
        # start with first family, how many connected to that family
        inds_seen = set()

        def _recurive(family_id):
            nonlocal inds_seen
            if family_id in self.__families:
                # count people in this family
                fam = self.__families[family_id]

                husband = self.get_person(fam.get_husband())
                if husband != None:
                    if husband.get_id() not in inds_seen:
                        inds_seen.add(husband.get_id())
                    _recurive(husband.get_parentid())
                
                wife = self.get_person(fam.get_wife())
                if wife != None:
                    if wife.get_id() not in inds_seen:
                        inds_seen.add(wife.get_id())
                    _recurive(wife.get_parentid())

                for child_id in fam.get_children():
                    if child_id not in inds_seen:
                        inds_seen.add(child_id)


        _recurive(self.__start_family_id)
        return len(inds_seen)


    def _count_generations(self, family_id):
        max_gen = -1

        def _recurive_gen(id, gen):
            nonlocal max_gen
            if id in self.__families:
                if max_gen < gen:
                    max_gen = gen

                fam = self.__families[id]

                husband = self.get_person(fam.get_husband())
                if husband != None:
                    _recurive_gen(husband.get_parentid(), gen + 1)
                
                wife = self.get_person(fam.get_wife())
                if wife != None:
                    _recurive_gen(wife.get_parentid(), gen + 1)

        _recurive_gen(family_id, 0)
        return max_gen + 1

