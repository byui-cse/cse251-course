"""
------------------------------------------------------------------------------
Course: CSE 251 
Lesson Week: 02
File: assignment.py 
Author: Brother Comeau

Purpose: Retrieve Star Wars details from a website

Instructions:

- each API call must only retrieve one piece of information
- You are not allowed to use any other modules/packages except for the ones used
  in this assignment.
- The only "fixed" or hard coded URL that you can use is TOP_API_URL.  Use this
  URL to retrieve other URLs that you can use to retrieve information form the
  website.
- You are limited to about 10,000 calls to the swapi website.  That sounds like
  a lot, but you can reach this limit. If you leave this assignment to the last
  day it's due, you might be locked out of the website and you will have to
  submit what you have at that point.  There are no extensions because you
  reached this server limit. Work ahead and spread working on the assignment
  over multiple days.
- You need to match the output outlined in the dcription of the assignment.
  Note that the names are sorted.
- You are requied to use a threaded class (inherited from threading.Thread) for
  this assignment.  This object will make the API calls to the swapi server. You
  can define your class within this Python file (ie., no need to have a seperate
  file for the class)
- Do not add any global variables except for the ones included in this program.
- The main goal of the program is to create as many threads objects (In
  different parts of your program) as you can, then start them all, then wait
  for all of them to finish.

The call to TOP_API_URL will return the following Dictionary.  Do NOT have this
dictionary hard coded - use the API call to get this dictionary.  Then you can
use this dictionary to make other API calls for data.

{
   "people": "http://swapi.dev/api/people/", 
   "planets": "http://swapi.dev/api/planets/", 
   "films": "http://swapi.dev/api/films/",
   "species": "http://swapi.dev/api/species/", 
   "vehicles": "http://swapi.dev/api/vehicles/", 
   "starships": "http://swapi.dev/api/starships/"
}

------------------------------------------------------------------------------
"""

from datetime import datetime, timedelta
import requests
import json
import threading

# Include cse 251 common Python files
import os, sys
sys.path.append('../../code')
from cse251 import *

# Const Values
TOP_API_URL = r'https://swapi.dev/api'

# Global Variables
call_count = 0


# TODO Add your threaded class definition here


# TODO Add any functions you need here


def main():
    log = Log(show_terminal=True)
    log.start_timer('Starting to retrieve data from swapi.dev')

    # TODO Retrieve Top API urls

    # TODO Retireve Details on film 6

    # TODO Display results

    log.stop_timer('Total Time To complete')
    log.write(f'There were {call_count} calls to swapi server')
    

if __name__ == "__main__":
    main()
