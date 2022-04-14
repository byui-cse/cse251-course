"""
File: server.py
Course: CSE251
Author: Brother Comeau

Instructions
- In a terminal window, run "python server.py"

Top level url returns the following
{
   "people": "http://127.0.0.1:8790/people/", 
   "planets": "http://127.0.0.1:8790/planets/", 
   "films": "http://127.0.0.1:8790/films/",
   "species": "http://127.0.0.1:8790/species/", 
   "vehicles": "http://127.0.0.1:8790/vehicles/", 
   "starships": "http://127.0.0.1:8790/starships/"
}

"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading
import time
import json
import os

TOP_API_URL = 'http://127.0.0.1:8790'

URL_PEOPLE    = "people"
URL_PLANETS   = "planets"
URL_FILMS     = "films"
URL_SPECIES   = "species"
URL_VEHICLES  = "vehicles"
URL_STARSHIPS = "starships"

DELAY = 1.0         # one second

master_dict = {}

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        global master_dict
        print(f'Request: {self.path}')

        # self.path => "/people/1"

        # delay the reply from the server
        time.sleep(DELAY)

        # check to top level URL
        if self.path == '/':
            reply = '{"people": "http://127.0.0.1:8790/people/", ' + \
                    '"planets": "http://127.0.0.1:8790/planets/", '  + \
                    '"films": "http://127.0.0.1:8790/films/", ' + \
                    '"species": "http://127.0.0.1:8790/species/", ' + \
                    '"vehicles": "http://127.0.0.1:8790/vehicles/", '  + \
                    '"starships": "http://127.0.0.1:8790/starships/"}'
            self.send_response(200)
            self.end_headers()
            self.wfile.write(str.encode(reply))
        else:
            # remove the ending '/' if found
            if self.path[-1] == '/':
                self.path = self.path[:-1]

            request = self.path[1:]   # "people/1"
            parts = request.split('/')
            # print(parts)
            if len(parts) != 2:
                self.send_error(404)
                # self.wfile.write(str.encode('Error 404 - not found'))
            else:
                command = parts[0]
                # Check for valid command
                if command not in (URL_PEOPLE, URL_PLANETS, URL_FILMS, URL_SPECIES, URL_VEHICLES, URL_STARSHIPS):
                    self.send_error(404)
                    # self.wfile.write(str.encode('Error 404 - not found'))
                else:
                    # check for valid id
                    id = parts[1]
                    if not id.isnumeric():
                        self.send_error(404)
                        # self.wfile.write(str.encode('Error 404 - not found'))
                    else:
                        key = f'{command}{id}'
                        if key not in master_dict:
                            self.send_error(404)
                            # self.wfile.write(str.encode('Error 404 - not found'))
                        else:
                            self.send_response(200)
                            self.end_headers()
                            # self.wfile.write(b'Hello world\t' + threading.current_thread().name.encode() + b'\t' + str(threading.active_count()).encode() + b'\n')
                            js = str(master_dict[key]).replace("'", '"')
                            # print()
                            # print(js)
                            # print()
                            self.wfile.write(str.encode(js))


class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass


def run():
    global master_dict

    if not os.path.exists('data.txt'):
        print('Error the file "data.txt" not found')
        return

    # load dict
    with open('data.txt') as f:
        data = f.read()
      
    # reconstructing the data as a dictionary
    master_dict = json.loads(data)

    # testing
    # print(type(master_dict['people1']))
    # print(master_dict['films6'])

    print(f'Star Wars server waiting..... \nURL: {TOP_API_URL}')

    server = ThreadingSimpleServer(('localhost', 8790), Handler)
    server.serve_forever()


if __name__ == '__main__':
    run()