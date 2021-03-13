"""
Course: CSE 251
Lesson Week: 11
File: Assignment.py
Author: <Your name>

Purpose: Week 11 assignment


Passengers (TOTAL_PASSENGERS) will be boarding a cruise ship.  Security
officers will add arriving passengers to a pasenger list.  There will be
mulitple entry points to get on the ship.  While the boarding process is going
on, ship directors will check the passenger list now and then so they can do
any planning they need to do.

While security offices are updating the pasenger list, no other security
officer or director can be using the list.

Directors can not read the passenger list if any security officer is updating
the list.  However, mulitple directors can read the list at the same time.

When Security and directors get access to the passenger list, they will take
security_processing(), director_processing() amount of time with
the list.  When they are not using the list, they will wait using these
functions security_waiting() and director_waiting() before trying
to access the passenger list again.

Passneger list: Each passenger has an ID.  There IDs will be integers starting at 1.  
The first will use ID = 1, the second passenger to arrive will use 2, etc.

Instructions:

- Use processes for the security (SECURITY_PERSONAL) and directors (DIRECTOR_PERSONAL)
- Make sure the directors print the messages STARTING_READING_MESSAGE and STOPING_READING_MESSAGE
- When using locks, the acquire() method must not use the timeout or block options. (ie., just lock.acquire())
- This problem is harder if you use the Python 'with lock:' statement.
- Add lots of print statements while debugging your program.  Remove them before 
  you submit your assignment.
- Use only the imported packages below.

"""

import time
import random
import multiprocessing as mp

# Number of passengers that will board the ship
TOTAL_PASSENGERS = 30

# number of security and ship directors
SECURITY_PERSONAL = 2
DIRECTOR_PERSONAL = 4

# When the first director starts reading the passenger list, display this message
STARTING_READING_MESSAGE = 'Directors reading vvvvvvvvvvvvvvvvvvvvvvv'

# When the last director ends reading the passenger list, display this message
STOPING_READING_MESSAGE  = 'Directors have stopped reading ^^^^^^^^^^'

# All done Passenger ID 
ALL_DONE = -1

# -----------------------------------------------------------------------------
def security_waiting():
    time.sleep(random.uniform(0, 1))

# -----------------------------------------------------------------------------
def security_processing():
    time.sleep(random.uniform(0, 1))

# -----------------------------------------------------------------------------
def director_waiting():
    time.sleep(random.uniform(0, 1))

# -----------------------------------------------------------------------------
def director_processing():
    time.sleep(random.uniform(0, .5))

# -----------------------------------------------------------------------------
def security(passenger_list, lock):
    """
    while there are still passengers to arrive
        security will wait for a passenger to arrive
        get access to the passenger list
        add passenger ID to the list (this takes time)
            when adding a passenger, use this print statement
            print(f'Security adding passenger: {id}')

    When the last security officer logs the last passenger, that officer adds 
    ALL_DONE to the passenger list.  Use this statement "print(f'Security: ALL Done')"
    """
    pass


# -----------------------------------------------------------------------------
def cruise_director(passenger_list, lock_directors, lock_security, directors_count):
    """
    while there are still passengers arriving (look for ALL_DONE)
        director will wait to access the passenger list
        if no security officer is updating the list
            start reading the list.
            if this is the first director reading the list, display a message (STARTING_READING_MESSAGE)
            before reading, display the message:
                print(f'Director reading: list size is {len(passenger_list)}')
            take some time reading the list.  
            after reading, if this is the last director, display message (STOPING_READING_MESSAGE)
    """
    pass

# -----------------------------------------------------------------------------
def main():
    # Passenger list
    passenger_list = mp.Manager().list()

    # Lock for the directors
    lock_directors = mp.Manager().Lock()
    
    # Lock for the security officers
    lock_security = mp.Manager().Lock()

    # Number of directors currently reading the passenger list
    directors_count = mp.Manager().Value('i', 0)
   
    # TODO - any other variables you need


    security_persons = []
    for _ in range(SECURITY_PERSONAL):
        security_persons.append(mp.Process(target=security, args=(passenger_list, lock_security)))

    director_persons = []
    for _ in range(DIRECTOR_PERSONAL):
        director_persons.append(mp.Process(target=cruise_director, args=(passenger_list, lock_directors, lock_security, directors_count)))

    # Start all
    for person in director_persons:
        person.start()
    for person in security_persons:
        person.start()

    # join all
    for person in director_persons:
        person.join()
    for person in security_persons:
        person.join()

    # Results
    print(f'All aboard.  Size of passenger list = {len(passenger_list) - 1}')


if __name__ == '__main__':
    main()

