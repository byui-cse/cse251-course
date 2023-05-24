"""
Course: CSE 251
Lesson Week: 02 - Team Activity
File: team.py
Author: Brother Comeau

Purpose: Playing Card API calls
"""

from datetime import datetime, timedelta
import threading
import requests
import json

# # Include cse 251 common Python files
from cse251 import *

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


class Deck:

    def __init__(self, deck_id):
        self.id = deck_id
        self.reshuffle()
        self.remaining = 52


    def reshuffle(self):
        req = Request_thread(rf'https://deckofcardsapi.com/api/deck/{self.id}/shuffle/')
        req.start()
        req.join()


    def draw_card(self):
        req = Request_thread(rf'https://deckofcardsapi.com/api/deck/{self.id}/draw/')
        req.start()
        req.join()
        if req.response != {}:
            self.remaining = req.response['remaining']
            return req.response['cards'][0]['code']
        else:
            return ''

    def cards_remaining(self):
        return self.remaining


    def draw_endless(self):
        if self.remaining <= 0:
            self.reshuffle()
        return self.draw_card()


if __name__ == '__main__':

    # TODO - run the program team_get_deck_id.py and insert
    #        the deck ID here.  You only need to run the 
    #        team_get_deck_id.py program once. You can have
    #        multiple decks if you need them

    deck_id = 'ENTER ID HERE'

    deck = Deck(deck_id)

    for i in range(55):
        card = deck.draw_endless()
        print(f'card {i + 1}: {card}', flush=True)

    print()
