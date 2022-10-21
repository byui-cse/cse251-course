"""
Course: CSE 251 
Lesson Week: 02
File: assignment.py 
Author: Brother Comeau

Purpose: Retrieve Star Wars details from a server

Instructions:

- Each API call must only retrieve one piece of information
- You are not allowed to use any other modules/packages except for the ones used
  in this assignment.
- Run the server.py program from a terminal/console program.  Simply type
  "python server.py"
- The only "fixed" or hard coded URL that you can use is TOP_API_URL.  Use this
  URL to retrieve other URLs that you can use to retrieve information from the
  server.
- You need to match the output outlined in the decription of the assignment.
  Note that the names are sorted.
- You are requied to use a threaded class (inherited from threading.Thread) for
  this assignment.  This object will make the API calls to the server. You can
  define your class within this Python file (ie., no need to have a seperate
  file for the class)
- Do not add any global variables except for the ones included in this program.

The call to TOP_API_URL will return the following Dictionary(JSON).  Do NOT have
this dictionary hard coded - use the API call to get this.  Then you can use
this dictionary to make other API calls for data.

{
   "people": "http://127.0.0.1:8790/people/", 
   "planets": "http://127.0.0.1:8790/planets/", 
   "films": "http://127.0.0.1:8790/films/",
   "species": "http://127.0.0.1:8790/species/", 
   "vehicles": "http://127.0.0.1:8790/vehicles/", 
   "starships": "http://127.0.0.1:8790/starships/"
}
"""

from datetime import datetime, timedelta
import requests
import json
import threading

# Include cse 251 common Python files
from cse251 import *

# Const Values
TOP_API_URL = 'http://127.0.0.1:8790'

# Global Variables
call_count = 0


# TODO Add your threaded class definition here
class RequestThread(threading.Thread):
    # https://realpython.com/python-requests/
    # constructor
    def __init__(self, url):
        # calling parent class constructor
        super().__init__()
        self.url = url
        self.response = {}

    # This is the method that is run when start() is called
    # TODO Add any functions you need here
    def run(self):
        response = requests.get(self.url)
        global call_count
        call_count += 1
        if response.status_code == 200:
            self.response = response.json()
        else:
            print(f"Error code: {response.status_code}", flush=True)


def main():
    log = Log(show_terminal=True)
    log.start_timer('Starting to retrieve data from the server')

    # TODO Retrieve Top API urls
    getSecondaryUrls = RequestThread(TOP_API_URL)
    getSecondaryUrls.start()
    getSecondaryUrls.join()
    SECONDARY_URLS = getSecondaryUrls.response

    # print_dict(SECONDARY_URLS)
    # TODO Retrieve Details on film 6
    film_six_url = SECONDARY_URLS['films'] + '6'
    film_six = RequestThread(film_six_url)
    film_six.start()
    film_six.join()
    # print_dict(film_six.response)

    character_Threads = [RequestThread(url) for url in film_six.response["characters"]]
    planets_Threads = [RequestThread(url) for url in film_six.response["planets"]]
    starships_Threads = [RequestThread(url) for url in film_six.response["starships"]]
    vehicles_Threads = [RequestThread(url) for url in film_six.response["vehicles"]]
    species_Threads = [RequestThread(url) for url in film_six.response["species"]]

    [thread.start() for thread in character_Threads]
    [thread.start() for thread in planets_Threads]
    [thread.start() for thread in starships_Threads]
    [thread.start() for thread in vehicles_Threads]
    [thread.start() for thread in species_Threads]

    [thread.join() for thread in character_Threads]
    [thread.join() for thread in planets_Threads]
    [thread.join() for thread in starships_Threads]
    [thread.join() for thread in vehicles_Threads]
    [thread.join() for thread in species_Threads]

    characters = [thread.response['name'] for thread in character_Threads]
    planets = [thread.response['name'] for thread in planets_Threads]
    starships = [thread.response['name'] for thread in starships_Threads]
    vehicles = [thread.response['name'] for thread in vehicles_Threads]
    species = [thread.response['name'] for thread in species_Threads]

    characters.sort()
    planets.sort()
    starships.sort()
    vehicles.sort()
    species.sort()

    # TODO Display results
    log.write("-----------------------------------------")
    log.write(f'Title   : {film_six.response["title"]}')
    log.write(f'Director: {film_six.response["director"]}')
    log.write(f'Producer: {film_six.response["producer"]}')
    log.write(f'Released: {film_six.response["release_date"]}')

    log.write('')

    log.write("Characters: {}".format(len(characters)))
    log.write(", ".join(characters))

    log.write('')

    log.write("Planets: {}".format(len(planets)))
    log.write(", ".join(planets))

    log.write('')

    log.write("Starships: {}".format(len(starships)))
    log.write(", ".join(starships))

    log.write('')

    log.write("Vehicles: {}".format(len(vehicles)))
    log.write(", ".join(vehicles))

    log.write('')

    log.write("Species: {}".format(len(species)))
    log.write(", ".join(species))
    log.write('')

    log.stop_timer('Total Time To complete')
    log.write(f'There were {call_count} calls to the server')
    

if __name__ == "__main__":
    main()
