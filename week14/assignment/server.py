"""
Course: CSE 251
Lesson Week: 13
File: server.py
Author: Brother Comeau
Purpose: Assignment 14 - Family Search

Instructions:

Open a terminal window and run this program

*******************  DO NOT MODIFY!!!!  *********************
*******************  DO NOT MODIFY!!!!  *********************
*******************  DO NOT MODIFY!!!!  *********************
*******************  DO NOT MODIFY!!!!  *********************
*******************  DO NOT MODIFY!!!!  *********************
*******************  DO NOT MODIFY!!!!  *********************
*******************  DO NOT MODIFY!!!!  *********************

"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import datetime
import json
import time
import random
import threading

hostName = "127.0.0.1"
serverPort = 8123

SLEEP = 0.25
MAX_GENERATIONS = 6

primes = (5000007787, 5000007797, 5000007799, 5000007811, 5000007823, 5000007829, 5000007877, 5000007899,
            5000007911, 5000007919, 5000007953, 5000007977, 5000007983, 5000008007, 5000008037, 5000008043, 5000008109, 5000008121,
            5000008127, 5000008133, 5000008147, 5000008151, 5000008201, 5000008219, 5000008271, 5000008297, 5000008313, 5000008319,
            5000008361, 5000008369, 5000008373, 5000008417)
PRIME = random.choice(primes)
ID = random.randint(10000, 10000000)

male_names = ('Liam', 'Noah', 'Oliver', 'William', 'Elijah', 'James', 
        'Benjamin', 'Lucas', 'Mason', 'Ethan', 'Alexander', 
        'Henry', 'Jacob', 'Michael', 'Daniel', 'Logan', 
        'Jackson', 'Sebastian', 'Jack', 'Aiden', 'Owen', 
        'Samuel', 'Matthew', 'Joseph', 'Levi', 'Mateo', 
        'David', 'John', 'Wyatt', 'Carter', 'Julian', 
        'Luke', 'Grayson', 'Isaac', 'Jayden', 'Theodore', 
        'Gabriel', 'Anthony', 'Dylan', 'Leo', 'Lincoln', 
        'Jaxon', 'Asher', 'Christopher', 'Josiah', 'Andrew', 
        'Thomas', 'Joshua', 'Ezra', 'Hudson')

female_names = ('Olivia', 'Emma', 'Ava', 'Sophia', 'Isabella', 'Charlotte', 'Amelia', 
            'Mia', 'Harper', 'Evelyn', 'Abigail', 'Emily', 'Ella', 
            'Elizabeth', 'Camila', 'Luna', 'Sofia', 'Avery', 'Mila', 
            'Aria', 'Scarlett', 'Penelope', 'Layla', 'Chloe', 'Victoria', 'Madison', 
            'Eleanor', 'Grace', 'Nora', 'Riley', 'Zoey', 'Hannah', 'Hazel', 
            'Lily', 'Ellie', 'Violet', 'Lillian', 'Zoe', 'Stella', 'Aurora', 
            'Natalie', 'Emilia', 'Everly', 'Leah', 'Aubrey', 'Willow', 
            'Addison', 'Lucy', 'Audrey', 'Bella')

surnames = ('Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Wilson', 'Martinez', 
            'Anderson', 'Taylor', 'Thomas', 'Hernandez', 'Moore', 'Martin', 'Jackson', 'Thompson', 'White', 'Lopez', 
            'Lee', 'Gonzalez', 'Harris', 'Clark', 'Lewis', 'Robinson', 'Walker', 'Perez', 'Hall', 'Young', 
            'Allen', 'Sanchez', 'Wright', 'King', 'Scott', 'Green', 'Baker', 'Adams', 'Nelson', 'Hill', 'Ramirez', 'Campbell', 
            'Mitchell', 'Roberts', 'Carter', 'Phillips', 'Evans', 'Turner', 'Torres', 'Parker', 'Collins', 'Edwards', 'Stewart', 'Flores', 
            'Morris', 'Nguyen', 'Murphy', 'Rivera', 'Cook', 'Rogers', 'Morgan', 'Peterson', 'Cooper', 'Reed', 'Bailey', 'Bell', 
            'Gomez', 'Tremblay', 'Gagnon', 'Roy', 'Côté', 'Bouchard', 'Hernández', 'García', 'Martínez', 'González', 'López', 'Rodríguez', 
            'Pérez', 'Sánchez', 'Ramírez', 'Flores', 'Gómez', 'Torres', 'Díaz', 'Vásquez', 
            'Cruz', 'Morales', 'Gutiérrez', 'Reyes', 'Ruíz', 'Jiménez')

max_thread_count = 0
thread_count = 0
lock = threading.Lock()

family_request_order = []
people = {}
families = {}
generations_created = 0


def get_name_male():
    return random.choice(male_names)


def get_name_female():
    return random.choice(female_names)

def get_surname():
    return random.choice(surnames)

def get_date():
    start_date = datetime.date(1753, 1, 1)
    end_date = datetime.date(2020, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return f'{random_date.day}-{random_date.month}-{random_date.year}'

def encode(id: int):
    if id == None:
        return None
    else:
        return (id * ID) ^ PRIME

def decode(code: int):
    if id == None:
        return None
    else:
        return (code ^ PRIME) // ID

class Log:

    def __init__(self, filename):
        super().__init__()
        self.lock = threading.Lock()
        self.filename = filename
        self.file = open(filename, 'w')

    def write(self, line):
        with self.lock:
            self.file.write(line)
            self.file.write('\n')
            self.file.flush()

    def __del__(self):
        self.file.close()

# Global log object
log = Log('server.log')

# ----------------------------------------------------------------------------
class Person:
    
    def __init__(self, id, name):
        super().__init__()
        self.id = id
        self.name = name
        self.parents = None
        self.family = None
        self.birth = get_date()

    def add_birth(self, date_str):
        self.birth = date_str

    def add_parents(self, id):
        self.parents = id

    def add_family(self, id):
        self.family = id

    def get_dict(self):
        person_dict = {}
    
        person_dict["id"] = encode(self.id)
        person_dict["name"] = self.name
        person_dict["birth"] = self.birth
        person_dict["parent_id"] = encode(self.parents)
        person_dict["family_id"] = encode(self.family)
    
        return person_dict

    def __str__(self):
        output  = f'id        : {encode(self.id)}\n'
        output += f'name       : {self.name}\n'
        output += f'birth      : {self.birth}\n'
        output += f'parent id : {encode(self.parents)}\n'
        output += f'family id : {encode(self.family)}\n'

        return output

# ----------------------------------------------------------------------------
class Family:

    def __init__(self, id, husband, wife):
        super().__init__()
        self.id = id
        self.husband = husband
        self.wife = wife
        self.children = []

    def add_child(self, id):
        self.children.append(id)
        
    def get_dict(self):
        family_dict = {}
    
        family_dict["id"] = encode(self.id)
        family_dict["husband_id"] = encode(self.husband)
        family_dict["wife_id"] = encode(self.wife)
        ids = []
        for child in self.children:
            ids.append(encode(child.id))
        family_dict["children"] = ids
    
        return family_dict

    def __str__(self):
        output  = f'id         : {encode(self.id)}\n'
        output += f'husband    : {encode(self.husband)}\n'
        output += f'wife       : {encode(self.wife)}\n'
        for child in self.children:
            output += f'  Child    : {encode(child.id)}\n'

        return output


# ----------------------------------------------------------------------------
def build_tree(gens):
    global people
    global families
    global log

    people = {}
    families = {}

    next_person_id = 1
    next_family_id = 1

    def _create_family(generation):
        nonlocal next_person_id
        nonlocal next_family_id
        
        # print(f'Generation: {generation}')
        # print(f'next person / family: {next_person_id} / {next_family_id}')
        if generation < 1:
            return

        husband = Person(next_person_id, get_name_male())
        people[next_person_id] = husband
        next_person_id += 1

        wife = Person(next_person_id, get_name_female())
        people[next_person_id] = wife
        next_person_id += 1

        family = Family(next_family_id, husband.id, wife.id)
        husband.add_family(next_family_id)
        wife.add_family(next_family_id)
        families[next_family_id] = family
        next_family_id += 1

        number_children = random.randint(0, 8)
        for i in range(number_children):
            if random.randint(1, 2) == 1:
                child = Person(next_person_id, get_name_male())
            else:
                child = Person(next_person_id, get_name_female())
            people[next_person_id] = child
            family.add_child(child)
            next_person_id += 1


        if generation > 1:
            if random.randint(1, 10) != 1:
                # create parents and recurve calls
                husband_parents = _create_family(generation - 1)
                husband.add_parents(husband_parents.id)
                husband_parents.add_child(husband)

            if random.randint(1, 10) != 1:
                wife_parents = _create_family(generation - 1)
                wife.add_parents(wife_parents.id)
                wife_parents.add_child(wife)


        # return the family that was created
        return family

    _create_family(gens)

    print(f'Number of people  : {len(people)}')
    print(f'Number of families: {len(families)}')
    log.write(f'Number of people  : {len(people)}')
    log.write(f'Number of families: {len(families)}')

    
# ----------------------------------------------------------------------------
class Handler(BaseHTTPRequestHandler):

    def get_person(self, id):
        global people
        if id in people:
            return people[id].get_dict()
        else:
            return None


    def get_family(self, id):
        global families
        if id in families:
            return families[id].get_dict()
        else:
            return None
 
    def do_GET(self):
        global thread_count
        global lock
        global max_thread_count
        global family_request_order
        global log
        global generations_created

        with lock:
            thread_count += 1
            if thread_count > max_thread_count:
                max_thread_count = thread_count
            print(f'Current: active threads / max count: {thread_count} / {max_thread_count}')
            log.write(f'Current: active threads / max count: {thread_count} / {max_thread_count}')

        print('- ' * 35)
        print(f'Request: {self.path}')

        log.write(f'Request: {self.path}')

        if SLEEP > 0:
            time.sleep(SLEEP)

        if 'start' in self.path:
            family_request_order = []
            parts = self.path.split('/')
            if len(parts) < 3:
                self.send_response(404)
                self.send_header("Content-type",  "application/json")
                self.end_headers()
                with lock:
                    thread_count -= 1
                return

            try:
                generations = int(parts[-1])
            except:
                generations = MAX_GENERATIONS

            output = f'Creating family tree with {generations} generations...'
            print(output)
            log.write(output)

            generations_created = generations
            build_tree(generations)

            max_thread_count = 1
            thread_count = 1

            json_data = '{"status":"OK"}'

                    
        elif 'end' in self.path:
            print('#' * 80)
            log.write('#' * 80)

            print(f'Total number of people  : {len(people)}')
            print(f'Total number of families: {len(families)}')
            print(f'Number of generations   : {generations_created}')
            log.write(f'Total number of people  : {len(people)}')
            log.write(f'Total number of families: {len(families)}')
            log.write(f'Number of generations   : {generations_created}')


            print('Families were requested in this order:')
            log.write('Families were requested in this order:')
            
            output = str(family_request_order)[1:-1]
            print(output)
            log.write(output)

            print(f'Final thread count (max count): {max_thread_count}')
            log.write(f'Final thread count (max count): {max_thread_count}')

            json_data = '{"status":"OK"}'

            print('#' * 80)
            log.write('#' * 80)

        elif 'person' in self.path or 'family' in self.path:
            parts = self.path.split('/')
            # print('****************************')
            # print(parts)

            if len(parts) < 3:
                self.send_response(404)
                self.send_header("Content-type",  "application/json")
                self.end_headers()
                with lock:
                    thread_count -= 1
                return

            try:
                id = decode(int(parts[-1]))
            except:
                id = None

            if id == None:
                self.send_response(404)
                self.send_header("Content-type",  "application/json")
                self.end_headers()
                with lock:
                    thread_count -= 1
                return

            if 'person' in self.path:
                data = self.get_person(id)
            else:
                data = self.get_family(id)
                family_request_order.append(id)

            if data != None:
                json_data = json.dumps(data)
            else:
                json_data = None
        else:
            start_id = 1 # random.randint(1, 100000)
            data = {"start_family_id" : encode(start_id)}
            json_data = json.dumps(data)

        if json_data == None:
            self.send_response(404)
            self.send_header("Content-type",  "application/json")
            self.end_headers()
        else:
            print('Sending:', json_data)
            log.write(f'Sending: {json_data}')

            self.send_response(200)
            self.send_header("Content-type",  "application/json")
            self.end_headers()
            self.wfile.write(bytes(json_data, "utf8"))

        with lock:
            thread_count -= 1

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    random.seed(101)

    # for id in people:
    #     print(people[id])
    # print('*' * 50)
    # for id in families:
    #     print(families[id])


    server = ThreadedHTTPServer((hostName, serverPort), Handler)
    print('Starting server, use <Ctrl-C> or <Command-C> to stop')
    server.serve_forever()
